"""Latihan mandiri: armada truk ekspedisi kargo."""


class Kendaraan:
    """Superclass sederhana untuk latihan inheritance."""

    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def deskripsi(self) -> str:
        """Mengembalikan deskripsi dasar kendaraan."""
        return f"{self.merek} {self.model} ({self.tahun})"


class Truk(Kendaraan):
    """Truk dengan kapasitas muatan dan validasi beban."""

    def __init__(
        self,
        merek: str,
        model: str,
        tahun: int,
        kapasitas_maksimal_ton: float,
    ):
        super().__init__(merek, model, tahun)
        self.kapasitas_maksimal_ton = kapasitas_maksimal_ton
        self.muatan_saat_ini = 0.0

    def muat_barang(self, berat_ton: float) -> bool:
        """Menambah muatan jika tidak melebihi kapasitas maksimal."""
        if berat_ton <= 0:
            print("Berat muatan harus lebih dari nol.")
            return False

        if self.muatan_saat_ini + berat_ton > self.kapasitas_maksimal_ton:
            print(
                f"Muatan melebihi kapasitas! Sisa ruang: "
                f"{self.kapasitas_maksimal_ton - self.muatan_saat_ini} ton"
            )
            return False

        self.muatan_saat_ini += berat_ton
        print(
            f"Muatan {berat_ton} ton ditambahkan. Total muatan: "
            f"{self.muatan_saat_ini} ton"
        )
        return True

    def deskripsi(self) -> str:
        """Menampilkan deskripsi truk beserta beban saat ini."""
        return (
            f"{super().deskripsi()} [Truk kapasitas "
            f"{self.kapasitas_maksimal_ton} ton | Muatan: "
            f"{self.muatan_saat_ini} ton]"
        )


if __name__ == "__main__":
    truk = Truk("Hino", "Dutro", 2023, kapasitas_maksimal_ton=5.0)
    print(truk.deskripsi())
    truk.muat_barang(2.5)
    truk.muat_barang(3.0)
    truk.muat_barang(2.0)
    print(truk.deskripsi())
