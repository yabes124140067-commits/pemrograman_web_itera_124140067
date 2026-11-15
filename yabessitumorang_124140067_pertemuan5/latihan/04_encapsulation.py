"""Penerapan encapsulation dan property pada rekening bank.

Program mendemonstrasikan atribut public, protected, private, name
mangling, serta getter dan setter melalui dekorator ``@property``.
"""


class RekeningBank:
    """Rekening bank dengan validasi saldo dan PIN private."""

    def __init__(
        self,
        nomor_rekening: str,
        nama_pemilik: str,
        saldo_awal: float,
        pin: str,
    ):
        self.nomor_rekening = nomor_rekening
        self._pemilik = nama_pemilik
        self.__saldo = max(0.0, float(saldo_awal))
        self.__pin = str(pin)
        self._riwayat_transaksi = []

    @property
    def saldo(self) -> float:
        """Mengembalikan saldo sebagai atribut read-only."""
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah_baru: float):
        """Mengubah saldo dengan validasi tipe dan nilai."""
        if not isinstance(jumlah_baru, (int, float)):
            raise TypeError("Nilai saldo harus berupa angka numerik!")
        if jumlah_baru < 0:
            raise ValueError("Saldo rekening tidak boleh negatif!")
        self.__saldo = float(jumlah_baru)
        print(
            f"[AUDIT] Saldo {self.nomor_rekening} disesuaikan "
            f"langsung menjadi: Rp {self.__saldo:,.2f}"
        )

    def setor(self, nominal: float):
        """Menambah saldo melalui transaksi setor tunai."""
        if nominal <= 0:
            print("Gagal: Nominal setor harus lebih besar dari Rp 0!")
            return
        self.__saldo += nominal
        self._riwayat_transaksi.append(
            f"Setor Tunai: +Rp {nominal:,.2f}"
        )
        print(
            f"Setor tunai Rp {nominal:,.2f} sukses. "
            f"Saldo saat ini: Rp {self.__saldo:,.2f}"
        )

    def tarik(self, nominal: float, pin_input: str) -> bool:
        """Menarik saldo setelah memvalidasi PIN dan kecukupan dana."""
        if pin_input != self.__pin:
            print("Gagal: PIN Transaksi yang Anda masukkan salah!")
            return False

        if nominal <= 0:
            print("Gagal: Nominal penarikan harus lebih dari Rp 0!")
            return False

        if nominal > self.__saldo:
            print(
                f"Gagal: Saldo tidak mencukupi! "
                f"(Saldo: Rp {self.__saldo:,.2f}, "
                f"Tarik: Rp {nominal:,.2f})"
            )
            return False

        self.__saldo -= nominal
        self._riwayat_transaksi.append(
            f"Tarik Tunai: -Rp {nominal:,.2f}"
        )
        print(
            f"Tarik tunai Rp {nominal:,.2f} berhasil. "
            f"Sisa saldo: Rp {self.__saldo:,.2f}"
        )
        return True

    def cetak_mutasi(self):
        """Menampilkan seluruh riwayat transaksi dan saldo akhir."""
        print(
            f"\n=== MUTASI REKENING {self.nomor_rekening} "
            f"({self._pemilik}) ==="
        )
        for log in self._riwayat_transaksi:
            print(f" - {log}")
        print(
            f"Saldo Akhir Terverifikasi: Rp {self.__saldo:,.2f}"
        )


if __name__ == "__main__":
    rek = RekeningBank(
        "121-009-8871",
        "Ahmad Fadhilah",
        500000,
        "123456",
    )

    print("Nomor Rekening (Public) :", rek.nomor_rekening)
    print("Pemilik Rekening (Prot) :", rek._pemilik)
    print("Saldo Rekening (@prop)  : Rp", rek.saldo)

    rek.setor(250000)
    rek.tarik(100000, "999999")
    rek.tarik(100000, "123456")
    rek.tarik(1000000, "123456")

    try:
        rek.saldo = -50000
    except ValueError as err:
        print(f"\nValidasi Tertangkap: {err}")

    print("\n--- Uji Proteksi Private Attribute ---")
    try:
        print(rek.__saldo)
    except AttributeError:
        print(
            "Akses langsung rek.__saldo GAGAL karena terlindungi "
            "(AttributeError)!"
        )

    print(
        "Nilai via Name Mangling (rek._RekeningBank__saldo): Rp",
        rek._RekeningBank__saldo,
    )

    rek.cetak_mutasi()
