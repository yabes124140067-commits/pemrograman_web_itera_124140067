import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it, vi } from 'vitest'
import BookForm from '../components/BookForm/BookForm.jsx'
import BookList from '../components/BookList/BookList.jsx'
import BookFilter from '../components/BookFilter/BookFilter.jsx'

describe('BookForm', () => {
  it('menampilkan pesan error bila kolom wajib kosong', async () => {
    const onSubmit = vi.fn()
    render(<BookForm onSubmit={onSubmit} />)
    await userEvent.click(screen.getByRole('button', { name: /tambah buku/i }))

    expect(screen.getByText('Judul buku wajib diisi')).toBeInTheDocument()
    expect(screen.getByText('Nama penulis wajib diisi')).toBeInTheDocument()
    expect(screen.getByLabelText('Judul')).toHaveClass('invalid')
    expect(onSubmit).not.toHaveBeenCalled()
  })

  it('memanggil onSubmit dengan data valid', async () => {
    const onSubmit = vi.fn()
    render(<BookForm onSubmit={onSubmit} />)
    await userEvent.type(screen.getByLabelText('Judul'), 'Clean Code')
    await userEvent.type(screen.getByLabelText('Penulis'), 'Robert Martin')
    await userEvent.selectOptions(screen.getByLabelText('Status'), 'baca')
    await userEvent.click(screen.getByRole('button', { name: /tambah buku/i }))

    expect(onSubmit).toHaveBeenCalledWith({ title: 'Clean Code', author: 'Robert Martin', status: 'baca' })
  })

  it('mengisi form dengan data awal pada mode edit', () => {
    render(<BookForm onSubmit={() => {}} initialData={{ id: '1', title: 'Dune', author: 'Herbert', status: 'beli' }} />)
    expect(screen.getByLabelText('Judul')).toHaveValue('Dune')
    expect(screen.getByRole('button', { name: /simpan perubahan/i })).toBeInTheDocument()
  })
})

describe('BookList', () => {
  const books = [
    { id: '1', title: 'Dune', author: 'Herbert', status: 'milik' },
    { id: '2', title: 'Emma', author: 'Austen', status: 'beli' },
  ]

  it('menampilkan semua buku', () => {
    render(<BookList books={books} onEdit={() => {}} onDelete={() => {}} />)
    expect(screen.getByText('Dune')).toBeInTheDocument()
    expect(screen.getByText('Emma')).toBeInTheDocument()
  })

  it('menampilkan pesan kosong bila tidak ada buku', () => {
    render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} />)
    expect(screen.getByText(/belum ada buku/i)).toBeInTheDocument()
  })

  it('memanggil onDelete dengan id buku', async () => {
    const onDelete = vi.fn()
    render(<BookList books={books} onEdit={() => {}} onDelete={onDelete} />)
    await userEvent.click(screen.getAllByRole('button', { name: 'Hapus' })[0])
    expect(onDelete).toHaveBeenCalledWith('1')
  })
})

describe('BookFilter', () => {
  it('memanggil callback saat mencari dan mengganti status', async () => {
    const onSearchChange = vi.fn()
    const onStatusChange = vi.fn()
    render(
      <BookFilter searchQuery="" onSearchChange={onSearchChange} statusFilter="semua" onStatusChange={onStatusChange} />,
    )
    await userEvent.type(screen.getByLabelText('Cari buku'), 'a')
    expect(onSearchChange).toHaveBeenCalledWith('a')
    await userEvent.selectOptions(screen.getByLabelText('Filter status'), 'beli')
    expect(onStatusChange).toHaveBeenCalledWith('beli')
  })
})
