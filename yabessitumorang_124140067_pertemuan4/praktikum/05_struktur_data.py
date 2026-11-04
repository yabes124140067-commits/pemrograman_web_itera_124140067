"""Praktikum 5 - Struktur Data (List, Dict, Set, Tuple).

Berkas: 05_struktur_data.py
Deskripsi: Operasi lanjutan List, Comprehension, Tuple, Dict, dan Set.
"""

# ---------------------------------------------------
# 1. LIST: Operasi Manipulasi dan List Comprehension
# ---------------------------------------------------
hobi = ["Membaca", "Ngoding", "Bermain Game"]
print("--- 1. EKSPLORASI LIST ---")
hobi.append("Sepak Bola")
hobi.insert(1, "Berenang")
hobi.remove("Membaca")
item_dihapus = hobi.pop()
print(f"List setelah operasi : {hobi}")
print(f"Item yang di-pop     : {item_dihapus}")

angka_mentah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kuadrat_genap = [x ** 2 for x in angka_mentah if x % 2 == 0]
print(f"Kuadrat bilangan genap : {kuadrat_genap}")

# ---------------------------------------------------
# 2. TUPLE: Koleksi Immutable yang Aman
# ---------------------------------------------------
print("\n--- 2. EKSPLORASI TUPLE ---")
titik_koordinat = (-5.3644, 105.3175)
print(f"Latitude ITERA  : {titik_koordinat[0]}")
print(f"Longitude ITERA : {titik_koordinat[1]}")

# ---------------------------------------------------
# 3. DICTIONARY: Pemetaan Pasangan Kunci-Nilai
# ---------------------------------------------------
print("\n--- 3. EKSPLORASI DICTIONARY ---")
profil_mahasiswa = {
    "nim": "124140067",
    "nama": "Yabes Situmorang",
    "program_studi": "Teknik Informatika",
    "ipk": 3.85,
    "matkul_diambil": [
        "Pemrograman Web",
        "Struktur Data",
        "Jaringan Komputer",
    ],
}

print(f"Nama Mahasiswa : {profil_mahasiswa['nama']}")
print(f"Status Beasiswa: {profil_mahasiswa.get('beasiswa', 'Tidak Menerima')}")

profil_mahasiswa["semester"] = 5
profil_mahasiswa["ipk"] = 3.90

print("\nRincian Data Profil Mahasiswa:")
for key, value in profil_mahasiswa.items():
    print(f"  * {key.replace('_', ' ').capitalize()}: {value}")

# ---------------------------------------------------
# 4. SET: Himpunan Elemen Unik dan Operasi Matematika
# ---------------------------------------------------
print("\n--- 4. EKSPLORASI SET ---")
daftar_nim_presensi = ["IF01", "IF02", "IF01", "IF03", "IF02", "IF04"]
nim_unik = set(daftar_nim_presensi)
print(f"NIM unik yang hadir : {nim_unik}")

mahasiswa_web = {"Budi", "Siti", "Andi", "Dewi"}
mahasiswa_ai = {"Andi", "Dewi", "Rian", "Eko"}

print(f"\nMahasiswa Web : {mahasiswa_web}")
print(f"Mahasiswa AI  : {mahasiswa_ai}")
print(f"Gabungan (Union |)     : {mahasiswa_web | mahasiswa_ai}")
print(f"Irisan (Intersection &): {mahasiswa_web & mahasiswa_ai}")
print(f"Selisih (Difference -) : {mahasiswa_web - mahasiswa_ai}")
