"""Latihan Mandiri 3 - Game Tebak Angka Rahasia Sederhana."""

angka_rahasia = 7
jumlah_percobaan = 0

print("=== GAME TEBAK ANGKA (1 - 10) ===")
print("Tebak angka rahasia. Ketik 'keluar' untuk berhenti.")

while True:
    masukan = input("Masukkan tebakan: ").strip()

    if masukan.lower() == "keluar":
        print("Permainan dihentikan.")
        break

    try:
        tebakan = int(masukan)
    except ValueError:
        print("Masukkan angka bulat, ya!")
        continue

    jumlah_percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(
            f"Selamat, tebakan benar! "
            f"Anda menebak dalam {jumlah_percobaan} percobaan."
        )
        break
