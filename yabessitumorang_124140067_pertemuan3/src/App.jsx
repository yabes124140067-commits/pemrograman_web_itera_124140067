import { NavLink, Route, Routes } from 'react-router-dom'
import Home from './pages/Home/Home.jsx'
import Stats from './pages/Stats/Stats.jsx'

/**
 * Komponen root: header navigasi + definisi route multi-halaman.
 * Provider (Router & Context) dipasang di main.jsx agar mudah dites.
 */
function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Manajemen Buku Pribadi</h1>
        <nav>
          <NavLink to="/" end>
            Beranda
          </NavLink>
          <NavLink to="/stats">Statistik</NavLink>
        </nav>
      </header>
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
          <Route path="*" element={<p>Halaman tidak ditemukan.</p>} />
        </Routes>
      </main>
    </div>
  )
}

export default App
