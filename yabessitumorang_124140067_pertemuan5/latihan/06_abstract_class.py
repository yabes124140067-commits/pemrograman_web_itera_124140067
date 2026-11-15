"""Penerapan abstract class, abstract method, dan interface pattern.

Program mendemonstrasikan class ``Shape`` dan ``DatabaseConnector`` sebagai
kontrak abstrak yang wajib diimplementasikan oleh subclass konkret.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class untuk bangun datar."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def luas(self) -> float:
        """Menghitung luas area bangun datar."""

    @abstractmethod
    def keliling(self) -> float:
        """Menghitung keliling bangun datar."""

    def cetak_laporan(self):
        """Mencetak laporan luas dan keliling secara polimorfik."""
        print(
            f"[{self.nama}] Luas: {self.luas():.2f} unit persegi | "
            f"Keliling: {self.keliling():.2f} unit"
        )


class PersegiPanjang(Shape):
    """Bangun datar persegi panjang."""

    def __init__(self, panjang: float, lebar: float):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> float:
        """Mengembalikan luas persegi panjang."""
        return self.panjang * self.lebar

    def keliling(self) -> float:
        """Mengembalikan keliling persegi panjang."""
        return 2 * (self.panjang + self.lebar)


class Lingkaran(Shape):
    """Bangun datar lingkaran."""

    def __init__(self, radius: float):
        super().__init__("Lingkaran")
        self.radius = radius

    def luas(self) -> float:
        """Mengembalikan luas lingkaran."""
        return math.pi * (self.radius ** 2)

    def keliling(self) -> float:
        """Mengembalikan keliling lingkaran."""
        return 2 * math.pi * self.radius


class DatabaseConnector(ABC):
    """Interface pattern untuk konektor database backend."""

    @property
    @abstractmethod
    def driver_name(self) -> str:
        """Nama driver database yang digunakan."""

    @abstractmethod
    def connect(self, host: str, port: int, database: str) -> bool:
        """Membuka koneksi ke database."""

    @abstractmethod
    def execute_query(self, sql: str) -> list:
        """Menjalankan query dan mengembalikan hasil."""

    @abstractmethod
    def disconnect(self):
        """Menutup koneksi database."""


class PostgreSQLConnector(DatabaseConnector):
    """Implementasi konektor PostgreSQL."""

    @property
    def driver_name(self) -> str:
        """Mengembalikan nama driver PostgreSQL."""
        return "PostgreSQL (psycopg2)"

    def connect(self, host: str, port: int, database: str) -> bool:
        """Mensimulasikan koneksi ke server PostgreSQL."""
        print(
            f"[{self.driver_name}] Terhubung ke "
            f"postgresql://{host}:{port}/{database} [OK]"
        )
        return True

    def execute_query(self, sql: str) -> list:
        """Mensimulasikan eksekusi query SELECT."""
        print(f"[{self.driver_name}] Menjalankan SQL: '{sql}'")
        return [
            {"id": 1, "nama": "Ahmad"},
            {"id": 2, "nama": "Nabila"},
        ]

    def disconnect(self):
        """Menutup koneksi database."""
        print(
            f"[{self.driver_name}] Koneksi database ditutup "
            "dengan aman."
        )


if __name__ == "__main__":
    print("--- 1. Uji Coba Kepatuhan Implementasi Shape ---")
    pp = PersegiPanjang(10, 5)
    ling = Lingkaran(7)

    pp.cetak_laporan()
    ling.cetak_laporan()

    print("\n--- 2. Pembuktian Enforcement Abstract Class ---")
    try:
        bentuk_gaib = Shape("Bentuk Abstrak")
        print(bentuk_gaib)
    except TypeError as err:
        print(f"Penolakan Python Terbukti: {err}")

    class SegitigaCacat(Shape):
        """Subclass yang sengaja lupa mengimplementasikan keliling()."""

        def __init__(self, alas, tinggi):
            super().__init__("Segitiga Cacat")
            self.alas = alas
            self.tinggi = tinggi

        def luas(self):
            """Mengimplementasikan luas segitiga saja."""
            return 0.5 * self.alas * self.tinggi

    try:
        s = SegitigaCacat(6, 8)
        print(s)
    except TypeError as err:
        print(f"Penolakan Subclass Cacat: {err}")

    print("\n--- 3. Uji Coba Interface Database Backend ---")
    db = PostgreSQLConnector()
    db.connect("localhost", 5432, "paw_praktikum_db")
    hasil = db.execute_query("SELECT id, nama FROM mahasiswa;")
    print("Hasil Query Data:", hasil)
    db.disconnect()
