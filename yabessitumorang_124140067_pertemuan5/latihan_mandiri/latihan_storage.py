"""Latihan mandiri: interface file storage service."""

from abc import ABC, abstractmethod


class FileStorage(ABC):
    """Kontrak abstrak untuk layanan penyimpanan berkas."""

    @abstractmethod
    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Mengunggah berkas ke penyimpanan."""

    @abstractmethod
    def download_file(self, nama_file: str) -> bytes | None:
        """Mengunduh berkas dari penyimpanan."""


class LocalDiskStorage(FileStorage):
    """Simulasi penyimpanan berkas pada disk lokal."""

    def __init__(self, folder: str = "local_storage"):
        self.folder = folder
        self.__files: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Menyimpan berkas ke folder lokal virtual."""
        self.__files[nama_file] = data_bytes
        print(
            f"[LOCAL] {nama_file} disimpan di folder {self.folder} "
            f"({len(data_bytes)} byte)."
        )
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        """Mengambil berkas dari folder lokal virtual."""
        data = self.__files.get(nama_file)
        if data is None:
            print(f"[LOCAL] Berkas {nama_file} tidak ditemukan.")
        return data


class CloudStorage(FileStorage):
    """Simulasi penyimpanan berkas pada server cloud."""

    def __init__(self, bucket: str):
        self.bucket = bucket
        self.__files: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Menyimpan berkas ke bucket cloud virtual."""
        self.__files[nama_file] = data_bytes
        print(
            f"[CLOUD] {nama_file} diunggah ke bucket {self.bucket} "
            f"({len(data_bytes)} byte)."
        )
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        """Mengambil berkas dari bucket cloud virtual."""
        data = self.__files.get(nama_file)
        if data is None:
            print(f"[CLOUD] Berkas {nama_file} tidak ditemukan.")
        return data


if __name__ == "__main__":
    local = LocalDiskStorage("data_lokal")
    cloud = CloudStorage("paw-storage")

    for storage in (local, cloud):
        storage.upload_file("catatan.txt", b"Belajar OOP Python")
        hasil = storage.download_file("catatan.txt")
        print("Isi berkas:", hasil)
