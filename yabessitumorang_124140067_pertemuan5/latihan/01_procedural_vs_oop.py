"""Perbandingan pendekatan prosedural dan object-oriented.

Program menampilkan cara mengelola data mahasiswa dengan dictionary dan
fungsi terpisah, lalu membandingkannya dengan class ``Mahasiswa``.
"""

mahasiswa_proc = {
    "nama": "Budi Santoso",
    "nim": "121140001",
    "jurusan": "Teknik Informatika",
    "ipk": 3.45,
}


def cetak_profil_prosedural(mhs):
    """Menampilkan profil mahasiswa dari dictionary."""
    print(
        f"[Prosedural] {mhs['nama']} ({mhs['nim']}) - "
        f"{mhs['jurusan']} | IPK: {mhs['ipk']}"
    )


def perbarui_ipk_prosedural(mhs, ipk_baru):
    """Memperbarui IPK dengan validasi rentang 0.0 sampai 4.0."""
    if 0.0 <= ipk_baru <= 4.0:
        mhs["ipk"] = ipk_baru
    else:
        print("Nilai IPK tidak valid!")


cetak_profil_prosedural(mahasiswa_proc)
perbarui_ipk_prosedural(mahasiswa_proc, 3.75)
cetak_profil_prosedural(mahasiswa_proc)


class Mahasiswa:
    """Mahasiswa dengan data dan perilaku yang terbungkus dalam class."""

    def __init__(self, nama: str, nim: str, jurusan: str, ipk: float):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def cetak_profil(self):
        """Menampilkan profil mahasiswa."""
        print(
            f"[OOP] {self.nama} ({self.nim}) - {self.jurusan} "
            f"| IPK: {self.ipk}"
        )

    def update_ipk(self, ipk_baru: float):
        """Memperbarui IPK dengan validasi di dalam class."""
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(
                f"IPK {self.nama} berhasil diperbarui menjadi "
                f"{self.ipk}"
            )
        else:
            print(
                "Peringatan: Nilai IPK harus berada pada rentang "
                "0.0 s.d 4.0!"
            )


print("\n--- Eksekusi Paradigma OOP ---")
mhs_oop = Mahasiswa(
    "Siti Rahma",
    "121140002",
    "Teknik Informatika",
    3.80,
)
mhs_oop.cetak_profil()
mhs_oop.update_ipk(3.92)
mhs_oop.cetak_profil()
