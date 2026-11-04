"""Latihan Mandiri 6 - Program penguji modul password_gen.

Berkas: main.py (berada di folder praktikum agar tidak bentrok
dengan main.py tugas 3 di folder utama).
"""

import password_gen
from password_gen import buat_password_acak


def main() -> None:
    """Menampilkan contoh password acak dengan beberapa panjang."""
    print("=== GENERATOR PASSWORD ACAK ===")

    for panjang in (8, 12, 16):
        password = buat_password_acak(panjang)
        print(f"Panjang {panjang:>2} karakter: {password}")

    print("\nUji lewat nama modul:", password_gen.buat_password_acak(10))


if __name__ == "__main__":
    main()
