from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.utils.crypto import get_random_string

from apps.partners.models import Partner
from apps.accounts.models import User


class PartnerAdmin(admin.ModelAdmin):
    list_display  = ['name', 'type', 'location', 'status', 'email', 'has_account']
    list_editable = ['status']
    list_filter   = ['type', 'status']
    search_fields = ['name', 'location', 'email']
    ordering      = ['name']
    readonly_fields = ['user', 'show_generated_password', 'created_at', 'updated_at']

    fieldsets = (
        ('Informasi Utama', {
            'fields': ('name', 'type', 'location', 'status', 'join_date')
        }),
        ('Kontak', {
            'fields': ('email', 'phone', 'address', 'contact_person', 'description')
        }),
        ('Akun Sistem', {
            'fields': ('user', 'show_generated_password'),
            'description': (
                'Akun login akan dibuat otomatis saat status diubah menjadi '
                '<strong>Aktif</strong>. Password hanya tampil saat pertama kali dibuat.'
            ),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # ---------- helpers ----------

    @admin.display(boolean=True, description='Punya Akun')
    def has_account(self, obj):
        return obj.user_id is not None

    @admin.display(description='Generated Password')
    def show_generated_password(self, obj):
        """
        Tampilkan password yang disimpan sementara di _plain_password
        (hanya ada jika baru saja dibuat pada request ini).
        """
        pwd = getattr(obj, '_plain_password', None)
        if pwd:
            return format_html(
                '<strong style="color:#e74c3c; font-size:1.1em;">{}</strong>'
                '&nbsp;<span style="color:#888;">(Simpan sekarang – tidak akan ditampilkan lagi)</span>',
                pwd
            )
        if obj.user_id:
            return format_html(
                '<span style="color:#27ae60;">Password sudah tersimpan (tidak bisa dilihat lagi)</span>'
            )
        return format_html('<span style="color:#888;">-</span>')

    # ---------- save override ----------

    def save_model(self, request, obj, form, change):
        status_changed_to_aktif = (
            'status' in form.changed_data
            and obj.status == 'Aktif'
        )
        is_new_and_aktif = (not change and obj.status == 'Aktif')

        if (status_changed_to_aktif or is_new_and_aktif) and obj.user_id is None:
            if not obj.email:
                messages.error(
                    request,
                    '⚠️  Email partner belum diisi. Akun tidak dapat dibuat otomatis.'
                )
                super().save_model(request, obj, form, change)
                return

            # Cek apakah email sudah dipakai
            if User.objects.filter(email=obj.email).exists():
                existing_user = User.objects.get(email=obj.email)
                obj.user = existing_user
                messages.warning(
                    request,
                    f'Email {obj.email} sudah terdaftar. Partner ditautkan ke akun yang ada.'
                )
            else:
                plain_password = f"ResikPlus@{get_random_string(5)}"
                new_user = User.objects.create_user(
                    email=obj.email,
                    password=plain_password,
                    is_active=True,
                    is_verified=True,
                    is_staff=False,
                    is_superuser=False,
                )

                # Simpan sementara di instance agar show_generated_password bisa baca
                obj._plain_password = plain_password
                obj.user = new_user

                messages.success(
                    request,
                    format_html(
                        '✅ Akun berhasil dibuat untuk <strong>{}</strong> '
                        '— Email: <strong>{}</strong> | Password: <strong>{}</strong> '
                        '<em>(Catat password ini sekarang!)</em>',
                        obj.name, obj.email, plain_password
                    )
                )

        super().save_model(request, obj, form, change)

        # Setelah save, _plain_password masih ada di obj sehingga
        # readonly field show_generated_password bisa menampilkannya
        # pada halaman change yang langsung di-redirect setelah save.


admin.site.register(Partner, PartnerAdmin)
