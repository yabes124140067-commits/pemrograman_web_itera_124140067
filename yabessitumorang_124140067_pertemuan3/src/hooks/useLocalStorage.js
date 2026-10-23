import { useEffect, useState } from 'react'

/**
 * Custom hook: state yang otomatis disinkronkan ke localStorage.
 * @param {string} key          kunci di localStorage
 * @param {*} initialValue      nilai awal bila belum ada data tersimpan
 * @returns {[*, Function]}     [value, setValue] seperti useState
 */
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = window.localStorage.getItem(key)
      return stored !== null ? JSON.parse(stored) : initialValue
    } catch (error) {
      // JSON rusak / localStorage tidak tersedia -> pakai nilai awal
      console.error(`Gagal membaca localStorage["${key}"]`, error)
      return initialValue
    }
  })

  // Simpan ulang setiap kali value berubah
  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value))
    } catch (error) {
      console.error(`Gagal menulis localStorage["${key}"]`, error)
    }
  }, [key, value])

  return [value, setValue]
}

export default useLocalStorage
