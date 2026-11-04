"""Modul matematika untuk menghitung geometri dan konversi suhu.

Nama  : Yabes Situmorang
NIM   : 124140067
Kelas : RB

Modul ini menyediakan fungsi luas dan keliling untuk persegi, persegi
panjang, dan lingkaran, serta konversi Celsius ke Fahrenheit dan Kelvin.
"""

PI = 3.14159


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Parameters
    ----------
    sisi : float
        Panjang sisi persegi.

    Returns
    -------
    float
        Luas persegi (sisi * sisi).
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Parameters
    ----------
    sisi : float
        Panjang sisi persegi.

    Returns
    -------
    float
        Keliling persegi (4 * sisi).
    """
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Parameters
    ----------
    panjang : float
        Panjang persegi panjang.
    lebar : float
        Lebar persegi panjang.

    Returns
    -------
    float
        Luas persegi panjang (panjang * lebar).
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Parameters
    ----------
    panjang : float
        Panjang persegi panjang.
    lebar : float
        Lebar persegi panjang.

    Returns
    -------
    float
        Keliling persegi panjang (2 * (panjang + lebar)).
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Parameters
    ----------
    jari_jari : float
        Jari-jari lingkaran.

    Returns
    -------
    float
        Luas lingkaran (PI * jari_jari ** 2).
    """
    return PI * jari_jari * jari_jari


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran.

    Parameters
    ----------
    jari_jari : float
        Jari-jari lingkaran.

    Returns
    -------
    float
        Keliling lingkaran (2 * PI * jari_jari).
    """
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Parameters
    ----------
    celsius : float
        Suhu dalam derajat Celsius.

    Returns
    -------
    float
        Suhu dalam derajat Fahrenheit (C * 9/5 + 32).
    """
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin.

    Parameters
    ----------
    celsius : float
        Suhu dalam derajat Celsius.

    Returns
    -------
    float
        Suhu dalam Kelvin (C + 273.15).
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("[TEST MODUL] math_operations")
    print(f"Luas persegi (sisi 4)          : {luas_persegi(4)}")
    print(f"Keliling persegi (sisi 4)      : {keliling_persegi(4)}")
    print(f"Luas persegi panjang (8 x 5)   : {luas_persegi_panjang(8, 5)}")
    print(f"Keliling persegi panjang (8x5) : {keliling_persegi_panjang(8, 5)}")
    print(f"Luas lingkaran (r 7)           : {luas_lingkaran(7):.2f}")
    print(f"Keliling lingkaran (r 7)       : {keliling_lingkaran(7):.2f}")
    print(f"25 Celsius ke Fahrenheit       : {celsius_ke_fahrenheit(25):.2f}")
    print(f"25 Celsius ke Kelvin           : {celsius_ke_kelvin(25):.2f}")
