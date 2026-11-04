"""Praktikum 4 - Modularitas Fungsi.

Berkas: 04_fungsi.py
Deskripsi: Penerapan def, default arguments, *args, **kwargs,
return ganda, dan lambda.
"""

# 1. Fungsi dengan Default Arguments dan Docstring
def hitung_luas_persegi_panjang(panjang: float, lebar: float = 1.0) -> float:
    """Menghitung luas persegi panjang.

    Parameters
    ----------
    panjang : float
        Panjang persegi panjang.
    lebar : float, optional
        Lebar persegi panjang (default 1.0).

    Returns
    -------
    float
        Luas persegi panjang (panjang * lebar).
    """
    luas = panjang * lebar
    return luas


hasil1 = hitung_luas_persegi_panjang(10.0, 5.0)
hasil2 = hitung_luas_persegi_panjang(8.0)
print(f"Luas 1 (10 x 5) : {hasil1} satuan")
print(f"Luas 2 (8 x def): {hasil2} satuan")

# 2. Fungsi Mengembalikan Lebih dari Satu Nilai (Multiple Returns)
def hitung_statistik_dasar(daftar_angka: list):
    """Mengembalikan nilai minimum, maksimum, dan rata-rata.

    Parameters
    ----------
    daftar_angka : list
        Daftar nilai yang akan dihitung statistiknya.

    Returns
    -------
    tuple
        Tuple berisi (nilai_min, nilai_max, rata_rata).
    """
    if not daftar_angka:
        return 0, 0, 0
    nilai_min = min(daftar_angka)
    nilai_max = max(daftar_angka)
    rata_rata = sum(daftar_angka) / len(daftar_angka)
    return nilai_min, nilai_max, rata_rata


nilai_mhs = [75, 88, 92, 60, 85, 90]
minimum, maksimum, rerata = hitung_statistik_dasar(nilai_mhs)
print("\nStatistik Nilai Mahasiswa:")
print(f"- Nilai Terendah : {minimum}")
print(f"- Nilai Tertinggi: {maksimum}")
print(f"- Nilai Rata-rata: {rerata:.2f}")

# 3. Fungsi dengan Arbitrary Arguments (*args dan **kwargs)
def cetak_rekap_pesanan(meja: int, *menu_makanan, **detail_tambahan):
    """Mencetak nota pesanan.

    Parameters
    ----------
    meja : int
        Nomor meja pelanggan.
    *menu_makanan : tuple
        Daftar menu yang dipesan.
    **detail_tambahan : dict
        Informasi tambahan seperti nama pelanggan dan metode bayar.

    Returns
    -------
    None
        Fungsi hanya mencetak ke konsol.
    """
    print(f"\n--- NOTA PESANAN MEJA {meja} ---")
    print("Daftar Menu yang Dipesan:")
    for nomor, makanan in enumerate(menu_makanan, start=1):
        print(f"  {nomor}. {makanan}")

    if detail_tambahan:
        print("Informasi Tambahan:")
        for kunci, nilai in detail_tambahan.items():
            print(f"  * {kunci.capitalize()}: {nilai}")


cetak_rekap_pesanan(
    4,
    "Nasi Goreng Spesial",
    "Es Teh Manis",
    "Ayam Bakar",
    pelanggan="Budi Santoso",
    metode_bayar="QRIS",
    catatan="Tanpa cabai (tidak pedas)",
)

# 4. Fungsi Anonim (Lambda Expression)
kuadrat = lambda x: x ** 2
print(f"\nUji coba lambda kuadrat (7^2): {kuadrat(7)}")

data_mahasiswa = [
    {"nama": "Siti", "umur": 21},
    {"nama": "Andi", "umur": 19},
    {"nama": "Budi", "umur": 22},
    {"nama": "Dewi", "umur": 20},
]

mahasiswa_terurut = sorted(data_mahasiswa, key=lambda m: m["umur"])
print("\nMahasiswa terurut berdasarkan umur (termuda ke tertua):")
for mhs in mahasiswa_terurut:
    print(f"- {mhs['nama']} ({mhs['umur']} tahun)")
