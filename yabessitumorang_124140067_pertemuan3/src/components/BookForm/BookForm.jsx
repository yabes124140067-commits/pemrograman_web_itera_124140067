import { useState } from 'react'
import PropTypes from 'prop-types'
import { STATUS_OPTIONS } from '../../constants.js'
import './BookForm.css'

const EMPTY = { title: '', author: '', status: 'milik' }

/**
 * Form tambah / edit buku, dengan validasi kolom wajib isi.
 * Bila `initialData` diberikan, form berada dalam mode edit.
 */
function BookForm({ onSubmit, initialData = null, onCancel = () => {} }) {
  const [form, setForm] = useState(initialData ?? EMPTY)
  const [errors, setErrors] = useState({})
  const isEdit = Boolean(initialData)

  const validate = (values) => {
    const result = {}
    if (!values.title.trim()) result.title = 'Judul buku wajib diisi'
    if (!values.author.trim()) result.author = 'Nama penulis wajib diisi'
    return result
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
    // Hapus pesan error kolom tersebut saat pengguna mulai mengetik
    if (errors[name]) setErrors((prev) => ({ ...prev, [name]: undefined }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const found = validate(form)
    setErrors(found)
    if (Object.keys(found).length > 0) return // berhenti jika ada error

    onSubmit({ title: form.title.trim(), author: form.author.trim(), status: form.status })
    if (!isEdit) setForm(EMPTY) // kosongkan form setelah tambah
  }

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate aria-label="Form buku">
      <h2>{isEdit ? 'Edit Buku' : 'Tambah Buku'}</h2>

      <div className="field">
        <label htmlFor="title">Judul</label>
        <input
          id="title"
          name="title"
          value={form.title}
          onChange={handleChange}
          className={errors.title ? 'invalid' : ''}
          aria-invalid={Boolean(errors.title)}
          placeholder="Contoh: Clean Code"
        />
        {errors.title && (
          <span className="error-text" role="alert">
            {errors.title}
          </span>
        )}
      </div>

      <div className="field">
        <label htmlFor="author">Penulis</label>
        <input
          id="author"
          name="author"
          value={form.author}
          onChange={handleChange}
          className={errors.author ? 'invalid' : ''}
          aria-invalid={Boolean(errors.author)}
          placeholder="Contoh: Robert C. Martin"
        />
        {errors.author && (
          <span className="error-text" role="alert">
            {errors.author}
          </span>
        )}
      </div>

      <div className="field">
        <label htmlFor="status">Status</label>
        <select id="status" name="status" value={form.status} onChange={handleChange}>
          {STATUS_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>

      <div className="form-actions">
        <button type="submit">{isEdit ? 'Simpan Perubahan' : 'Tambah Buku'}</button>
        {isEdit && (
          <button type="button" className="secondary" onClick={onCancel}>
            Batal
          </button>
        )}
      </div>
    </form>
  )
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.shape({
    id: PropTypes.string,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']),
  }),
  onCancel: PropTypes.func,
}

export default BookForm
