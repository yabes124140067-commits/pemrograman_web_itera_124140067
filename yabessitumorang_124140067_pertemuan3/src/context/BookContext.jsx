import { createContext, useCallback, useContext, useMemo, useState } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage.js'

const BookContext = createContext(null)

export const STORAGE_KEY = 'books-app:books'

/**
 * Provider global state buku (Context API).
 * Menyimpan daftar buku (persisten via localStorage), filter status, dan kata kunci pencarian.
 */
export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage(STORAGE_KEY, [])
  const [statusFilter, setStatusFilter] = useState('semua')
  const [searchQuery, setSearchQuery] = useState('')

  const addBook = useCallback(
    ({ title, author, status }) => {
      const newBook = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 7), title, author, status }
      setBooks((prev) => [...prev, newBook])
    },
    [setBooks],
  )

  const updateBook = useCallback(
    (id, changes) => {
      setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...changes } : b)))
    },
    [setBooks],
  )

  const deleteBook = useCallback(
    (id) => {
      setBooks((prev) => prev.filter((b) => b.id !== id))
    },
    [setBooks],
  )

  // Buku yang tampil = hasil filter status + pencarian judul/penulis
  const filteredBooks = useMemo(() => {
    const q = searchQuery.trim().toLowerCase()
    return books.filter((b) => {
      const matchStatus = statusFilter === 'semua' || b.status === statusFilter
      const matchSearch = q === '' || b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q)
      return matchStatus && matchSearch
    })
  }, [books, statusFilter, searchQuery])

  const value = {
    books,
    filteredBooks,
    statusFilter,
    searchQuery,
    setStatusFilter,
    setSearchQuery,
    addBook,
    updateBook,
    deleteBook,
  }

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
}

/** Hook akses context; error jelas bila dipakai di luar Provider. */
// eslint-disable-next-line react-refresh/only-export-components
export function useBooks() {
  const ctx = useContext(BookContext)
  if (!ctx) throw new Error('useBooks harus dipakai di dalam <BookProvider>')
  return ctx
}
