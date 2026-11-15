"""Latihan mandiri: enkapsulasi penggajian karyawan."""


class Karyawan:
    """Karyawan dengan gaji pokok private dan validasi UMR."""

    UPAH_MINIMUM = 3_200_000

    def __init__(self, nama: str, jabatan: str, gaji_pokok: float):
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji_pokok = 0.0
        self.gaji_pokok = gaji_pokok

    @property
    def gaji_pokok(self) -> float:
        """Mengembalikan gaji pokok karyawan."""
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nominal: float):
        """Mengatur gaji pokok dengan batas minimal UMR."""
        if not isinstance(nominal, (int, float)):
            raise TypeError("Gaji pokok harus berupa angka.")
        if nominal < self.UPAH_MINIMUM:
            raise ValueError(
                f"Gaji pokok tidak boleh di bawah UMR "
                f"Rp {self.UPAH_MINIMUM:,.0f}."
            )
        self.__gaji_pokok = float(nominal)

    def hitung_gaji_bersih(self, pajak_persen: float) -> float:
        """Menghitung gaji bersih setelah potongan pajak."""
        if not 0 <= pajak_persen <= 100:
            raise ValueError("Pajak harus berada pada rentang 0 sampai 100.")
        potongan = self.__gaji_pokok * (pajak_persen / 100)
        return self.__gaji_pokok - potongan

    def __str__(self) -> str:
        """Menampilkan identitas dan gaji pokok karyawan."""
        return (
            f"{self.nama} - {self.jabatan} | Gaji pokok: "
            f"Rp {self.__gaji_pokok:,.0f}"
        )


if __name__ == "__main__":
    karyawan = Karyawan("Yabes Situmorang", "Programmer", 5000000)
    print(karyawan)
    print(
        "Gaji bersih (pajak 10%): Rp",
        f"{karyawan.hitung_gaji_bersih(10):,.0f}",
    )

    try:
        karyawan.gaji_pokok = 2000000
    except ValueError as err:
        print(f"Validasi tertangkap: {err}")
