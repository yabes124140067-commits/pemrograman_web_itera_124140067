import { useState } from 'react'
import BookForm from '../../components/BookForm/BookForm.jsx'
import BookFilter from '../../components/BookFilter/BookFilter.jsx'
import BookList from '../../components/BookList/BookList.jsx'
import { useBooks } from '../../context/BookContext.jsx'
import './Home.css'

/** Halaman utama: form tambah/edit, filter, dan daftar buku. */
function Home() {
  const { filteredBooks, searchQuery, setSearchQuery, statusFilter, setStatusFilter, addBook, updateBook, deleteBook } =
    useBooks()
  const [editingBook, setEditingBook] = useState(null)

  const handleSubmit = (data) => {
    if (editingBook) {
      updateBook(editingBook.id, data)
      setEditingBook(null)
    } else {
      addBook(data)
    }
  }

  const handleDelete = (id) => {
    if (window.confirm('Yakin ingin menghapus buku ini?')) {
      deleteBook(id)
      if (editingBook?.id === id) setEditingBook(null)
    }
  }

  return (
    <section className="home">
      {/* key memaksa form di-reset saat berpindah antara mode tambah / edit buku lain */}
      <BookForm
        key={editingBook ? editingBook.id : 'new'}
        onSubmit={handleSubmit}
        initialData={editingBook}
        onCancel={() => setEditingBook(null)}
      />
      <BookFilter
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        statusFilter={statusFilter}
        onStatusChange={setStatusFilter}
      />
      <BookList books={filteredBooks} onEdit={setEditingBook} onDelete={handleDelete} />
    </section>
  )
}

export default Home
