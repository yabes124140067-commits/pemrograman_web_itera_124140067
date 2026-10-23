import PropTypes from 'prop-types'
import BookItem, { bookShape } from '../BookItem/BookItem.jsx'
import './BookList.css'

/** Daftar buku; menampilkan pesan kosong bila tidak ada data. */
function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p className="empty">Belum ada buku yang cocok. Coba tambah buku baru atau ubah filter.</p>
  }

  return (
    <ul className="book-list" aria-label="Daftar buku">
      {books.map((book) => (
        <BookItem key={book.id} book={book} onEdit={onEdit} onDelete={onDelete} />
      ))}
    </ul>
  )
}

BookList.propTypes = {
  books: PropTypes.arrayOf(bookShape).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
}

export default BookList
