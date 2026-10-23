import PropTypes from 'prop-types'
import { STATUS_LABEL } from '../../constants.js'
import './BookItem.css'

/** Satu baris buku: judul, penulis, badge status, tombol edit & hapus. */
function BookItem({ book, onEdit, onDelete }) {
  return (
    <li className="book-item">
      <div className="book-info">
        <strong>{book.title}</strong>
        <span className="author">{book.author}</span>
        <span className={`badge badge-${book.status}`}>{STATUS_LABEL[book.status]}</span>
      </div>
      <div className="book-actions">
        <button type="button" className="secondary" onClick={() => onEdit(book)}>
          Edit
        </button>
        <button type="button" className="danger" onClick={() => onDelete(book.id)}>
          Hapus
        </button>
      </div>
    </li>
  )
}

export const bookShape = PropTypes.shape({
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
})

BookItem.propTypes = {
  book: bookShape.isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
}

export default BookItem
