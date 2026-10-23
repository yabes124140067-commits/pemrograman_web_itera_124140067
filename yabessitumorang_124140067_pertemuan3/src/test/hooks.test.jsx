import { act, renderHook } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import useLocalStorage from '../hooks/useLocalStorage.js'
import useBookStats from '../hooks/useBookStats.js'

describe('useLocalStorage', () => {
  it('memakai nilai awal bila localStorage kosong', () => {
    const { result } = renderHook(() => useLocalStorage('k1', ['a']))
    expect(result.current[0]).toEqual(['a'])
  })

  it('menyimpan perubahan ke localStorage', () => {
    const { result } = renderHook(() => useLocalStorage('k2', 0))
    act(() => result.current[1](42))
    expect(result.current[0]).toBe(42)
    expect(JSON.parse(window.localStorage.getItem('k2'))).toBe(42)
  })

  it('membaca data yang sudah tersimpan', () => {
    window.localStorage.setItem('k3', JSON.stringify({ x: 1 }))
    const { result } = renderHook(() => useLocalStorage('k3', null))
    expect(result.current[0]).toEqual({ x: 1 })
  })
})

describe('useBookStats', () => {
  it('menghitung total dan jumlah per status', () => {
    const books = [
      { id: '1', title: 'A', author: 'x', status: 'milik' },
      { id: '2', title: 'B', author: 'y', status: 'milik' },
      { id: '3', title: 'C', author: 'z', status: 'baca' },
      { id: '4', title: 'D', author: 'w', status: 'beli' },
    ]
    const { result } = renderHook(() => useBookStats(books))
    expect(result.current).toEqual({ total: 4, milik: 2, baca: 1, beli: 1 })
  })

  it('mengembalikan nol untuk daftar kosong', () => {
    const { result } = renderHook(() => useBookStats([]))
    expect(result.current).toEqual({ total: 0, milik: 0, baca: 0, beli: 0 })
  })
})
