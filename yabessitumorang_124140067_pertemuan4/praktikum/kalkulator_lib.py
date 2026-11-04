"""Modul kustom penyedia fungsi-fungsi aritmatika.

Berkas: kalkulator_lib.py
"""


def tambah(a: float, b: float) -> float:
    """Mengembalikan hasil penjumlahan a + b.

    Parameters
    ----------
    a : float
        Angka pertama.
    b : float
        Angka kedua.

    Returns
    -------
    float
        Hasil a + b.
    """
    return a + b


def kurang(a: float, b: float) -> float:
    """Mengembalikan hasil pengurangan a - b.

    Parameters
    ----------
    a : float
        Angka pertama.
    b : float
        Angka kedua.

    Returns
    -------
    float
        Hasil a - b.
    """
    return a - b


def kali(a: float, b: float) -> float:
    """Mengembalikan hasil perkalian a * b.

    Parameters
    ----------
    a : float
        Angka pertama.
    b : float
        Angka kedua.

    Returns
    -------
    float
        Hasil a * b.
    """
    return a * b


def bagi(a: float, b: float):
    """Mengembalikan hasil pembagian a / b.

    Parameters
    ----------
    a : float
        Angka pembilang.
    b : float
        Angka penyebut.

    Returns
    -------
    float or str
        Hasil pembagian, atau pesan error jika b bernilai 0.
    """
    if b == 0:
        return "Error: Tidak dapat membagi dengan angka nol!"
    return a / b


if __name__ == "__main__":
    print("[TEST MODUL] Menjalankan uji coba internal kalkulator_lib:")
    print("Test 10 + 5 =", tambah(10, 5))
    print("Test 10 / 0 =", bagi(10, 0))
