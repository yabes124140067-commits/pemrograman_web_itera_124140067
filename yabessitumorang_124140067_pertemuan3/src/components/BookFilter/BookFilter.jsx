import PropTypes from 'prop-types'
import { STATUS_OPTIONS } from '../../constants.js'
import './BookFilter.css'

/** Kontrol pencarian (judul/penulis) dan filter status. */
function BookFilter({ searchQuery, onSearchChange, statusFilter, onStatusChange }) {
  return (
    <div className="book-filter">
      <input
        type="search"
        placeholder="Cari judul atau penulis..."
        aria-label="Cari buku"
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
      />
      <select aria-label="Filter status" value={statusFilter} onChange={(e) => onStatusChange(e.target.value)}>
        <option value="semua">Semua Status</option>
        {STATUS_OPTIONS.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  )
}

BookFilter.propTypes = {
  searchQuery: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  statusFilter: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
}

export default BookFilter
