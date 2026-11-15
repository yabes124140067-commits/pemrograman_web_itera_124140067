"""Latihan mandiri: pemodelan entitas sistem kasir toko.

Entitas ``Produk``, ``Keranjang``, dan ``Pengguna`` masing-masing memiliki
minimal tiga atribut data dan dua method perilaku.
"""


class Produk:
    """Produk yang dijual di toko."""

    def __init__(self, nama: str, harga: float, stok: int):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def total_nilai_stok(self) -> float:
        """Menghitung nilai seluruh stok produk."""
        return self.harga * self.stok

    def kurangi_stok(self, jumlah: int) -> bool:
        """Mengurangi stok jika jumlahnya mencukupi."""
        if jumlah <= 0 or jumlah > self.stok:
            print(f"Stok {self.nama} tidak mencukupi.")
            return False
        self.stok -= jumlah
        return True

    def __str__(self) -> str:
        """Menampilkan informasi produk."""
        return (
            f"{self.nama} | Rp {self.harga:,.0f} | Stok: {self.stok}"
        )


class Keranjang:
    """Keranjang belanja berisi daftar produk."""

    def __init__(self):
        self.__daftar_item = []

    def tambah_produk(self, produk: Produk, jumlah: int = 1) -> bool:
        """Menambahkan produk ke keranjang jika stok tersedia."""
        if not produk.kurangi_stok(jumlah):
            return False
        self.__daftar_item.append((produk, jumlah))
        print(f"{jumlah} x {produk.nama} masuk keranjang.")
        return True

    def total_belanja(self) -> float:
        """Menghitung total harga seluruh item di keranjang."""
        return sum(
            produk.harga * jumlah
            for produk, jumlah in self.__daftar_item
        )

    def __str__(self) -> str:
        """Menampilkan isi keranjang."""
        return (
            f"Keranjang: {len(self.__daftar_item)} jenis produk | "
            f"Total: Rp {self.total_belanja():,.0f}"
        )


class Pengguna:
    """Pengguna yang memiliki saldo untuk berbelanja."""

    def __init__(self, nama: str, email: str, saldo: float = 0.0):
        self.nama = nama
        self.email = email
        self.__saldo = saldo

    def top_up(self, nominal: float) -> None:
        """Menambah saldo pengguna."""
        if nominal <= 0:
            print("Nominal top up harus lebih dari nol.")
            return
        self.__saldo += nominal
        print(f"Saldo {self.nama}: Rp {self.__saldo:,.0f}")

    def bayar(self, nominal: float) -> bool:
        """Membayar tagihan jika saldo mencukupi."""
        if nominal > self.__saldo:
            print("Saldo tidak mencukupi.")
            return False
        self.__saldo -= nominal
        print(f"Pembayaran berhasil. Sisa saldo: Rp {self.__saldo:,.0f}")
        return True

    def __str__(self) -> str:
        """Menampilkan identitas pengguna."""
        return f"{self.nama} ({self.email})"


if __name__ == "__main__":
    produk = Produk("Keyboard Mekanik", 450000, 10)
    keranjang = Keranjang()
    pengguna = Pengguna("Yabes", "yabes@example.com", 1000000)

    print(produk)
    keranjang.tambah_produk(produk, 2)
    print(keranjang)
    print(pengguna)
    pengguna.bayar(keranjang.total_belanja())
