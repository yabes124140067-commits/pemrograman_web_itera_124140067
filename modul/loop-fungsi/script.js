// FOR LOOP
console.log("For Loop");

for (let i = 1; i <= 5; i++) {
  console.log("Perulangan ke-" + i);
}

// WHILE LOOP
console.log("While Loop");

let angka = 1;

while (angka <= 5) {
  console.log("Angka: " + angka);
  angka++;
}

// FOR...OF
console.log("For...of");

const buah = ["Apel", "Jeruk", "Mangga", "Pisang"];

for (const item of buah) {
  console.log(item);
}

// FUNGSI
function sapaNama(nama) {
  return "Halo, " + nama + "!";
}

console.log(sapaNama("Yabes"));

// FUNGSI KALKULATOR
function kalkulator(a, b, operator) {
  switch (operator) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      return a / b;
    default:
      return "Operator tidak valid";
  }
}

console.log("10 + 5 =", kalkulator(10, 5, "+"));
console.log("10 - 5 =", kalkulator(10, 5, "-"));
console.log("10 * 5 =", kalkulator(10, 5, "*"));
console.log("10 / 5 =", kalkulator(10, 5, "/"));

// MENAMPILKAN HASIL KE HALAMAN
document.getElementById("result").innerHTML = `
    <h2>Hasil Praktikum</h2>
    <p>${sapaNama("Yabes")}</p>
    <p>10 + 5 = ${kalkulator(10, 5, "+")}</p>
    <p>10 - 5 = ${kalkulator(10, 5, "-")}</p>
    <p>10 × 5 = ${kalkulator(10, 5, "*")}</p>
    <p>10 ÷ 5 = ${kalkulator(10, 5, "/")}</p>
`;
