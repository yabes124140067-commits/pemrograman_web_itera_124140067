console.log("JavaScript berhasil terhubung!");

const formBarang = document.getElementById("form-barang");

let keranjang = [];
const dataKeranjang = localStorage.getItem("keranjang");

if (dataKeranjang) {
  keranjang = JSON.parse(dataKeranjang);
  tampilkanKeranjang();
}
const uangBayarInput = document.getElementById("uang-bayar");
const errorBayar = document.getElementById("error-bayar");
const kembalianElement = document.getElementById("kembalian");
const resetTransaksi = document.getElementById("reset-transaksi");

formBarang.addEventListener("submit", function (event) {
  event.preventDefault();

  const nama = document.getElementById("nama-barang").value.trim();
  const harga = Number(document.getElementById("harga-barang").value);
  const qty = Number(document.getElementById("qty-barang").value);

  const errorNama = document.getElementById("error-nama");
  const errorHarga = document.getElementById("error-harga");
  const errorQty = document.getElementById("error-qty");

  errorNama.textContent = "";
  errorHarga.textContent = "";
  errorQty.textContent = "";

  let valid = true;

  // Validasi nama
  if (nama === "") {
    errorNama.textContent = "Nama barang wajib diisi.";
    valid = false;
  } else if (nama.length < 3) {
    errorNama.textContent = "Nama barang minimal 3 karakter.";
    valid = false;
  }

  // Validasi harga
  if (harga < 500 || isNaN(harga)) {
    errorHarga.textContent = "Harga minimal Rp500.";
    valid = false;
  }

  // Validasi qty
  if (qty < 1 || !Number.isInteger(qty)) {
    errorQty.textContent = "Jumlah harus berupa angka bulat minimal 1.";
    valid = false;
  }

  // Jika valid, masukkan barang ke keranjang
  if (valid) {
    const barang = {
      nama: nama,
      harga: harga,
      qty: qty,
    };

    keranjang.push(barang);

    localStorage.setItem("keranjang", JSON.stringify(keranjang));

    tampilkanKeranjang();
    formBarang.reset();
  }
});

function tampilkanKeranjang() {
  const tabelKeranjang = document.getElementById("tabel-keranjang");
  const totalElement = document.getElementById("total");
  const diskonElement = document.getElementById("diskon");
  const totalAkhirElement = document.getElementById("total-akhir");

  tabelKeranjang.innerHTML = "";

  let total = 0;

  keranjang.forEach(function (barang, index) {
    const subtotal = barang.harga * barang.qty;

    total = total + subtotal;

    const baris = `
            <tr>
                <td>${index + 1}</td>
                <td>${barang.nama}</td>
                <td>Rp ${barang.harga}</td>
                <td>${barang.qty}</td>
                <td>Rp ${subtotal}</td>
                <td>
                    <button onclick="hapusBarang(${index})">
                        Hapus
                    </button>
                </td>
            </tr>
        `;

    tabelKeranjang.innerHTML += baris;
  });

  totalElement.textContent = total;
  let diskon = 0;

  if (total >= 50000) {
    diskon = total * 0.1;
  }

  const totalAkhir = total - diskon;

  diskonElement.textContent = diskon;
  totalAkhirElement.textContent = totalAkhir;
}

function hapusBarang(index) {
  keranjang.splice(index, 1);

  localStorage.setItem("keranjang", JSON.stringify(keranjang));

  tampilkanKeranjang();
}
function hitungKembalian() {
  const uangBayar = Number(uangBayarInput.value);
  const totalAkhir = Number(document.getElementById("total-akhir").textContent);

  errorBayar.textContent = "";

  if (uangBayar < totalAkhir) {
    errorBayar.textContent = "Uang bayar tidak cukup.";
    kembalianElement.textContent = 0;
    return;
  }

  const kembalian = uangBayar - totalAkhir;

  kembalianElement.textContent = kembalian;
}
uangBayarInput.addEventListener("input", hitungKembalian);
resetTransaksi.addEventListener("click", function () {
  keranjang = [];

  localStorage.removeItem("keranjang");

  tampilkanKeranjang();

  formBarang.reset();

  uangBayarInput.value = "";
  errorBayar.textContent = "";
  kembalianElement.textContent = 0;
});
