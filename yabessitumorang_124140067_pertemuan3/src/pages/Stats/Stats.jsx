import { Link } from 'react-router-dom'
import { useBooks } from '../../context/BookContext.jsx'
import useBookStats from '../../hooks/useBookStats.js'
import './Stats.css'

/** Halaman statistik: jumlah buku per status. */
function Stats() {
  const { books } = useBooks()
  const stats = useBookStats(books)

  const cards = [
    { key: 'total', label: 'Total Buku', value: stats.total },
    { key: 'milik', label: 'Milik', value: stats.milik },
    { key: 'baca', label: 'Sedang Dibaca', value: stats.baca },
    { key: 'beli', label: 'Ingin Dibeli', value: stats.beli },
  ]

  return (
    <section>
      <h2>Statistik Buku</h2>
      <div className="stats-grid">
        {cards.map((c) => (
          <div key={c.key} className={`stat-card stat-${c.key}`}>
            <span className="stat-value">{c.value}</span>
            <span className="stat-label">{c.label}</span>
          </div>
        ))}
      </div>
      <p>
        <Link to="/">← Kembali ke daftar buku</Link>
      </p>
    </section>
  )
}

export default Stats
