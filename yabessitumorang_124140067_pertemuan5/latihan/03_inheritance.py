"""Implementasi inheritance, super(), overriding, dan MRO.

Program memodelkan hierarki kendaraan dengan superclass ``Kendaraan``,
subclass ``Mobil`` dan ``Motor``, serta multiple inheritance pada
``MobilListrik``.
"""


class Kendaraan:
    """Superclass dasar untuk seluruh kendaraan."""

    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def deskripsi(self) -> str:
        """Mengembalikan deskripsi dasar kendaraan."""
        return f"{self.merek} {self.model} ({self.tahun})"

    def tambah_jarak(self, km: float):
        """Menambah jarak tempuh jika nilainya valid."""
        if km > 0:
            self.odometer += km
            print(
                f"[{self.merek}] Menempuh perjalanan +{km} km. "
                f"Total Odo: {self.odometer} km"
            )
        else:
            print("Nilai kilometer tambahan tidak valid!")

    def klakson(self) -> str:
        """Mengembalikan suara klakson standar."""
        return "Tin tin!"


class Mobil(Kendaraan):
    """Subclass kendaraan roda empat."""

    def __init__(
        self,
        merek: str,
        model: str,
        tahun: int,
        jumlah_pintu: int,
        kapasitas_tangki: float,
    ):
        super().__init__(merek, model, tahun)
        self.jumlah_pintu = jumlah_pintu
        self.kapasitas_tangki = kapasitas_tangki
        self.sisa_bensin = kapasitas_tangki

    def deskripsi(self) -> str:
        """Memperluas deskripsi dasar dengan informasi mobil."""
        deskripsi_dasar = super().deskripsi()
        return (
            f"{deskripsi_dasar} [Mobil {self.jumlah_pintu} Pintu, "
            f"Tangki: {self.kapasitas_tangki}L]"
        )

    def klakson(self) -> str:
        """Mengoverride klakson dengan suara khas mobil."""
        return "Telolet! Telolet! (Klakson Mobil)"

    def isi_bensin(self, liter: float):
        """Mengisi bensin tanpa melampaui kapasitas tangki."""
        if self.sisa_bensin + liter <= self.kapasitas_tangki:
            self.sisa_bensin += liter
            print(
                f"[{self.merek} {self.model}] Diisi bensin {liter}L. "
                f"Sisa bahan bakar: {self.sisa_bensin}L"
            )
        else:
            print("Kapasitas tangki bensin akan meluap!")


class Motor(Kendaraan):
    """Subclass kendaraan roda dua."""

    def __init__(
        self,
        merek: str,
        model: str,
        tahun: int,
        kapasitas_cc: int,
    ):
        super().__init__(merek, model, tahun)
        self.kapasitas_cc = kapasitas_cc

    def deskripsi(self) -> str:
        """Memperluas deskripsi dasar dengan kapasitas mesin."""
        return (
            f"{super().deskripsi()} "
            f"[Motor Sport {self.kapasitas_cc}cc]"
        )

    def klakson(self) -> str:
        """Mengoverride klakson dengan suara khas motor."""
        return "Bip bip! (Klakson Motor)"

    def wheelie(self):
        """Menampilkan aksi atraksi motor."""
        print(
            f"[{self.merek} {self.model}] Melakukan atraksi wheelie "
            "satu roda!"
        )


class KomponenBaterai:
    """Komponen baterai untuk kendaraan listrik."""

    def __init__(self, kapasitas_kwh: float):
        self.kapasitas_kwh = kapasitas_kwh
        self.daya_tersisa = 100.0

    def isi_daya(self, persen: float):
        """Menambah daya baterai maksimal sampai 100 persen."""
        self.daya_tersisa = min(100.0, self.daya_tersisa + persen)
        print(
            f"Baterai diisi ulang. Kapasitas daya: "
            f"{self.daya_tersisa}%"
        )


class MobilListrik(Mobil, KomponenBaterai):
    """Mobil listrik hasil multiple inheritance."""

    def __init__(
        self,
        merek: str,
        model: str,
        tahun: int,
        kapasitas_kwh: float,
    ):
        Mobil.__init__(
            self,
            merek,
            model,
            tahun,
            jumlah_pintu=4,
            kapasitas_tangki=0.0,
        )
        KomponenBaterai.__init__(self, kapasitas_kwh)

    def deskripsi(self) -> str:
        """Menampilkan deskripsi khusus kendaraan listrik."""
        return (
            f"{self.merek} {self.model} ({self.tahun}) "
            f"[EV Baterai {self.kapasitas_kwh} kWh, "
            f"Daya: {self.daya_tersisa}%]"
        )


if __name__ == "__main__":
    avanza = Mobil(
        "Toyota",
        "Avanza Veloz",
        2023,
        jumlah_pintu=5,
        kapasitas_tangki=45.0,
    )
    cbr = Motor("Honda", "CBR250RR", 2022, kapasitas_cc=250)
    ioniq = MobilListrik(
        "Hyundai",
        "Ioniq 5",
        2024,
        kapasitas_kwh=72.6,
    )

    print("--- Deskripsi Kendaraan ---")
    print(avanza.deskripsi())
    print(cbr.deskripsi())
    print(ioniq.deskripsi())

    print("\n--- Uji Coba Suara Klakson ---")
    print(f"{avanza.model} : {avanza.klakson()}")
    print(f"{cbr.model}    : {cbr.klakson()}")

    print("\n--- Perjalanan & Konsumsi Energi ---")
    avanza.tambah_jarak(120.5)
    avanza.isi_bensin(15)
    cbr.wheelie()
    ioniq.isi_daya(30)

    print("\n--- Pemeriksaan Relasi Pewarisan ---")
    print(
        "Apakah avanza adalah instance dari Mobil?    :",
        isinstance(avanza, Mobil),
    )
    print(
        "Apakah avanza adalah instance dari Kendaraan?:",
        isinstance(avanza, Kendaraan),
    )
    print(
        "Apakah cbr adalah instance dari Mobil?       :",
        isinstance(cbr, Mobil),
    )
    print(
        "Apakah Mobil subclass dari Kendaraan?        :",
        issubclass(Mobil, Kendaraan),
    )
    print(
        "\nMRO MobilListrik:",
        [kelas.__name__ for kelas in MobilListrik.__mro__],
    )
