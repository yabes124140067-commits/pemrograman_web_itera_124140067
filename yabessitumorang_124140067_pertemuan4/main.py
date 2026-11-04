"""Program utama penggunaan modul math_operations.

Nama  : Yabes Situmorang
NIM   : 124140067
Kelas : RB

Berkas ini mendemonstrasikan dua cara import yang berbeda:
1. import math_operations          -> akses lewat nama modul
2. from math_operations import ... -> panggil langsung
"""

import math_operations
from math_operations import PI, celsius_ke_fahrenheit, celsius_ke_kelvin


def cetak_garis(karakter: str = "=", panjang: int = 50) -> None:
    """Mencetak garis pemisah agar keluaran lebih rapi.

    Parameters
    ----------
    karakter : str, optional
        Karakter yang dipakai untuk garis (default "=").
    panjang : int, optional
        Jumlah karakter pada garis (default 50).

    Returns
    -------
    None
        Fungsi hanya mencetak ke konsol.
    """
    print(karakter * panjang)


def main() -> None:
    """Menjalankan seluruh demonstrasi fungsi modul math_operations."""
    cetak_garis()
    print("DEMO MODUL MATH_OPERATIONS".center(50))
    print(f"Konstanta PI = {PI}")
    cetak_garis()

    # --- Geometri: persegi (cara import 1) ---
    sisi = 6.0
    print("\n[1] PERSEGI (sisi = 6)")
    print(f"Luas     : {math_operations.luas_persegi(sisi):.2f}")
    print(f"Keliling : {math_operations.keliling_persegi(sisi):.2f}")

    # --- Geometri: persegi panjang (cara import 1) ---
    panjang, lebar = 10.0, 4.5
    print("\n[2] PERSEGI PANJANG (panjang = 10, lebar = 4.5)")
    print(
        "Luas     : "
        f"{math_operations.luas_persegi_panjang(panjang, lebar):.2f}"
    )
    print(
        "Keliling : "
        f"{math_operations.keliling_persegi_panjang(panjang, lebar):.2f}"
    )

    # --- Geometri: lingkaran (cara import 1) ---
    jari_jari = 7.0
    print("\n[3] LINGKARAN (jari-jari = 7)")
    print(f"Luas     : {math_operations.luas_lingkaran(jari_jari):.2f}")
    print(f"Keliling : {math_operations.keliling_lingkaran(jari_jari):.2f}")

    # --- Konversi suhu (cara import 2: from ... import ...) ---
    suhu_celsius = [0, 25, 37, 100]
    print("\n[4] KONVERSI SUHU")
    print(f"{'Celsius':>10}{'Fahrenheit':>14}{'Kelvin':>12}")
    cetak_garis("-", 36)
    for celsius in suhu_celsius:
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>10.2f}{fahrenheit:>14.2f}{kelvin:>12.2f}")

    cetak_garis()
    print("Program selesai.")


if __name__ == "__main__":
    main()
