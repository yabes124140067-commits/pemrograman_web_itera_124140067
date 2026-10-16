// ARRAY
let buah = ["Apel", "Jeruk", "Mangga"];

console.log("Array awal:", buah);

// PUSH
buah.push("Pisang");
console.log("Setelah push:", buah);

// POP
buah.pop();
console.log("Setelah pop:", buah);

// SORT
buah.sort();
console.log("Setelah sort:", buah);

// MAP
let buahBesar = buah.map(function (item) {
  return item.toUpperCase();
});

console.log("Hasil map:", buahBesar);

// FILTER
let hasilFilter = buah.filter(function (item) {
  return item.length > 5;
});

console.log("Hasil filter:", hasilFilter);

// OBJECT
const mahasiswa = {
  nama: "Yabes Situmorang",
  nim: "124140067",
  jurusan: "Teknik Informatika",

  tampilkanData: function () {
    return `
            Nama: ${this.nama}<br>
            NIM: ${this.nim}<br>
            Jurusan: ${this.jurusan}
        `;
  },
};

console.log(mahasiswa.nama);
console.log(mahasiswa.nim);
console.log(mahasiswa.jurusan);

// MENAMPILKAN HASIL
document.getElementById("result").innerHTML = `
    <h2>Data Mahasiswa</h2>
    <p>${mahasiswa.tampilkanData()}</p>

    <h2>Array Buah</h2>
    <p>${buah.join(", ")}</p>

    <h2>Hasil Map</h2>
    <p>${buahBesar.join(", ")}</p>

    <h2>Hasil Filter</h2>
    <p>${hasilFilter.join(", ")}</p>
`;
