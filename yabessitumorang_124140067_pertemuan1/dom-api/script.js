// DOM
const teks = document.getElementById("teks");
const tombolTambah = document.getElementById("tambah");
const tombolHapus = document.getElementById("hapus");
const tombolWarna = document.getElementById("warna");

tombolTambah.addEventListener("click", function () {
  teks.textContent = "Teks berhasil ditambahkan.";
});

tombolHapus.addEventListener("click", function () {
  teks.textContent = "";
});

tombolWarna.addEventListener("click", function () {
  teks.style.color = "blue";
});

// FETCH API
async function ambilData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");

    const data = await response.json();

    const posts = document.getElementById("posts");

    posts.innerHTML = "";

    data.slice(0, 5).forEach(function (post) {
      const div = document.createElement("div");

      div.innerHTML = `
                <h3>${post.title}</h3>
                <p>${post.body}</p>
                <hr>
            `;

      posts.appendChild(div);
    });
  } catch (error) {
    document.getElementById("posts").textContent = "Gagal mengambil data API.";
    console.error(error);
  }
}

ambilData();
