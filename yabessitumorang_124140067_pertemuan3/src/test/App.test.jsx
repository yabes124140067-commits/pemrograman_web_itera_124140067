import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { beforeEach, describe, expect, it, vi } from 'vitest'
import App from '../App.jsx'
import { BookProvider, STORAGE_KEY } from '../context/BookContext.jsx'

const renderApp = (route = '/') =>
  render(
    <MemoryRouter initialEntries={[route]}>
      <BookProvider>
        <App />
      </BookProvider>
    </MemoryRouter>,
  )

const addBook = async (title, author, status = 'milik') => {
  await userEvent.type(screen.getByLabelText('Judul'), title)
  await userEvent.type(screen.getByLabelText('Penulis'), author)
  await userEvent.selectOptions(screen.getByLabelText('Status'), status)
  await userEvent.click(screen.getByRole('button', { name: /tambah buku/i }))
}

describe('App (integrasi)', () => {
  beforeEach(() => {
    vi.spyOn(window, 'confirm').mockReturnValue(true)
  })

  it('menambah buku dan menyimpannya ke localStorage', async () => {
    renderApp()
    await addBook('Clean Code', 'Robert Martin')
    expect(screen.getByText('Clean Code')).toBeInTheDocument()
    expect(JSON.parse(window.localStorage.getItem(STORAGE_KEY))).toHaveLength(1)
  })

  it('mengedit buku', async () => {
    renderApp()
    await addBook('Dune', 'Herbert')
    await userEvent.click(screen.getByRole('button', { name: 'Edit' }))
    const title = screen.getByLabelText('Judul')
    await userEvent.clear(title)
    await userEvent.type(title, 'Dune Messiah')
    await userEvent.click(screen.getByRole('button', { name: /simpan perubahan/i }))
    expect(screen.getByText('Dune Messiah')).toBeInTheDocument()
  })

  it('menghapus buku', async () => {
    renderApp()
    await addBook('Emma', 'Austen')
    await userEvent.click(screen.getByRole('button', { name: 'Hapus' }))
    expect(screen.queryByText('Emma')).not.toBeInTheDocument()
  })

  it('memfilter berdasarkan status dan mencari berdasarkan judul/penulis', async () => {
    renderApp()
    await addBook('Dune', 'Herbert', 'milik')
    await addBook('Emma', 'Austen', 'beli')

    await userEvent.selectOptions(screen.getByLabelText('Filter status'), 'beli')
    expect(screen.queryByText('Dune')).not.toBeInTheDocument()
    expect(screen.getByText('Emma')).toBeInTheDocument()

    await userEvent.selectOptions(screen.getByLabelText('Filter status'), 'semua')
    await userEvent.type(screen.getByLabelText('Cari buku'), 'herb')
    expect(screen.getByText('Dune')).toBeInTheDocument()
    expect(screen.queryByText('Emma')).not.toBeInTheDocument()
  })

  it('menampilkan statistik di halaman /stats', async () => {
    window.localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify([
        { id: '1', title: 'A', author: 'a', status: 'milik' },
        { id: '2', title: 'B', author: 'b', status: 'baca' },
      ]),
    )
    renderApp('/stats')
    const total = screen.getByText('Total Buku').closest('.stat-card')
    expect(within(total).getByText('2')).toBeInTheDocument()
  })
})
