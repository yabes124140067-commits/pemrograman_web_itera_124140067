"""Latihan mandiri: class Buku dengan diskon dan dunder length."""


class Buku:
    """Buku dengan harga asli, diskon, dan jumlah halaman."""

    def __init__(
        self,
        judul: str,
        penulis: str,
        harga_asli: float,
        jumlah_halaman: int,
    ):
        self.judul = judul
        self.penulis = penulis
        self.harga_asli = harga_asli
        self.jumlah_halaman = jumlah_halaman

    def hitung_harga_diskon(self, persen: float) -> float:
        """Mengembalikan harga setelah potongan persen."""
        if not 0 <= persen <= 100:
            raise ValueError("Persen diskon harus 0 sampai 100.")
        return self.harga_asli * (1 - persen / 100)

    def __str__(self) -> str:
        """Mencetak kartu buku."""
        return (
            f"Judul   : {self.judul}\n"
            f"Penulis : {self.penulis}\n"
            f"Harga   : Rp {self.harga_asli:,.0f}\n"
            f"Halaman : {self.jumlah_halaman}"
        )

    def __len__(self) -> int:
        """Mengembalikan jumlah halaman saat len(buku) dipanggil."""
        return self.jumlah_halaman


if __name__ == "__main__":
    buku = Buku(
        "Python untuk Pemula",
        "Andi Nugraha",
        150000,
        320,
    )
    print(buku)
    print(f"Harga diskon 20%: Rp {buku.hitung_harga_diskon(20):,.0f}")
    print(f"Jumlah halaman: {len(buku)}")
