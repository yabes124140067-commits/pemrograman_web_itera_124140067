"""Pengelola koleksi dan transaksi perpustakaan.

Class ``Library`` menyimpan koleksi item di atribut private ``__koleksi``
dan menyediakan operasi tambah, tampil, cari, pinjam, serta kembali.
"""

from library_item import LibraryItem
from member import Member


class Library:
    """Menyimpan dan mengelola seluruh item perpustakaan."""

    def __init__(self, nama: str = "Perpustakaan ITERA"):
        if not nama.strip():
            raise ValueError("Nama perpustakaan tidak boleh kosong.")
        self.nama = nama.strip()
        self.__koleksi: list[LibraryItem] = []

    @property
    def koleksi(self) -> tuple[LibraryItem, ...]:
        """Mengembalikan koleksi sebagai tuple read-only."""
        return tuple(self.__koleksi)

    @property
    def jumlah_koleksi(self) -> int:
        """Mengembalikan jumlah item dalam koleksi."""
        return len(self.__koleksi)

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item baru dengan validasi tipe dan ID unik."""
        if not isinstance(item, LibraryItem):
            print("  [!] Item harus berupa LibraryItem.")
            return False

        if any(item.item_id == lama.item_id for lama in self.__koleksi):
            print(f"  [!] ID {item.item_id} sudah digunakan.")
            return False

        self.__koleksi.append(item)
        print(f"  [OK] Item '{item.judul}' ditambahkan.")
        return True

    def tampilkan_katalog(self) -> None:
        """Menampilkan seluruh item beserta status ketersediaannya."""
        print(f"\n{'=' * 78}")
        print(f"KATALOG {self.nama.upper()} ({self.jumlah_koleksi} ITEM)")
        print("=" * 78)
        print(f"{'No':<4}{'ID':<9}{'Judul':<31}{'Tahun':<7}{'Status':<12}")
        print("-" * 78)

        for nomor, item in enumerate(self.__koleksi, start=1):
            if len(item.judul) > 28:
                judul = item.judul[:25] + "..."
            else:
                judul = item.judul
            status = "Dipinjam" if item.is_dipinjam else "Tersedia"
            print(
                f"{nomor:<4}{item.item_id:<9}{judul:<31}"
                f"{item.tahun_terbit:<7}{status:<12}"
            )

        print("-" * 78)
        tersedia = sum(
            1 for item in self.__koleksi if not item.is_dipinjam
        )
        print(
            f"Tersedia: {tersedia} item | "
            f"Dipinjam: {self.jumlah_koleksi - tersedia} item"
        )

    def cari_item(self, kata_kunci: str) -> list[LibraryItem]:
        """Mencari item berdasarkan ID atau potongan judul."""
        kunci = kata_kunci.strip().lower()
        if not kunci:
            return []

        return [
            item
            for item in self.__koleksi
            if kunci in item.item_id.lower()
            or kunci in item.judul.lower()
        ]

    def cari_item_id(self, item_id: str) -> LibraryItem | None:
        """Mencari satu item berdasarkan ID secara persis."""
        kunci = item_id.strip().upper()
        for item in self.__koleksi:
            if item.item_id == kunci:
                return item
        return None

    def tampilkan_hasil_pencarian(self, kata_kunci: str) -> None:
        """Menampilkan hasil pencarian dengan detail polimorfik."""
        hasil = self.cari_item(kata_kunci)
        print(f"\nPencarian '{kata_kunci}' -> {len(hasil)} item ditemukan")
        if not hasil:
            print("  Tidak ada item yang cocok.")
            return

        for item in hasil:
            print(f"  {item.get_detail()}")

    def pinjam_item(self, item_id: str, member: Member) -> bool:
        """Meminjamkan item kepada anggota jika item tersedia."""
        item = self.cari_item_id(item_id)
        if item is None:
            print(f"  [!] Item dengan ID {item_id} tidak ditemukan.")
            return False
        if not isinstance(member, Member):
            print("  [!] Peminjam harus berupa Member.")
            return False

        if item.pinjam(member.nama):
            member.tambah_pinjaman(item)
            return True
        return False

    def kembalikan_item(
        self,
        item_id: str,
        member: Member,
        hari_terlambat: int = 0,
    ) -> float:
        """Mengembalikan item dan menghitung denda keterlambatan."""
        item = self.cari_item_id(item_id)
        if item is None:
            print(f"  [!] Item dengan ID {item_id} tidak ditemukan.")
            return 0.0
        if not isinstance(member, Member):
            print("  [!] Pengembali harus berupa Member.")
            return 0.0
        if item.peminjam != member.nama:
            print(
                f"  [!] '{item.judul}' tidak dipinjam oleh "
                f"{member.nama}."
            )
            return 0.0
        if hari_terlambat < 0:
            print("  [!] Hari terlambat tidak boleh negatif.")
            return 0.0

        item.kembalikan()
        member.hapus_pinjaman(item)
        denda = item.hitung_denda(hari_terlambat)
        print(f"  [OK] '{item.judul}' dikembalikan oleh {member.nama}.")
        print(
            f"       Terlambat {hari_terlambat} hari | "
            f"Denda: Rp {denda:,.0f}"
        )
        return denda
