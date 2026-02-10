import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.courses.models import Course, Module, Lesson

def create_dummy_modules():
    # Helper to clean up existing modules to avoid duplicates if run multiple times
    # Module.objects.all().delete() # Uncomment if you want to wipe existing modules
    
    # 1. Dasar-Dasar Daur Ulang
    course_recycling = Course.objects.filter(title="Dasar-Dasar Daur Ulang").first()
    if course_recycling:
        modules_data = [
            {
                "title": "Pengenalan Sampah",
                "description": "Memahami jenis-jenis sampah dan dampaknya",
                "lessons": [
                    {"title": "Apa itu Sampah?", "type": "video", "duration": "5:30", "content": "https://www.youtube.com/watch?v=example1"},
                    {"title": "Dampak Sampah Plastik", "type": "document", "duration": "10 menit baca", "content": "Artikel tentang dampak mikroplastik."},
                    {"title": "Kuis Pemahaman Dasar", "type": "quiz", "duration": "15:00", "content": "Kuis 10 soal multiple choice."}
                ]
            },
            {
                "title": "Pemisahan Sampah",
                "description": "Cara memisahkan sampah organik dan anorganik",
                "lessons": [
                    {"title": "Kategori Sampah Rumah Tangga", "type": "video", "duration": "8:45", "content": "https://example.com/video2"},
                    {"title": "Praktik Memilah Sampah", "type": "assignment", "duration": "30:00", "content": "Tugas: Foto tempat sampah terpilah di rumah Anda."},
                ]
            },
            {
                "title": "Menyalurkan Sampah",
                "description": "Kemana sampah harus dibuang?",
                "lessons": [
                    {"title": "Mengenal Bank Sampah", "type": "video", "duration": "6:20", "content": "https://example.com/video3"},
                    {"title": "Lokasi Bank Sampah ResikPlus", "type": "document", "duration": "5 menit baca", "content": "Daftar mitra kami."}
                ]
            }
        ]
        create_modules_for_course(course_recycling, modules_data)

    # 2. Pengolahan Kompos Rumah Tangga
    course_compost = Course.objects.filter(title="Pengolahan Kompos Rumah Tangga").first()
    if course_compost:
        modules_data = [
            {
                "title": "Teori Pengomposan",
                "description": "Mengapa mengompos itu penting?",
                "lessons": [
                    {"title": "Siklus Nutrisi Alam", "type": "video", "duration": "10:00", "content": "Video animasi siklus karbon dan nitrogen."},
                    {"title": "Bahan Hijau vs Bahan Coklat", "type": "document", "duration": "15 menit baca", "content": "Tabel perbandingan rasio C:N."}
                ]
            },
            {
                "title": "Metode Takakura",
                "description": "Membuat kompos dengan keranjang Takakura",
                "lessons": [
                    {"title": "Persiapan Alat dan Bahan", "type": "video", "duration": "12:15", "content": "Tutorial membuat biang bakteri."},
                    {"title": "Perawatan Harian", "type": "video", "duration": "5:50", "content": "Cara mengaduk dan menjaga kelembaban."},
                    {"title": "Panen Kompos", "type": "assignment", "duration": "45:00", "content": "Laporan hasil panen kompos pertama."}
                ]
            }
        ]
        create_modules_for_course(course_compost, modules_data)
        
    # 3. Manajemen Bank Sampah (Lanjutan)
    course_bank = Course.objects.filter(title="Manajemen Bank Sampah").first()
    if course_bank:
        modules_data = [
            {
                "title": "Administrasi Bank Sampah",
                "description": "Pencatatan dan pembukuan",
                "lessons": [
                    {"title": "SOP Penerimaan Nasabah", "type": "document", "duration": "20 menit baca", "content": "Dokumen SOP standar."},
                    {"title": "Sistem Bagi Hasil", "type": "video", "duration": "15:30", "content": "Penjelasan model bisnis bank sampah."}
                ]
            },
            {
                "title": "Pemasaran Produk Daur Ulang",
                "description": "Menjual hasil olahan",
                "lessons": [
                    {"title": "Marketplace untuk Produk Daur Ulang", "type": "video", "duration": "20:00", "content": "Strategi digital marketing."},
                    {"title": "Studi Kasus Sukses", "type": "document", "duration": "10 menit baca", "content": "Kisah inspiratif bank sampah maju."}
                ]
            }
        ]
        create_modules_for_course(course_bank, modules_data)

def create_modules_for_course(course, modules_data):
    print(f"Creating modules for: {course.title}")
    for i, m_data in enumerate(modules_data):
        module, created = Module.objects.get_or_create(
            course=course,
            title=m_data['title'],
            defaults={
                'description': m_data.get('description', ''),
                'order': i + 1
            }
        )
        
        # Create lessons
        for j, l_data in enumerate(m_data['lessons']):
            Lesson.objects.get_or_create(
                module=module,
                title=l_data['title'],
                defaults={
                    'type': l_data.get('type', 'video'),
                    'duration': l_data.get('duration', ''),
                    'content': l_data.get('content', ''),
                    'order': j + 1
                }
            )
        print(f"  - Module '{module.title}' with {len(m_data['lessons'])} lessons processed.")

if __name__ == "__main__":
    create_dummy_modules()
