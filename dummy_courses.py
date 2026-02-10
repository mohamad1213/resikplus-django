import os
import django
from decimal import Decimal

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.courses.models import Course

def create_dummy_courses():
    courses_data = [
        {
            "title": "Dasar-Dasar Daur Ulang",
            "subtitle": "Panduan lengkap untuk pemula",
            "description": "Pelajari cara memilah sampah dengan benar dan memahami proses daur ulang dasar.",
            "instructor": "Budi Santoso",
            "duration": "4 Minggu",
            "level": "Pemula",
            "price": Decimal("150000.00"),
            "type": "Online",
            "status": "Aktif",
            "students_count": 120,
            "lessons_count": 8,
            "features": ["Sertifikat", "Akses Seumur Hidup", "Forum Diskusi"]
        },
        {
            "title": "Pengolahan Kompos Rumah Tangga",
            "subtitle": "Ubah sampah organik menjadi pupuk",
            "description": "Teknik membuat kompos dari sisa makanan dan sampah organik rumah tangga.",
            "instructor": "Siti Aminah",
            "duration": "2 Minggu",
            "level": "Pemula",
            "price": Decimal("75000.00"),
            "type": "Online",
            "status": "Aktif",
            "students_count": 85,
            "lessons_count": 5,
            "features": ["Video Tutorial", "E-book Panduan"]
        },
        {
            "title": "Manajemen Bank Sampah",
            "subtitle": "Strategi mengelola bank sampah",
            "description": "Kursus tingkat lanjut untuk pengelola bank sampah agar lebih produktif dan efisien.",
            "instructor": "Rudi Hartono",
            "duration": "6 Minggu",
            "level": "Lanjutan",
            "price": Decimal("300000.00"),
            "type": "Hybrid",
            "status": "Aktif",
            "students_count": 45,
            "lessons_count": 12,
            "features": ["Sesi Live Zoom", "Studi Kasus", "Sertifikat Profesional"]
        },
        {
            "title": "Kerajinan dari Barang Bekas",
            "subtitle": "Kreativitas tanpa batas",
            "description": "Tutorial membuat kerajinan tangan bernilai jual dari barang-barang bekas.",
            "instructor": "Dewi Kreati",
            "duration": "3 Minggu",
            "level": "Menengah",
            "price": Decimal("100000.00"),
            "type": "Offline",
            "status": "Coming Soon",
            "students_count": 0,
            "lessons_count": 10,
            "features": ["Workshop Kit", "Video Tutorial"]
        },
        {
            "title": "Audit Lingkungan untuk Bisnis",
            "subtitle": "Menuju bisnis yang berkelanjutan",
            "description": "Panduan melakukan audit lingkungan sederhana untuk UMKM dan bisnis kecil.",
            "instructor": "Prof. Green",
            "duration": "5 Minggu",
            "level": "Lanjutan",
            "price": Decimal("500000.00"),
            "type": "Online",
            "status": "Draft",
            "students_count": 0,
            "lessons_count": 15,
            "features": ["Template Audit", "Konsultasi 1-on-1"]
        }
    ]

    for data in courses_data:
        course, created = Course.objects.get_or_create(
            title=data["title"],
            defaults=data
        )
        if created:
            print(f"Course created: {course.title}")
        else:
            print(f"Course already exists: {course.title}")

if __name__ == "__main__":
    create_dummy_courses()
