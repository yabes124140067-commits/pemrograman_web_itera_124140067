"""Model anggota perpustakaan.

Class ``Member`` menyimpan identitas anggota dan daftar item yang sedang
dipinjam. Data identitas dilindungi dengan atribut private.
"""

from library_item import LibraryItem


class Member:
    """Anggota perpustakaan yang dapat meminjam item."""

    def __init__(self, member_id: str, nama: str):
        if not member_id.strip():
            raise ValueError("ID anggota tidak boleh kosong.")
        if not nama.strip():
            raise ValueError("Nama anggota tidak boleh kosong.")

        self.__member_id = member_id.strip().upper()
        self.__nama = nama.strip()
        self._daftar_pinjaman: list[LibraryItem] = []

    @property
    def member_id(self) -> str:
        """Mengembalikan ID unik anggota."""
        return self.__member_id

    @property
    def nama(self) -> str:
        """Mengembalikan nama anggota."""
        return self.__nama

    @property
    def daftar_pinjaman(self) -> tuple[LibraryItem, ...]:
        """Mengembalikan daftar pinjaman sebagai tuple read-only."""
        return tuple(self._daftar_pinjaman)

    @property
    def jumlah_pinjaman(self) -> int:
        """Mengembalikan jumlah item yang sedang dipinjam."""
        return len(self._daftar_pinjaman)

    def tambah_pinjaman(self, item: LibraryItem) -> None:
        """Mencatat item baru ke daftar pinjaman anggota."""
        if item not in self._daftar_pinjaman:
            self._daftar_pinjaman.append(item)

    def hapus_pinjaman(self, item: LibraryItem) -> None:
        """Menghapus item dari daftar pinjaman anggota."""
        if item in self._daftar_pinjaman:
            self._daftar_pinjaman.remove(item)

    def __str__(self) -> str:
        """Representasi ringkas data anggota."""
        return (
            f"{self.__nama} ({self.__member_id}) - "
            f"{self.jumlah_pinjaman} item dipinjam"
        )
