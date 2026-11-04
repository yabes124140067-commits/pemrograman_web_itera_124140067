"""Praktikum 6 - Modul & Package Python.

Berkas: 06_modul_app.py
Deskripsi: Menggunakan modul standar (math, random, datetime)
dan modul kustom kalkulator_lib.
"""

import math
import random
from datetime import datetime

import kalkulator_lib as calc

print("--- 1. EKSPLORASI STANDARD LIBRARY ---")
sisi_a, sisi_b = 6, 8
sisi_miring = math.hypot(sisi_a, sisi_b)
print(
    f"Segitiga {sisi_a} dan {sisi_b} -> "
    f"Sisi miring (hypotenuse): {sisi_miring}"
)

dadu = random.randint(1, 6)
pemenang = random.choice(["Budi", "Siti", "Andi", "Dewi"])
print(f"Hasil lempar dadu acak (1-6): {dadu}")
print(f"Pemenang giveaway terpilih : {pemenang}")

waktu_sekarang = datetime.now()
print(
    "Waktu eksekusi program     : "
    f"{waktu_sekarang.strftime('%d %B %Y, pukul %H:%M:%S')}"
)

print("\n--- 2. PENGGUNAAN MODUL KUSTOM (kalkulator_lib) ---")
angka1 = 20
angka2 = 4

print(f"Operasi {angka1} + {angka2} = {calc.tambah(angka1, angka2)}")
print(f"Operasi {angka1} - {angka2} = {calc.kurang(angka1, angka2)}")
print(f"Operasi {angka1} * {angka2} = {calc.kali(angka1, angka2)}")
print(f"Operasi {angka1} / {angka2} = {calc.bagi(angka1, angka2)}")
print(f"Uji coba pembagian nol     : {calc.bagi(angka1, 0)}")
