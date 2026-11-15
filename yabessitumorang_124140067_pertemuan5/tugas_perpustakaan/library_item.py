"""Model item perpustakaan dengan abstract class dan inheritance.

Modul ini berisi class abstrak ``LibraryItem`` serta dua subclass konkret,
yaitu ``Book`` dan ``Magazine``.
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract base class untuk seluruh item di perpustakaan.

    Atribut ``__dipinjam`` dan ``__peminjam`` bersifat private agar status
    peminjaman hanya dapat diubah melalui method ``pinjam()`` dan
    ``kembalikan()``.
    """

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        if not item_id.strip():
            raise ValueError("ID item tidak boleh kosong.")
        if not judul.strip():
            raise ValueError("Judul item tidak boleh kosong.")
        if tahun_terbit < 0:
            raise ValueError("Tahun terbit tidak boleh negatif.")

        self._item_id = item_id.strip().upper()
        self._judul = judul.strip()
        self._tahun_terbit = tahun_terbit
        self.__dipinjam = False
        self.__peminjam: str | None = None

    @property
    def item_id(self) -> str:
        """Mengembalikan ID unik item."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Mengembalikan judul item."""
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        """Mengembalikan tahun terbit item."""
        return self._tahun_terbit

    @property
    def is_dipinjam(self) -> bool:
        """Menandakan apakah item sedang dipinjam."""
        return self.__dipinjam

    @property
    def peminjam(self) -> str | None:
        """Mengembalikan nama peminjam atau ``None`` jika tersedia."""
        return self.__peminjam

    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail item sesuai jenisnya."""

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan sesuai jenis item."""

    def pinjam(self, nama_peminjam: str) -> bool:
        """Meminjamkan item kepada anggota dengan validasi status."""
        if self.__dipinjam:
            print(
                f"  [!] '{self._judul}' sedang dipinjam oleh "
                f"{self.__peminjam}."
            )
            return False
        if not nama_peminjam.strip():
            print("  [!] Nama peminjam tidak boleh kosong.")
            return False

        self.__dipinjam = True
        self.__peminjam = nama_peminjam.strip()
        print(f"  [OK] '{self._judul}' dipinjam oleh {self.__peminjam}.")
        return True

    def kembalikan(self) -> bool:
        """Mengembalikan item dan mengosongkan data peminjam."""
        if not self.__dipinjam:
            print(f"  [!] '{self._judul}' tidak sedang dipinjam.")
            return False

        self.__dipinjam = False
        self.__peminjam = None
        return True

    def __str__(self) -> str:
        """Representasi singkat item untuk ditampilkan ke pengguna."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"[{self.item_id}] {self._judul} "
            f"({self.tahun_terbit}) - {status}"
        )


class Book(LibraryItem):
    """Item buku yang menyimpan penulis dan genre."""

    TARIF_DENDA = 1000.0

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        penulis: str,
        genre: str,
    ):
        super().__init__(item_id, judul, tahun_terbit)
        self.__penulis = penulis.strip() or "-"
        self.__genre = genre.strip() or "-"

    @property
    def penulis(self) -> str:
        """Mengembalikan nama penulis buku."""
        return self.__penulis

    @property
    def genre(self) -> str:
        """Mengembalikan genre buku."""
        return self.__genre

    def get_detail(self) -> str:
        """Menampilkan detail buku secara lengkap."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"Buku {self.item_id} | {self.judul} | Penulis: "
            f"{self.__penulis} | Genre: {self.__genre} | "
            f"Tahun: {self.tahun_terbit} | Status: {status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda buku sebesar Rp1.000 per hari."""
        if hari_terlambat < 0:
            raise ValueError("Hari terlambat tidak boleh negatif.")
        return hari_terlambat * self.TARIF_DENDA


class Magazine(LibraryItem):
    """Item majalah yang menyimpan edisi dan penerbit."""

    TARIF_DENDA = 500.0

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        edisi: str,
        penerbit: str,
    ):
        super().__init__(item_id, judul, tahun_terbit)
        self.__edisi = edisi.strip() or "-"
        self.__penerbit = penerbit.strip() or "-"

    @property
    def edisi(self) -> str:
        """Mengembalikan edisi majalah."""
        return self.__edisi

    @property
    def penerbit(self) -> str:
        """Mengembalikan nama penerbit majalah."""
        return self.__penerbit

    def get_detail(self) -> str:
        """Menampilkan detail majalah secara lengkap."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"Majalah {self.item_id} | {self.judul} | Edisi: "
            f"{self.__edisi} | Penerbit: {self.__penerbit} | "
            f"Tahun: {self.tahun_terbit} | Status: {status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda majalah sebesar Rp500 per hari."""
        if hari_terlambat < 0:
            raise ValueError("Hari terlambat tidak boleh negatif.")
        return hari_terlambat * self.TARIF_DENDA
