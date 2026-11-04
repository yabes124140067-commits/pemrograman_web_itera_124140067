"""Program penghitung Body Mass Index (BMI) sederhana.

Nama  : Yabes Situmorang
NIM   : 124140067
Kelas : RB

Program meminta berat badan (kg) dan tinggi badan (m) dari pengguna,
lalu menghitung BMI dan menampilkan kategorinya.
"""


def hitung_bmi(berat_kg: float, tinggi_m: float) -> float:
    """Menghitung nilai BMI.

    Parameters
    ----------
    berat_kg : float
        Berat badan dalam kilogram.
    tinggi_m : float
        Tinggi badan dalam meter.

    Returns
    -------
    float
        Nilai BMI dengan rumus berat / (tinggi * tinggi).
    """
    return berat_kg / (tinggi_m * tinggi_m)


def tentukan_kategori(bmi: float) -> str:
    """Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameters
    ----------
    bmi : float
        Nilai BMI yang sudah dihitung.

    Returns
    -------
    str
        Kategori berat badan sesuai ketentuan praktikum.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    if bmi < 25:
        return "Berat badan normal"
    if bmi < 30:
        return "Berat badan berlebih"
    return "Obesitas"


def baca_angka(prompt: str) -> float:
    """Membaca input angka positif dari pengguna dengan validasi.

    Parameters
    ----------
    prompt : str
        Teks yang ditampilkan sebelum pengguna mengetik.

    Returns
    -------
    float
        Angka positif yang valid.
    """
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("Input tidak valid. Masukkan angka, contoh: 65.5")
            continue

        if nilai <= 0:
            print("Nilai harus lebih besar dari 0.")
            continue

        return nilai


def main() -> None:
    """Menjalankan alur utama program penghitung BMI."""
    print("=" * 42)
    print("PROGRAM PENGHITUNG BMI".center(42))
    print("=" * 42)

    berat = baca_angka("Masukkan berat badan (kg) : ")
    tinggi = baca_angka("Masukkan tinggi badan (m) : ")

    bmi = hitung_bmi(berat, tinggi)
    kategori = tentukan_kategori(bmi)

    print("-" * 42)
    print(f"Berat badan  : {berat:.2f} kg")
    print(f"Tinggi badan : {tinggi:.2f} m")
    print(f"Nilai BMI    : {bmi:.2f}")
    print(f"Kategori     : {kategori}")
    print("=" * 42)


if __name__ == "__main__":
    main()
