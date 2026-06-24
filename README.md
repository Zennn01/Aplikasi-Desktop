# 📋 Aplikasi Desktop — Biodata & Absensi

Repositori berisi aplikasi desktop untuk manajemen biodata (profil pengguna) dan absensi menggunakan Python (Tkinter) & SQLite. Dokumentasi ini menyelaraskan istilah sehingga "Biodata" dan "Absensi" dipahami dengan konsisten.

---

## 📂 Struktur Project (root)

```
Aplikasi-Desktop/
├── Pertemuan-1/          # Versi 1 (folder kapital P) — Aplikasi Biodata Sederhana
├── pertemuan-2/          # Versi 2 (folder lowercase) — Aplikasi dengan Absensi & Auth
│   └── README.md         # Dokumentasi detil versi 2
└── README.md             # File ini (ringkasan & quick start)
```

---

## 🎯 Ringkasan Fitur

Project ini menggabungkan dua fitur utama:
- **Biodata**: pengelolaan profil pengguna (nama, alamat, NIM, dsb.)
- **Absensi**: pencatatan kehadiran (jam masuk/pulang, status, riwayat)

Kedua fitur dihubungkan oleh controller utama `BioDataController` yang melakukan navigasi antar view dan memanggil model untuk operasi database.

---

## 📁 Penjelasan Lengkap Per Folder

### 🔹 **Pertemuan-1** — Aplikasi Biodata Sederhana (Versi Pertama)

Versi pertama aplikasi yang fokus pada **menampilkan biodata pengguna** dalam format kartu (card).

#### Struktur folder:

```
Pertemuan-1/
├── main.py               # Entry point aplikasi
├── test.py               # Sanity check: verifikasi tools & dependencies
├── controllers/
│   └── biodata_controller.py    # Koordinator logic & view
├── models/
│   └── biodata_model.py         # Data biodata (hardcoded)
├── views/
│   └── biodata_view.py          # UI tampilan kartu biodata
└── databases/
    ├── database.py              # Setup database SQLite & seed data
    └── absensi.db               # File database (auto-generated)
```

#### Penjelasan file per file:

**`main.py`** — Entry Point
- Inisialisasi window Tkinter
- Membuat instance `BioDataController`
- Menjalankan aplikasi dengan `.run()`

**`test.py`** — Sanity Check
- Verifikasi kesiapan environment: Python, Tkinter, SQLite3, Pillow
- Menampilkan popup confirmation jika semua tools siap

**`controllers/biodata_controller.py`** — MVC Controller
- Menghubungkan antara model (data) dan view (UI)
- Mengambil data dari `BioDataModel`
- Menampilkan ke UI menggunakan `BioDataView`
- Menjalankan event loop Tkinter

**`models/biodata_model.py`** — Data Model
- Menyimpan data biodata dalam dictionary (hardcoded)
- Field: nama, NIM, kelas, jurusan, email, telepon, alamat, hobi
- Method `get_biodata()` mengembalikan data dalam bentuk dictionary

**`views/biodata_view.py`** — UI Layer
- Membuat UI kartu biodata dengan Tkinter
- Header biru dengan avatar & nama
- Body berisi daftar field biodata
- Styling: border, font, warna, padding
- Method `show_card()` untuk menampilkan kartu
- Method `_add_info_row()` helper untuk baris info individual

**`databases/database.py`** — Database Setup
- **`get_connection()`** — Membuat koneksi ke SQLite
- **`init_database()`** — Membuat tabel `users` dan `absensi`
  - Tabel `users`: id, username, password, role, nama, created_at
  - Tabel `absensi`: id, user_id, tanggal, jam_masuk, jam_pulang, status, keterangan, created_at
- **`insert_default_data()`** — Insert akun demo:
  - Dosen: `dosen1` / `123456`
  - Mahasiswa: `mahasiswa1` / `123456`, `mahasiswa2` / `123456`
- **`absensi.db`** — SQLite database file (auto-generated setelah menjalankan database.py)

---

### 🔹 **pertemuan-2** — Aplikasi Biodata + Absensi + Authentication (Versi Perbaikan)

Versi lanjutan dengan fitur **authentication**, **manajemen pengguna**, dan **pencatatan absensi**.

*Lihat: `pertemuan-2/README.md` untuk dokumentasi detail versi 2*

#### Perbedaan utama vs Pertemuan-1:
- ✅ Sistem login (authentication)
- ✅ Multi-user support
- ✅ Navigasi antar halaman (dashboard, biodata, absensi)
- ✅ CRUD operations lebih kompleks

---

## 🚀 Quick Start (Jalankan Aplikasi)

### 1️⃣ **Pertemuan-1 (Rekomendasi untuk pemula)**

```bash
# Clone repo
git clone https://github.com/Zennn01/Aplikasi-Desktop.git
cd Aplikasi-Desktop

# Install dependency
pip install pillow

# Buka folder Pertemuan-1
cd Pertemuan-1

# Setup database (opsional)
python databases/database.py

# Jalankan aplikasi
python main.py

# Jalankan sanity check
python test.py
```

**Expected Output:**
- Jendela aplikasi membuka dengan kartu biodata
- Menampilkan data: Nama, NIM, Kelas, Jurusan, Email, Telepon, Alamat, Hobi

---

### 2️⃣ **pertemuan-2 (Rekomendasi untuk production)**

```bash
cd pertemuan-2

# Setup database
python databases/database.py

# Jalankan aplikasi
python main.py

# Jalankan sanity check
python test.py
```

**Expected Output:**
- Jendela login screen
- Masuk dengan akun: `mahasiswa1` / `123456` atau `admin` / `123456`
- Dashboard dengan fitur biodata & absensi

---

## 👥 Akun Demo (Data Seed)

### Pertemuan-1 & Pertemuan-2

| Username | Password | Role | Status |
|----------|----------|------|--------|
| `admin` | `123456` | Admin | ✅ Pertemuan-2 only |
| `mahasiswa1` | `123456` | Mahasiswa | ✅ |
| `mahasiswa2` | `123456` | Mahasiswa | ✅ |

> **Catatan Security:** Password disimpan plain-text untuk development. **Jangan gunakan di production!**

---

## 🛠 Troubleshooting

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError: No module named 'PIL'` | `pip install pillow` |
| `ModuleNotFoundError: No module named 'tkinter'` | Pasang tkinter sesuai OS (biasanya included Python) |
| `Database is locked` | Tutup proses lain yang mengakses `absensi.db` |
| Aplikasi tidak merespons | Pastikan Python & Tkinter terpasang dengan benar |

---

## 📊 Arsitektur MVC

Aplikasi menggunakan pola **Model-View-Controller (MVC)**:

```
┌─────────────┐
│   View      │  ← Menampilkan UI (Tkinter)
└──────┬──────┘
       │
┌──────▼──────┐
│ Controller  │  ← Koordinator logic
└──────┬──────┘
       │
┌──────▼──────┐
│   Model     │  ← Mengelola data (dict/database)
└─────────────┘
```

**Alur:**
1. `main.py` → inisialisasi Controller
2. Controller → ambil data dari Model
3. Controller → render View dengan data
4. View → tampilkan UI ke user

---

## 🔗 Dokumentasi Detil

- **Pertemuan-1 Documentation:** `Pertemuan-1/` (folder ini)
- **Pertemuan-2 Documentation:** `pertemuan-2/README.md` — dokumentasi lengkap versi 2 (rekomendasi)

---

## 📌 Catatan Developer

- `BioDataController` menangani navigasi dan logika untuk biodata serta absensi.
- Database default dan akun seed dibuat oleh `databases/database.py`.
- Password disimpan plain-text untuk keperluan development; jangan dipakai di produksi.
- Gunakan **pertemuan-2** untuk aplikasi yang lebih matang & production-ready.

---

**Last Updated:** 2026-06-24
