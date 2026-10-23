import '@testing-library/jest-dom/vitest'
import { afterEach } from 'vitest'
import { cleanup } from '@testing-library/react'

// Bersihkan DOM & localStorage setiap selesai satu test
afterEach(() => {
  cleanup()
  window.localStorage.clear()
})
