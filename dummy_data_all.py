import os
import django
import random
from decimal import Decimal
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.partners.models import Partner
from apps.products.models import Product
from apps.articles.models import Article

def create_dummy_partners():
    print("Creating dummy partners...")
    partners_data = [
        {
            "name": "Bank Sampah Sejahtera",
            "type": "Pengumpul",
            "location": "Jakarta Selatan",
            "status": "Aktif",
            "phone": "081234567890",
            "email": "info@bssejahtera.com",
            "address": "Jl. Fatmawati No. 10",
            "contact_person": "Budi Santoso",
            "description": "Menerima sampah plastik dan kertas."
        },
        {
            "name": "CV. Daur Ulang Jaya",
            "type": "Pengolah",
            "location": "Bekasi",
            "status": "Aktif",
            "phone": "081987654321",
            "email": "contact@dujaya.com",
            "address": "Kawasan Industri Jababeka",
            "contact_person": "Siti Aminah",
            "description": "Pengolah limbah plastik menjadi bijih plastik."
        },
        {
            "name": "Bank Sampah Mandiri",
            "type": "Pengumpul",
            "location": "Depok",
            "status": "Pending",
            "phone": "085678901234",
            "email": "bsmandiri@gmail.com",
            "address": "Jl. Margonda Raya",
            "contact_person": "Rudi Hartono",
            "description": "Fokus pada sampah elektronik."
        },
        {
            "name": "PT. Green Solution",
            "type": "Pengolah",
            "location": "Tangerang",
            "status": "Aktif",
            "phone": "02155556666",
            "email": "info@greensolution.id",
            "address": "Jl. Daan Mogot KM 19",
            "contact_person": "Dewi Sartika",
            "description": "Solusi pengolahan limbah B3."
        },
        {
            "name": "Koperasi Warga Peduli",
            "type": "Pengumpul",
            "location": "Bogor",
            "status": "Aktif",
            "phone": "081345678901",
            "email": "koperasiwp@yahoo.com",
            "address": "Jl. Raya Pajajaran",
            "contact_person": "Ahmad Yani",
            "description": "Mengumpulkan sampah organik untuk kompos."
        },
        {
            "name": "UD. Plastik Makmur",
            "type": "Pengolah",
            "location": "Jakarta Timur",
            "status": "Nonaktif",
            "phone": "087788990011",
            "email": "udpm@gmail.com",
            "address": "Kawasan Pulogadung",
            "contact_person": "Joko Widodo",
            "description": "Daur ulang botol plastik PET."
        },
        {
            "name": "Bank Sampah Berkah",
            "type": "Pengumpul",
            "location": "Jakarta Barat",
            "status": "Aktif",
            "phone": "085233445566",
            "email": "bsberkah@outlook.com",
            "address": "Jl. Panjang No. 5",
            "contact_person": "Rina Nose",
            "description": "Menerima minyak jelantah."
        }
    ]

    for data in partners_data:
        Partner.objects.get_or_create(name=data['name'], defaults=data)
        print(f"  - Partner '{data['name']}' processed.")


def create_dummy_products():
    print("\nCreating dummy products...")
    products_data = [
        {
            "name": "Mesin Pencacah Plastik",
            "category": "Mesin",
            "price": Decimal("15000000.00"),
            "description": "Mesin pencacah plastik kapasitas 50kg/jam. Cocok untuk UMKM.",
            "stock_quantity": 5,
            "sku": "MCH-001",
            "weight": "150 kg",
            "specs": ["Kapasitas: 50kg/jam", "Daya: 5HP", "Dimensi: 120x60x100 cm"]
        },
        {
            "name": "Tong Sampah Pilah 3 Warna",
            "category": "Alat",
            "price": Decimal("750000.00"),
            "description": "Set tong sampah organik, anorganik, dan B3.",
            "stock_quantity": 50,
            "sku": "BIN-003",
            "weight": "5 kg",
            "specs": ["Material: Fiber", "Kapasitas: 60L per tong"]
        },
        {
            "name": "Tas Belanja Daur Ulang",
            "category": "Produk",
            "price": Decimal("25000.00"),
            "description": "Tas belanja kuat dan modis dari kemasan plastik daur ulang.",
            "stock_quantity": 200,
            "sku": "BAG-001",
            "weight": "100 g",
            "specs": ["Material: Plastik Kemasan", "Ukuran: 40x35 cm"]
        },
        {
            "name": "Komposter Rumahan",
            "category": "Alat",
            "price": Decimal("350000.00"),
            "description": "Alat pembuat kompos praktis untuk skala rumah tangga.",
            "stock_quantity": 30,
            "sku": "CMP-001",
            "weight": "3 kg",
            "specs": ["Kapasitas: 20L", "Material: Plastik HDPE"]
        },
         {
            "name": "Bijih Plastik PP Hitam",
            "category": "Bahan Baku",
            "price": Decimal("12000.00"),
            "description": "Bijih plastik PP daur ulang kualitas super.",
            "stock_quantity": 5000,
            "sku": "RAW-001",
            "weight": "1 kg (min order)",
            "specs": ["Jenis: PP", "Warna: Hitam", "MFI: 10"]
        },
        {
            "name": "Sarung Tangan Safety",
            "category": "Aksesoris",
            "price": Decimal("15000.00"),
            "description": "Melindungi tangan saat memilah sampah.",
            "stock_quantity": 100,
            "sku": "ACC-001",
            "weight": "200 g",
            "specs": ["Material: Kain Katun Tebal", "Ukuran: All Size"]
        },
        {
            "name": "Bioaktivator Kompos",
            "category": "Lainnya",
            "price": Decimal("30000.00"),
            "description": "Cairan pemercepat proses pengomposan.",
            "stock_quantity": 150,
            "sku": "OTH-001",
            "weight": "1 L",
            "specs": ["Isi: 1 Liter", "Kandungan: EM4"]
        }
    ]

    for data in products_data:
        Product.objects.get_or_create(name=data['name'], defaults=data)
        print(f"  - Product '{data['name']}' processed.")

def create_dummy_articles():
    print("\nCreating dummy articles...")
    articles_data = [
        {
            "title": "5 Cara Mudah Memulai Zero Waste di Rumah",
            "content": "Zero waste bukan berarti tidak menghasilkan sampah sama sekali, tapi meminimalkan sampah yang kita kirim ke TPA. Mulai dari langkah kecil seperti membawa botol minum sendiri...",
            "excerpt": "Tips praktis untuk mengurangi sampah rumah tangga sehari-hari.",
            "category": "Tips & Trik",
            "author": "Admin ResikPlus",
            "status": "Published",
            "tags": ["zero waste", "tips", "gaya hidup"]
        },
        {
            "title": "Bahaya Mikroplastik bagi Kesehatan",
            "content": "Mikroplastik kini ditemukan di mana-mana, mulai dari air minum hingga makanan laut. Apa dampaknya bagi tubuh manusia dalam jangka panjang?",
            "excerpt": "Menelusuri dampak partikel plastik kecil terhadap tubuh kita.",
            "category": "Edukasi",
            "author": "Dr. Lingkungan",
            "status": "Published",
            "tags": ["kesehatan", "plastik", "lingkungan"]
        },
        {
            "title": "Mengenal Jenis-Jenis Plastik dan Kode Daur Ulangnya",
            "content": "Tidak semua plastik sama. Ada 7 kode daur ulang plastik yang perlu Anda ketahui agar tidak salah memilah. PET, HDPE, PVC, LDPE, PP, PS, dan lainnya.",
            "excerpt": "Panduan lengkap memahami simbol segitiga pada kemasan plastik.",
            "category": "Edukasi",
            "author": "Tim Ahli",
            "status": "Published",
            "tags": ["daur ulang", "plastik", "edukasi"]
        },
        {
            "title": "Sukses Mengelola Bank Sampah Kampung",
            "content": "Kisah inspiratif dari Kampung Berseri yang berhasil mengubah sampah menjadi emas melalui pengelolaan bank sampah yang profesional dan transparan.",
            "excerpt": "Studi kasus keberhasilan bank sampah tingkat RW.",
            "category": "Inspirasi",
            "author": "Jurnalis Hijau",
            "status": "Published",
            "tags": ["bank sampah", "inspirasi", "komunitas"]
        },
        {
            "title": "Cara Membuat Eco-Enzyme dari Kulit Buah",
            "content": "Jangan buang kulit buah Anda! Ubah menjadi cairan serbaguna Eco-Enzyme yang bisa digunakan untuk pembersih lantai, pupuk, dan desinfektan alami.",
            "excerpt": "Tutorial langkah demi langkah membuat cairan ajaib fermentasi.",
            "category": "DIY",
            "author": "Admin ResikPlus",
            "status": "Published",
            "tags": ["diy", "organik", "eco-enzyme"]
        },
        {
            "title": "Regulasi Terbaru Pengelolaan Sampah 2026",
            "content": "Pemerintah baru saja menerbitkan peraturan baru terkait tanggung jawab produsen atas kemasan produk mereka. Simak poin-poin pentingnya di sini.",
            "excerpt": "Update peraturan pemerintah terkait lingkungan hidup.",
            "category": "Berita",
            "author": "Tim Legal",
            "status": "Draft",
            "tags": ["hukum", "peraturan", "pemerintah"]
        },
        {
            "title": "Workshop Daur Ulang Kertas Bekas",
            "content": "Ikuti workshop seru mengubah kertas bekas menjadi kertas daur ulang estetik yang bisa dijual kembali. Daftarkan diri Anda segera!",
            "excerpt": "Jadwal dan info pendaftaran workshop daur ulang kertas.",
            "category": "Event",
            "author": "Event Organizer",
            "status": "Scheduled",
            "tags": ["event", "workshop", "kertas"]
        }
    ]

    for data in articles_data:
        # Check if exists by title to avoid slug conflict errors on re-run (though slug logic handles it, creating duplicates is messy)
        if not Article.objects.filter(title=data['title']).exists():
            Article.objects.create(**data)
            print(f"  - Article '{data['title']}' created.")
        else:
             print(f"  - Article '{data['title']}' already exists.")

if __name__ == "__main__":
    create_dummy_partners()
    create_dummy_products()
    create_dummy_articles()
