// Variabel
var nama = "Yabes Situmorang";
let usia = 20;
const TAHUN_LAHIR = 2006;

console.log("Nama: " + nama);
console.log("Usia: " + usia);
console.log("Tahun Lahir: " + TAHUN_LAHIR);

document.getElementById("result").innerHTML = `
    <p>Nama: <strong>${nama}</strong></p>
    <p>Usia: <strong>${usia}</strong></p>
    <p>Tahun Lahir: <strong>${TAHUN_LAHIR}</strong></p>
`;

// Kondisional
let nilai = 85;

if (nilai >= 90) {
  console.log("Grade A");
} else if (nilai >= 80) {
  console.log("Grade B");
} else if (nilai >= 70) {
  console.log("Grade C");
} else {
  console.log("Grade D");
}

// Ternary
let status = nilai >= 70 ? "Lulus" : "Tidak Lulus";
console.log("Status: " + status);

// Switch Case
let hari = 3;

switch (hari) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
  default:
    console.log("Hari tidak valid");
}
