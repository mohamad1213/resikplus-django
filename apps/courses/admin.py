from django.contrib import admin
from .models import Course, Module, Lesson, CourseRegistration


# ─── Inline: Lesson di dalam Module ───────────────────────────────────────────

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ['order', 'title', 'type', 'duration', 'content']
    ordering = ['order']


# ─── Inline: Module di dalam Course ───────────────────────────────────────────

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    fields = ['order', 'title', 'description']
    ordering = ['order']
    show_change_link = True  # link ke halaman Module untuk edit Lesson-nya


# ─── Course Admin ──────────────────────────────────────────────────────────────

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ['title', 'level', 'type', 'status', 'price', 'students_count', 'lessons_count', 'created_at']
    list_filter   = ['status', 'level', 'type']
    search_fields = ['title', 'instructor', 'description']
    ordering      = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Informasi Kursus', {
            'fields': ('title', 'subtitle', 'description', 'instructor', 'image')
        }),
        ('Detail Kursus', {
            'fields': ('level', 'type', 'duration', 'price', 'features')
        }),
        ('Status & Statistik', {
            'fields': ('status', 'students_count', 'lessons_count')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    inlines = [ModuleInline]


# ─── Module Admin (standalone, agar bisa edit Lesson-nya) ─────────────────────

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display  = ['title', 'course', 'order']
    list_filter   = ['course']
    search_fields = ['title', 'course__title']
    ordering      = ['course', 'order']

    inlines = [LessonInline]


# ─── Course Registration Admin ─────────────────────────────────────────────────

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'phone', 'course', 'created_at']
    list_filter   = ['course']
    search_fields = ['full_name', 'email', 'phone']
    ordering      = ['-created_at']
    readonly_fields = ['full_name', 'email', 'phone', 'course', 'notes', 'created_at']

    # Pendaftar tidak boleh diedit/dihapus sembarangan
    def has_add_permission(self, request):
        return False
