"""Latihan mandiri: dispatcher multi-saluran notifikasi."""


class NotifikasiEmail:
    """Kanal notifikasi melalui email."""

    def __init__(self, alamat: str):
        self.alamat = alamat

    def kirim(self, pesan: str, penerima: str) -> None:
        """Mengirim pesan melalui email."""
        print(f"[EMAIL -> {penerima}] {pesan}")


class NotifikasiSMS:
    """Kanal notifikasi melalui SMS."""

    def __init__(self, nomor_hp: str):
        self.nomor_hp = nomor_hp

    def kirim(self, pesan: str, penerima: str) -> None:
        """Mengirim pesan melalui SMS."""
        print(f"[SMS -> {penerima}] {pesan}")


class NotifikasiWhatsApp:
    """Kanal notifikasi melalui WhatsApp."""

    def __init__(self, nomor_hp: str):
        self.nomor_hp = nomor_hp

    def kirim(self, pesan: str, penerima: str) -> None:
        """Mengirim pesan melalui WhatsApp."""
        print(f"[WHATSAPP -> {penerima}] {pesan}")


def broadcast_pengumuman(daftar_channel: list, pesan: str) -> None:
    """Mengirim pengumuman ke seluruh kanal secara polimorfik."""
    print("=== BROADCAST PENGUMUMAN DARURAT ===")
    for channel in daftar_channel:
        penerima = getattr(channel, "alamat", None)
        if penerima is None:
            penerima = getattr(channel, "nomor_hp", "pengguna")
        channel.kirim(pesan, penerima)


if __name__ == "__main__":
    channels = [
        NotifikasiEmail("yabes@example.com"),
        NotifikasiSMS("081234567890"),
        NotifikasiWhatsApp("081234567890"),
    ]
    broadcast_pengumuman(
        channels,
        "Segera evakuasi ke titik kumpul terdekat.",
    )
