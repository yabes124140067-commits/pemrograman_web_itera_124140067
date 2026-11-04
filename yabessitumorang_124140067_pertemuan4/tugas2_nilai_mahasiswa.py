"""Program pengelolaan data nilai mahasiswa.

Nama  : Yabes Situmorang
NIM   : 124140067
Kelas : RB

Program menyimpan data 5 mahasiswa dalam list of dictionary, menghitung
nilai akhir, menentukan grade A-E, mencetak tabel, lalu menampilkan
mahasiswa dengan nilai akhir tertinggi dan terendah.
"""

BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

data_mahasiswa = [
    {
        "nama": "Fajar Nugroho",
        "nim": "124140011",
        "nilai_uts": 88.0,
        "nilai_uas": 90.0,
        "nilai_tugas": 92.0,
    },
    {
        "nama": "Gita Permata",
        "nim": "124140012",
        "nilai_uts": 75.0,
        "nilai_uas": 78.0,
        "nilai_tugas": 80.0,
    },
    {
        "nama": "Hendra Saputra",
        "nim": "124140013",
        "nilai_uts": 62.0,
        "nilai_uas": 65.0,
        "nilai_tugas": 70.0,
    },
    {
        "nama": "Intan Maharani",
        "nim": "124140014",
        "nilai_uts": 52.0,
        "nilai_uas": 55.0,
        "nilai_tugas": 58.0,
    },
    {
        "nama": "Joko Susilo",
        "nim": "124140015",
        "nilai_uts": 40.0,
        "nilai_uas": 45.0,
        "nilai_tugas": 48.0,
    },
]


def hitung_nilai_akhir(mahasiswa: dict) -> float:
    """Menghitung nilai akhir seorang mahasiswa.

    Parameters
    ----------
    mahasiswa : dict
        Dictionary berisi kunci nilai_uts, nilai_uas, dan nilai_tugas.

    Returns
    -------
    float
        Nilai akhir = 30% UTS + 40% UAS + 30% Tugas.
    """
    return (
        BOBOT_UTS * mahasiswa["nilai_uts"]
        + BOBOT_UAS * mahasiswa["nilai_uas"]
        + BOBOT_TUGAS * mahasiswa["nilai_tugas"]
    )


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade berdasarkan nilai akhir.

    Parameters
    ----------
    nilai_akhir : float
        Nilai akhir mahasiswa.

    Returns
    -------
    str
        Grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 60:
        return "C"
    if nilai_akhir >= 50:
        return "D"
    return "E"


def olah_data(data: list) -> list:
    """Menambahkan nilai akhir dan grade ke setiap data mahasiswa.

    Parameters
    ----------
    data : list
        List of dictionary data mahasiswa.

    Returns
    -------
    list
        List baru yang sudah memiliki kunci nilai_akhir dan grade.
    """
    hasil = []
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa)
        hasil.append(
            {
                **mahasiswa,
                "nilai_akhir": nilai_akhir,
                "grade": tentukan_grade(nilai_akhir),
            }
        )
    return hasil


def buat_tabel(data: list) -> str:
    """Membuat tabel data mahasiswa dalam bentuk string.

    Parameters
    ----------
    data : list
        List data mahasiswa yang sudah memiliki nilai_akhir dan grade.

    Returns
    -------
    str
        Tabel siap cetak dengan perataan f-string.
    """
    garis = "-" * 78
    baris = [
        garis,
        f"{'No':<4}{'Nama':<22}{'NIM':<13}{'UTS':>6}{'UAS':>6}"
        f"{'Tugas':>7}{'Akhir':>8}{'Grade':>7}",
        garis,
    ]

    for nomor, mahasiswa in enumerate(data, start=1):
        baris.append(
            f"{nomor:<4}{mahasiswa['nama']:<22}{mahasiswa['nim']:<13}"
            f"{mahasiswa['nilai_uts']:>6.1f}{mahasiswa['nilai_uas']:>6.1f}"
            f"{mahasiswa['nilai_tugas']:>7.1f}{mahasiswa['nilai_akhir']:>8.2f}"
            f"{mahasiswa['grade']:>7}"
        )

    baris.append(garis)
    return "\n".join(baris)


def cari_nilai_tertinggi(data: list) -> list:
    """Mencari semua mahasiswa dengan nilai akhir tertinggi.

    Parameters
    ----------
    data : list
        List data mahasiswa yang sudah memiliki nilai_akhir.

    Returns
    -------
    list
        Daftar mahasiswa dengan nilai akhir tertinggi (bisa lebih dari satu).
    """
    nilai_tertinggi = max(mahasiswa["nilai_akhir"] for mahasiswa in data)
    return [
        mahasiswa
        for mahasiswa in data
        if mahasiswa["nilai_akhir"] == nilai_tertinggi
    ]


def cari_nilai_terendah(data: list) -> list:
    """Mencari semua mahasiswa dengan nilai akhir terendah.

    Parameters
    ----------
    data : list
        List data mahasiswa yang sudah memiliki nilai_akhir.

    Returns
    -------
    list
        Daftar mahasiswa dengan nilai akhir terendah (bisa lebih dari satu).
    """
    nilai_terendah = min(mahasiswa["nilai_akhir"] for mahasiswa in data)
    return [
        mahasiswa
        for mahasiswa in data
        if mahasiswa["nilai_akhir"] == nilai_terendah
    ]


def tampilkan_ekstrem(judul: str, daftar: list) -> None:
    """Menampilkan daftar mahasiswa pada nilai ekstrem tertentu.

    Parameters
    ----------
    judul : str
        Judul bagian yang akan dicetak.
    daftar : list
        Daftar mahasiswa hasil pencarian nilai tertinggi/terendah.

    Returns
    -------
    None
        Fungsi hanya mencetak ke konsol.
    """
    print(f"\n{judul}")
    for mahasiswa in daftar:
        print(
            f"  - {mahasiswa['nama']} ({mahasiswa['nim']}) "
            f"dengan nilai akhir {mahasiswa['nilai_akhir']:.2f} "
            f"(Grade {mahasiswa['grade']})"
        )


def main() -> None:
    """Menjalankan alur utama program pengelolaan nilai mahasiswa."""
    data_lengkap = olah_data(data_mahasiswa)

    print("=" * 78)
    print("DATA NILAI MAHASISWA".center(78))
    print("=" * 78)
    print(buat_tabel(data_lengkap))

    total_nilai = sum(mhs["nilai_akhir"] for mhs in data_lengkap)
    rata_rata = total_nilai / len(data_lengkap)
    print(f"Rata-rata nilai akhir kelas: {rata_rata:.2f}")

    tampilkan_ekstrem(
        "Mahasiswa dengan nilai akhir TERTINGGI:",
        cari_nilai_tertinggi(data_lengkap),
    )
    tampilkan_ekstrem(
        "Mahasiswa dengan nilai akhir TERENDAH:",
        cari_nilai_terendah(data_lengkap),
    )


if __name__ == "__main__":
    main()
