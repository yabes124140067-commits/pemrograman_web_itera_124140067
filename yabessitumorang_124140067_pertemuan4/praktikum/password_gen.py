"""Latihan Mandiri 6 - Modul Generator Password Acak.

Berkas: password_gen.py
"""

import random
import string


def buat_password_acak(panjang: int = 8) -> str:
    """Membuat password acak dari huruf dan angka.

    Parameters
    ----------
    panjang : int, optional
        Jumlah karakter password (default 8).

    Returns
    -------
    str
        Password acak berisi huruf besar, huruf kecil, dan angka.

    Raises
    ------
    ValueError
        Jika panjang kurang dari 1.
    """
    if panjang < 1:
        raise ValueError("Panjang password harus minimal 1 karakter.")

    karakter = string.ascii_letters + string.digits
    return "".join(random.choice(karakter) for _ in range(panjang))


if __name__ == "__main__":
    print("[TEST MODUL] password_gen")
    print("Password 8 karakter :", buat_password_acak())
    print("Password 12 karakter:", buat_password_acak(12))
