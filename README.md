# 📋 Aplikasi Desktop - Sistem Absensi

Repositori berisi koleksi aplikasi desktop untuk manajemen absensi dan biodata dengan Python Tkinter & SQLite.

---

## 📂 Struktur Project

```
Aplikasi-Desktop/
├── pertemuan-1/          # (Jika ada)
├── pertemuan-2/          # ⭐ Sistem Absensi Lengkap
│   ├── databases/
│   ├── controllers/
│   ├── models/
│   ├── views/
│   ├── main.py
│   ├── test.py
│   └── README.md
└── README.md             # File ini
```

---

## 🎯 Pertemuan 2: Sistem Absensi Desktop

### 📁 **Folder 1: `databases/`** - Database Management

Mengelola semua operasi database menggunakan SQLite.

#### 📄 File:
- **`database.py`** - Script inisialisasi & migrasi database
- **`absensi.db`** - File database (otomatis dibuat)

#### ✨ Fitur:
```
✓ Koneksi database dengan pengaturan optimal
✓ Inisialisasi tabel Users dan Absensi
✓ Migrasi data aman (tanpa menghapus data lama)
✓ Insert data default untuk testing
✓ Foreign key constraints untuk data integrity
```

#### 📊 Struktur Database:

**Tabel USERS:**
```sql
id, username, password, role, nama, alamat, 
nim, kelas, jurusan, email, telepon, hobi, created_at
```

**Tabel ABSENSI:**
```sql
id, user_id, tanggal, jam_masuk, jam_pulang, 
status, keterangan, created_at
```

---

### 🎯 **Folder 2: `controllers/`** - Business Logic

Mengontrol alur aplikasi, navigasi, dan interaksi user.

#### 📄 File:
- **`biodata_controller.py`** - Controller utama aplikasi

#### 🎮 Fungsi:
```
✓ Manajemen session (login/logout)
✓ Navigasi antar view
✓ Handle event user
✓ Integrasi Model ↔ View
✓ Validasi input & error handling
```

#### 🔄 Alur Aplikasi:
```
LOGIN 
  ↓
DASHBOARD (tampilan utama)
  ├─→ ABSENSI (Checkin/Checkout)
  ├─→ BIODATA (Lihat profil)
  ├─→ RIWAYAT (Histori absensi)
  ├─→ EDIT BIODATA (Admin only)
  └─→ LOGOUT
```

---

## 🚀 Cara Menjalankan

### 1️⃣ **Setup Awal (Sekali saja)**

```bash
# Clone atau masuk ke folder project
cd Aplikasi-Desktop

# Install dependencies
pip install pillow
```

### 2️⃣ **Inisialisasi Database**

```bash
# Jalankan dari folder pertemuan-2
cd pertemuan-2
python databases/database.py

# Output: Database initialized successfully!
```

### 3️⃣ **Jalankan Aplikasi**

```bash
# Dari folder pertemuan-2
python main.py
```

### 4️⃣ **Test Environment**

```bash
# Verifikasi semua library terpasang
python test.py
```

---

## 👤 Akun Demo

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `123456` |
| Mahasiswa 1 | `mahasiswa1` | `123456` |
| Mahasiswa 2 | `mahasiswa2` | `123456` |

---

## 📸 User Interface Flow

```
┌─────────────────────────────────────┐
│      SISTEM ABSENSI DESKTOP         │
└─────────────────────────────────────┘
            │
            ▼
    ┌───────────────────┐
    │  📋 LOGIN VIEW    │
    │ Username/Password │
    └───────────────────┘
            │
    ┌───────┴────────┐
    │                │
   ✓ Valid      ✗ Invalid
    │                │
    ▼                ▼
DASHBOARD      Error & Retry
    │
    ├─► 📝 ABSENSI
    │   (Checkin/Checkout)
    │
    ├─► 👤 BIODATA
    │   (Lihat Profil)
    │
    ├─► 📊 RIWAYAT
    │   (History Absensi)
    │
    ├─► ✏️ EDIT BIODATA
    │   (Admin Only)
    │
    └─► 🚪 LOGOUT
        (Back to Login)
```

---

## 🏗️ Arsitektur MVC

```
┌─────────────────────────────────────────────────┐
│          APLIKASI DESKTOP MVC                   │
├─────────────────────────────────────────────────┤
│                                                  │
│ ┌──────────┐  ┌──────────────┐  ┌────────────┐ │
│ │  MODEL   │  │  CONTROLLER  │  │   VIEW     │ │
│ ├──────────┤  ├──────────────┤  ├────────────┤ │
│ │ User     │  │ BioData      │  │ LoginView  │ │
│ │ Absensi  │◄→│ Controller   │◄→│ Dashboard  │ │
│ │          │  │              │  │ AbsensiV   │ │
│ └──────────┘  └──────────────┘  └────────────┘ │
│       │              │                │         │
│       └──────────────┼────────────────┘         │
│                      │                          │
│              ┌───────▼────────┐                 │
│              │   DATABASE     │                 │
│              │  absensi.db    │                 │
│              └────────────────┘                 │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Teknologi | Fungsi |
|-----------|--------|
| **Python 3.7+** | Bahasa pemrograman |
| **Tkinter** | GUI Framework (built-in) |
| **SQLite3** | Database (built-in) |
| **Pillow** | Image processing |

---

## 📋 File-File Penting

| File | Lokasi | Deskripsi |
|------|--------|-----------|
| `main.py` | `/pertemuan-2/` | Entry point aplikasi |
| `test.py` | `/pertemuan-2/` | Sanity check environment |
| `database.py` | `/pertemuan-2/databases/` | Database setup & operations |
| `biodata_controller.py` | `/pertemuan-2/controllers/` | Main application controller |
| `absensi.db` | `/pertemuan-2/databases/` | SQLite database file |

---

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'PIL'`
```bash
pip install pillow
```

### Error: `ModuleNotFoundError: No module named 'tkinter'`
```bash
# Windows
pip install tk

# Linux
sudo apt-get install python3-tk

# macOS
brew install python-tk@3.9
```

### Error: `Database is locked`
- Tutup aplikasi yang sedang mengakses database
- Hapus file `absensi.db` dan jalankan `database.py` lagi

### Error: `Permission denied`
- Jalankan di folder dengan write permission
- Cek hak akses folder project

---

## 📝 Catatan Developer

- Database otomatis dibuat saat `database.py` pertama kali dijalankan
- Setiap user hanya bisa punya 1 record absensi per hari
- Admin memiliki akses penuh, mahasiswa hanya bisa view data mereka
- Password tersimpan sebagai plain text (untuk development saja!)

---

## 🔗 Struktur Lengkap pertemuan-2

```
pertemuan-2/
├── databases/
│   ├── database.py          # Setup & operasi database
│   └── absensi.db           # SQLite database file
│
├── controllers/
│   └── biodata_controller.py  # Main controller app
│
├── models/
│   ├── user_model.py        # User data operations
│   └── absensi_model.py     # Attendance data operations
│
├── views/
│   ├── login_view.py        # Login screen
│   ├── dashboard_view.py    # Main dashboard
│   ├── absensi_view.py      # Attendance checkin
│   ├── biodata_db_view.py   # View biodata
│   ├── riwayat_view.py      # History attendance
│   ├── edit_biodata_view.py # Edit biodata (admin)
│   └── register_view.py     # Registration screen
│
├── main.py                  # Application entry point
├── test.py                  # Environment test
└── README.md                # Documentation
```

---

## 📖 Dokumentasi Lengkap

Untuk penjelasan detail tentang setiap folder, silakan lihat:
👉 [`pertemuan-2/README.md`](./pertemuan-2/README.md)

---

## 🎓 Pembelajaran Konsep

Dari project ini, Anda belajar:

✅ **GUI Programming** - Tkinter widgets & layouts  
✅ **Database** - SQLite, queries, migrations  
✅ **OOP** - Classes, models, controllers  
✅ **Design Patterns** - MVC architecture  
✅ **Event Handling** - User interactions  
✅ **Session Management** - User authentication  

---

**Last Updated:** 2026-06-24  
**Version:** 1.0  
**Status:** Development 🚀
