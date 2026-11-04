"""Latihan Mandiri 4 - Fungsi Validator Password."""


def validasi_password(password: str) -> bool:
    """Memeriksa apakah sebuah password valid.

    Password dianggap valid jika panjangnya minimal 8 karakter dan
    mengandung setidaknya satu angka.

    Parameters
    ----------
    password : str
        Password yang akan diperiksa.

    Returns
    -------
    bool
        True jika password valid, False jika tidak.
    """
    cukup_panjang = len(password) >= 8
    ada_angka = any(karakter.isdigit() for karakter in password)
    return cukup_panjang and ada_angka


def main() -> None:
    """Menguji fungsi validasi_password dengan beberapa contoh."""
    contoh_password = [
        "rahasia123",   # valid
        "rahasia",      # tidak ada angka
        "12345678",     # tidak ada huruf, tetapi memenuhi aturan
        "abc12",        # kurang dari 8 karakter
        "P@ssw0rd!",    # valid
    ]

    print("=== UJI VALIDASI PASSWORD ===")
    print(f"{'Password':<15}{'Panjang':>8}{'Ada Angka':>11}{'Status':>14}")
    print("-" * 48)

    for password in contoh_password:
        status = "VALID" if validasi_password(password) else "TIDAK VALID"
        ada_angka = "Ya" if any(c.isdigit() for c in password) else "Tidak"
        print(f"{password:<15}{len(password):>8}{ada_angka:>11}{status:>14}")


if __name__ == "__main__":
    main()
