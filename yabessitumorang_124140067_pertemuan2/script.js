// =====================================================
// Dashboard Tugas Kuliah - Pertemuan 2 (ES6+)
// =====================================================

// ---------- Fungsi bantu (arrow functions) ----------
// Mencegah teks dari user dibaca sebagai HTML
const escapeHtml = (teks) =>
  String(teks).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[c]);

// Format tanggal ke bahasa Indonesia, contoh: 17 Okt 2026
const formatTanggal = (tanggal) =>
  new Date(tanggal).toLocaleDateString("id-ID", { day: "numeric", month: "short", year: "numeric" });

// Kode cuaca Open-Meteo -> teks singkat
const KODE_CUACA = {
  0: "Cerah", 1: "Cerah berawan", 2: "Berawan sebagian", 3: "Mendung",
  45: "Berkabut", 51: "Gerimis", 61: "Hujan ringan", 63: "Hujan sedang",
  65: "Hujan lebat", 80: "Hujan lokal", 95: "Badai petir"
};

// ---------- CLASS 1: TaskItem (model data satu tugas) ----------
class TaskItem {
  // Destructuring di parameter + nilai default
  constructor({ id = Date.now(), title, course = "", deadline = "", done = false }) {
    this.id = id;
    this.title = title;
    this.course = course;
    this.deadline = deadline;
    this.done = done;
  }

  // Mengembalikan objek BARU (immutable) dengan spread operator
  toggle() {
    return new TaskItem({ ...this, done: !this.done });
  }

  // Getter: true kalau sudah lewat deadline dan belum selesai
  get isOverdue() {
    if (!this.deadline || this.done) return false;
    const hariIni = new Date().toISOString().slice(0, 10);
    return this.deadline < hariIni;
  }
}

// ---------- CLASS 2: DashboardApp (mengatur seluruh aplikasi) ----------
class DashboardApp {
  constructor() {
    this.storageKey = "dashboard_tugas_v1";
    this.tasks = [];
    this.filter = "all";

    // Ambil elemen HTML yang dipakai
    this.form = document.querySelector("#form-tugas");
    this.list = document.querySelector("#daftar-tugas");
    this.filterBox = document.querySelector("#filter");
    this.statBox = document.querySelector("#statistik");
  }

  // Fungsi utama: dijalankan sekali saat halaman dibuka
  async init() {
    this.startClock();
    this.bindEvents();
    await this.loadTasks();
    this.render();
    // Cuaca & kutipan jalan bersamaan, tidak saling menunggu
    this.loadWeather();
    this.loadQuote();
  }

  // ----- localStorage -----
  saveTasks() {
    localStorage.setItem(this.storageKey, JSON.stringify(this.tasks));
  }

  async loadTasks() {
    const saved = localStorage.getItem(this.storageKey);

    if (saved !== null) {
      // Sudah pernah disimpan: ubah data biasa jadi objek TaskItem lagi
      this.tasks = JSON.parse(saved).map((data) => new TaskItem(data));
      return;
    }

    // Pertama kali dibuka: ambil contoh tugas dari API (async/await)
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/todos?_limit=5");
      const data = await response.json();
      this.tasks = data.map(({ id, title, completed }) =>
        new TaskItem({ id, title, course: "Contoh", done: completed })
      );
    } catch (error) {
      console.error("Gagal memuat tugas awal:", error);
      this.tasks = [];
    }
    this.saveTasks();
  }

  // ----- Operasi tugas (spread operator = array tidak diubah langsung) -----
  addTask(data) {
    const task = new TaskItem(data);
    this.tasks = [task, ...this.tasks];
    this.update();
  }

  toggleTask(id) {
    this.tasks = this.tasks.map((t) => (t.id === id ? t.toggle() : t));
    this.update();
  }

  editTask(id) {
    const task = this.tasks.find((t) => t.id === id);
    const judulBaru = prompt("Ubah judul tugas:", task.title);
    if (judulBaru === null || judulBaru.trim() === "") return; // dibatalkan
    this.tasks = this.tasks.map((t) =>
      t.id === id ? new TaskItem({ ...t, title: judulBaru.trim() }) : t
    );
    this.update();
  }

  deleteTask(id) {
    if (!confirm("Hapus tugas ini?")) return;
    this.tasks = this.tasks.filter((t) => t.id !== id);
    this.update();
  }

  update() {
    this.saveTasks();
    this.render();
  }

  // ----- Event -----
  bindEvents() {
    // Tambah tugas
    this.form.addEventListener("submit", (e) => {
      e.preventDefault();
      const title = document.querySelector("#input-judul").value.trim();
      const course = document.querySelector("#input-matkul").value.trim();
      const deadline = document.querySelector("#input-deadline").value;
      if (!title) return;
      this.addTask({ title, course, deadline });
      this.form.reset();
    });

    // Klik tombol filter
    this.filterBox.addEventListener("click", (e) => {
      const { filter } = e.target.dataset;
      if (!filter) return;
      this.filter = filter;
      this.filterBox.querySelectorAll("button").forEach((b) =>
        b.classList.toggle("aktif", b === e.target)
      );
      this.render();
    });

    // Klik di daftar tugas (centang / edit / hapus)
    this.list.addEventListener("click", (e) => {
      const { action, id } = e.target.dataset;
      if (!action) return;
      const taskId = Number(id);
      if (action === "toggle") this.toggleTask(taskId);
      if (action === "edit") this.editTask(taskId);
      if (action === "delete") this.deleteTask(taskId);
    });
  }

  // ----- Tampilan (template literals) -----
  render() {
    const shown = this.tasks.filter(({ done }) => {
      if (this.filter === "active") return !done;
      if (this.filter === "done") return done;
      return true;
    });

    // let dipakai karena nilainya ditentukan nanti (bergantung isi daftar)
    let html;
    if (shown.length === 0) {
      html = `<li class="kosong">Belum ada tugas di sini. Tambahkan lewat form di atas.</li>`;
    } else {
      html = shown.map((t) => `
        <li class="item ${t.done ? "selesai" : ""}">
          <input type="checkbox" data-action="toggle" data-id="${t.id}"
                 ${t.done ? "checked" : ""} aria-label="Tandai selesai">
          <div class="isi">
            <p class="judul">${escapeHtml(t.title)}</p>
            <p class="info">
              ${t.course ? escapeHtml(t.course) : "Tanpa mata kuliah"}
              ${t.deadline ? ` &bull; Deadline ${formatTanggal(t.deadline)}` : ""}
              ${t.isOverdue ? ` <span class="terlambat">&bull; Terlambat</span>` : ""}
            </p>
          </div>
          <div class="aksi">
            <button class="ghost" data-action="edit" data-id="${t.id}">Edit</button>
            <button class="danger" data-action="delete" data-id="${t.id}">Hapus</button>
          </div>
        </li>`).join("");
    }
    this.list.innerHTML = html;
    this.renderStats();
  }

  renderStats() {
    const total = this.tasks.length;
    const selesai = this.tasks.filter((t) => t.done).length;
    const terlambat = this.tasks.filter((t) => t.isOverdue).length;
    this.statBox.innerHTML = `
      <h2>Ringkasan</h2>
      <div class="stat"><span>Total tugas</span><strong>${total}</strong></div>
      <div class="stat"><span>Selesai</span><strong>${selesai}</strong></div>
      <div class="stat"><span>Belum selesai</span><strong>${total - selesai}</strong></div>
      <div class="stat"><span>Terlambat</span><strong>${terlambat}</strong></div>`;
  }

  // ----- Jam & tanggal -----
  startClock() {
    const tick = () => {
      const now = new Date();
      document.querySelector("#jam").textContent = now.toLocaleTimeString("id-ID");
      document.querySelector("#tanggal").textContent = now.toLocaleDateString("id-ID", {
        weekday: "long", day: "numeric", month: "long", year: "numeric"
      });
    };
    tick();
    setInterval(tick, 1000);
  }

  // ----- API: cuaca (async/await) -----
  async loadWeather() {
    const box = document.querySelector("#cuaca");
    try {
      const url = "https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true";
      const response = await fetch(url);
      const { current_weather: { temperature, windspeed, weathercode } } = await response.json();
      box.innerHTML = `
        <h2>Cuaca di ITERA</h2>
        <p class="suhu">${temperature}&deg;C</p>
        <p class="muted">${KODE_CUACA[weathercode] ?? "Cuaca tidak diketahui"} &bull; Angin ${windspeed} km/j</p>`;
    } catch (error) {
      box.innerHTML = `<h2>Cuaca di ITERA</h2><p class="muted">Gagal memuat cuaca. Cek koneksi internet.</p>`;
    }
  }

  // ----- API: kutipan (async/await) -----
  async loadQuote() {
    const box = document.querySelector("#kutipan");
    try {
      const response = await fetch("https://dummyjson.com/quotes/random");
      const { quote, author } = await response.json();
      box.innerHTML = `
        <h2>Kutipan hari ini</h2>
        <blockquote>"${escapeHtml(quote)}"</blockquote>
        <p class="penulis">${escapeHtml(author)}</p>
        <button class="ghost" id="btn-kutipan">Kutipan lain</button>`;
      document.querySelector("#btn-kutipan").addEventListener("click", () => this.loadQuote());
    } catch (error) {
      box.innerHTML = `<h2>Kutipan hari ini</h2><p class="muted">Gagal memuat kutipan. Cek koneksi internet.</p>`;
    }
  }
}

// ---------- Jalankan aplikasi ----------
const app = new DashboardApp();
app.init();