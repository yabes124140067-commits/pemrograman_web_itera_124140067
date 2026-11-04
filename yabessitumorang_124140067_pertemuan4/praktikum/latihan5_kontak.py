"""Latihan Mandiri 5 - Katalog Kontak Sederhana."""

kontak = {
    "Budi Santoso": "081234567890",
    "Siti Aminah": "082345678901",
    "Andi Wijaya": "083456789012",
}


def tambah_kontak(nama: str, nomor: str) -> None:
    """Menambahkan kontak baru ke dalam dictionary.

    Parameters
    ----------
    nama : str
        Nama kontak.
    nomor : str
        Nomor telepon kontak.

    Returns
    -------
    None
        Fungsi hanya mencetak konfirmasi ke konsol.
    """
    kontak[nama] = nomor
    print(f"Kontak '{nama}' berhasil ditambahkan.")


def cari_kontak(nama: str) -> None:
    """Mencari nomor telepon berdasarkan nama menggunakan .get().

    Parameters
    ----------
    nama : str
        Nama kontak yang dicari.

    Returns
    -------
    None
        Fungsi hanya mencetak hasil pencarian ke konsol.
    """
    nomor = kontak.get(nama)
    if nomor is None:
        print(f"Kontak '{nama}' tidak ditemukan.")
    else:
        print(f"{nama}: {nomor}")


def tampilkan_semua() -> None:
    """Menampilkan seluruh kontak yang tersimpan.

    Returns
    -------
    None
        Fungsi hanya mencetak daftar kontak ke konsol.
    """
    if not kontak:
        print("Belum ada kontak tersimpan.")
        return

    print("\n=== DAFTAR KONTAK ===")
    for urutan, (nama, nomor) in enumerate(kontak.items(), start=1):
        print(f"{urutan}. {nama:<20} : {nomor}")


def main() -> None:
    """Menjalankan menu interaktif katalog kontak."""
    while True:
        print("\n=== KATALOG KONTAK ===")
        print("1. Tambah kontak")
        print("2. Cari kontak")
        print("3. Tampilkan semua kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            nama = input("Nama kontak   : ").strip()
            nomor = input("Nomor telepon : ").strip()
            if nama and nomor:
                tambah_kontak(nama, nomor)
            else:
                print("Nama dan nomor tidak boleh kosong.")
        elif pilihan == "2":
            nama = input("Nama yang dicari: ").strip()
            cari_kontak(nama)
        elif pilihan == "3":
            tampilkan_semua()
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-4.")


if __name__ == "__main__":
    main()
