"""Program utama Sistem Manajemen Perpustakaan Sederhana.

Skrip ini mendemonstrasikan penambahan item, penampilan katalog,
pencarian berdasarkan judul atau ID, peminjaman, pengembalian, dan
perhitungan denda.
"""

from library import Library
from library_item import Book, Magazine
from member import Member


def tampilkan_judul(judul: str) -> None:
    """Mencetak judul bagian agar keluaran mudah dibaca."""
    print(f"\n{judul}")


def isi_koleksi(perpustakaan: Library) -> None:
    """Menambahkan beberapa buku dan majalah ke perpustakaan."""
    daftar_item = [
        Book(
            "BK-001",
            "Python untuk Pemula",
            2023,
            "Andi Nugraha",
            "Teknologi",
        ),
        Book(
            "BK-002",
            "Pemrograman Berorientasi Objek",
            2022,
            "Rina Wijaya",
            "Teknologi",
        ),
        Book(
            "BK-003",
            "Algoritma dan Struktur Data",
            2021,
            "Budi Santoso",
            "Informatika",
        ),
        Book(
            "BK-004",
            "Dasar-Dasar Basis Data",
            2020,
            "Siti Rahma",
            "Informatika",
        ),
        Magazine(
            "MJ-001",
            "Majalah Teknologi",
            2024,
            "Edisi 12",
            "Media Digital",
        ),
        Magazine(
            "MJ-002",
            "Majalah Ilmu Komputer",
            2023,
            "Edisi 8",
            "Campus Press",
        ),
    ]

    tampilkan_judul("1. MENAMBAHKAN ITEM KE PERPUSTAKAAN")
    for item in daftar_item:
        perpustakaan.tambah_item(item)


def main() -> None:
    """Menjalankan seluruh skenario pengujian sistem perpustakaan."""
    perpustakaan = Library("Perpustakaan ITERA")
    isi_koleksi(perpustakaan)

    tampilkan_judul("2. KATALOG ITEM PERPUSTAKAAN")
    perpustakaan.tampilkan_katalog()

    tampilkan_judul("3. PENCARIAN BERDASARKAN JUDUL DAN ID")
    perpustakaan.tampilkan_hasil_pencarian("Python")
    perpustakaan.tampilkan_hasil_pencarian("MJ-002")

    tampilkan_judul("4. PEMINJAMAN DAN STATUS KETERSEDIAAN")
    anggota = Member("MB-001", "Yabes Situmorang")
    print(f"  Anggota: {anggota}")
    perpustakaan.pinjam_item("BK-001", anggota)
    perpustakaan.pinjam_item("BK-001", anggota)

    buku = perpustakaan.cari_item_id("BK-001")
    if buku is not None:
        status = "Dipinjam" if buku.is_dipinjam else "Tersedia"
        print(f"  Status BK-001: {status}")
    print(f"  {anggota}")

    tampilkan_judul("5. PENGEMBALIAN DAN PERHITUNGAN DENDA")
    perpustakaan.kembalikan_item("BK-001", anggota, hari_terlambat=3)

    if buku is not None:
        status = "Dipinjam" if buku.is_dipinjam else "Tersedia"
        print(f"  Status BK-001: {status}")
    print(f"  {anggota}")


if __name__ == "__main__":
    main()
