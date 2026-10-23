import { useMemo } from 'react'

/**
 * Custom hook: menghitung statistik dari daftar buku.
 * @param {Array<{status: string}>} books
 * @returns {{total:number, milik:number, baca:number, beli:number}}
 */
function useBookStats(books) {
  return useMemo(() => {
    const stats = { total: books.length, milik: 0, baca: 0, beli: 0 }
    books.forEach((book) => {
      if (book.status in stats) stats[book.status] += 1
    })
    return stats
  }, [books])
}

export default useBookStats
