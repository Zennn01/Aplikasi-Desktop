# 📋 Sistem Absensi Desktop - Pertemuan 2

Aplikasi Desktop untuk manajemen absensi dan biodata mahasiswa/karyawan dengan GUI menggunakan Tkinter dan SQLite.

---

## 📁 Struktur Folder

### 1️⃣ Folder `databases/` - Database Management
Berisi file dan script untuk pengelolaan database SQLite aplikasi.

#### 📄 File dalam folder:
- **`database.py`** - Script utama untuk inisialisasi dan migrasi database
- **`absensi.db`** - File database SQLite (otomatis dibuat saat pertama kali dijalankan)

#### ✨ Fungsi `database.py`:
```
✓ Koneksi database dengan pengaturan optimal
✓ Inisialisasi tabel Users dan Absensi
✓ Migrasi data aman (tanpa menghapus data lama)
✓ Insert data default untuk testing (admin + 2 mahasiswa)
```

#### 📊 Struktur Database:
```
📌 Tabel USERS:
   - id, username, password, role
   - nama, alamat, nim, kelas, jurusan
   - email, telepon, hobi, created_at

📌 Tabel ABSENSI:
   - id, user_id, tanggal, jam_masuk, jam_pulang
   - status, keterangan, created_at
```

---

### 2️⃣ Folder `controllers/` - Business Logic
Berisi controller yang mengelola alur aplikasi dan interaksi antar komponen.

#### 📄 File dalam folder:
- **`biodata_controller.py`** - Controller utama aplikasi

#### 🎮 Fungsi Controller:
```
✓ Manajemen session user (login/logout)
✓ Navigasi antar view (dashboard, absensi, biodata, riwayat)
✓ Handle event dari user (klik tombol, submit form)
✓ Integrasi Model (data) dengan View (tampilan)
✓ Validasi input dan error handling
```

#### 🔄 Alur Aplikasi:
```
1. LOGIN → 2. DASHBOARD → 3. PILIH MENU:
                             ├─ Absensi (Checkin/Checkout)
                             ├─ Biodata (Lihat Data)
                             ├─ Riwayat (Histori Absensi)
                             ├─ Edit Biodata (Admin Only)
                             └─ Logout
```

---

## 🚀 Cara Menjalankan Aplikasi

### 📋 Prasyarat (Prerequisites):
```bash
Python 3.7+
```

### 1️⃣ Setup (Hanya pertama kali):

```bash
# Masuk ke folder pertemuan-2
cd pertemuan-2

# Install dependencies
pip install pillow tkinter sqlite3
```

### 2️⃣ Inisialisasi Database:

```bash
# Jalankan script database untuk membuat & populate database
python databases/database.py

# Output:
# Database initialized successfully!
```

### 3️⃣ Jalankan Aplikasi:

```bash
# Cara 1: Jalankan main.py
python main.py

# Atau Cara 2: Dari parent directory
python -m pertemuan-2.main
```

### 4️⃣ Login Akun Demo:
```
👤 Admin:
   Username: admin
   Password: 123456

👤 Mahasiswa 1:
   Username: mahasiswa1
   Password: 123456

👤 Mahasiswa 2:
   Username: mahasiswa2
   Password: 123456
```

---

## 🎨 User Flow Diagram

```
┌─────────────────────────────────────────────┐
│       SISTEM ABSENSI DESKTOP v1.0            │
└─────────────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │   LOGIN VIEW           │
        │ (Username + Password)  │
        └────────────────────────┘
                     │
         ┌──────────┴──────────┐
         │                     │
      ✓ Valid            ✗ Invalid
         │                     │
         ▼                     ▼
    DASHBOARD         Error Message
        │             (Coba Lagi)
        │                     │
        │                     └─────┘
        │
        ├─► 1. ABSENSI (Checkin/Checkout)
        │   └─► Simpan jam masuk & pulang
        │
        ├─► 2. BIODATA
        │   └─► Lihat info profil lengkap
        │
        ├─► 3. RIWAYAT
        │   └─► Lihat daftar absensi bulan ini
        │
        ├─► 4. EDIT BIODATA (Admin Only)
        │   └─► Update data pribadi
        │
        └─► 5. LOGOUT
            └─► Kembali ke Login
```

---

## 📸 Gambaran Umum Project

### 🎯 Folder 1: `databases/`

**Tujuan:** Mengelola persistent data menggunakan SQLite

**Fitur Utama:**
- ✅ Database berbasis file (absensi.db)
- ✅ Tabel terstruktur untuk users dan absensi
- ✅ Koneksi aman dengan foreign key
- ✅ Migrasi database tanpa data loss
- ✅ Data seed untuk development

**Use Case:**
```
Saat user login:
database.py ← verify username & password ← users table

Saat user absen:
database.py ← insert jam_masuk ← absensi table

Saat view riwayat:
database.py ← query absensi WHERE user_id = X ← absensi table
```

---

### 🎯 Folder 2: `controllers/`

**Tujuan:** Mengontrol logika aplikasi dan navigasi

**Fitur Utama:**
- ✅ Session management (current_user tracking)
- ✅ Route handling (show_login, show_dashboard, dll)
- ✅ Event binding (login, register, absen, logout)
- ✅ Model-View integration
- ✅ Error handling & validation

**Use Case:**
```
User klik "Tombol Absensi" 
    ↓ (View mengirim event ke Controller)
controller.handle_absen_masuk()
    ↓ (Controller memvalidasi)
controller.absensi_model.absen_masuk()
    ↓ (Model mengirim ke Database)
database.py INSERT INTO absensi
    ↓ (Controller refresh view)
controller.show_absensi()
```

---

## 🔧 File Pendukung

| File | Deskripsi |
|------|-----------|
| `main.py` | Entry point aplikasi, menjalankan GUI |
| `test.py` | Sanity check - test apakah semua library terpasang |

---

## 🐛 Testing & Troubleshooting

### Jalankan Test:
```bash
python test.py
```
Akan muncul popup "Sukses" jika semua dependencies siap.

### Common Issues:

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError: No module named 'tkinter'` | `pip install tk` |
| `ModuleNotFoundError: No module named 'PIL'` | `pip install pillow` |
| `Database is locked` | Tutup aplikasi lain yang akses `absensi.db` |
| `Permission denied` | Jalankan di folder dengan write permission |

---

## 📊 Arsitektur MVC

```
┌─────────────────────────────────────────────────────┐
│                  APLIKASI DESKTOP                    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐│
│  │   MODELS     │  │  CONTROLLERS │  │   VIEWS    ││
│  ├──────────────┤  ├──────────────┤  ├────────────┤│
│  │ UserModel    │  │ BioData      │  │ LoginView  ││
│  │ AbsensiModel │  │ Controller   │  │ Dashboard  ││
│  │              │  │              │  │ AbsensiView││
│  │ Database ops │  │ Navigation & │  │ RiwayatView││
│  │              │  │ Session mgmt │  │            ││
│  └──────────────┘  └──────────────┘  └────────────┘│
│         │                 │                  │      │
│         └─────────────────┼──────────────────┘      │
│                           │                          │
│                    ┌──────▼──────┐                  │
│                    │  DATABASE   │                  │
│                    │ absensi.db  │                  │
│                    └─────────────┘                  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## 📝 Catatan Penting

- Database otomatis dibuat saat `database.py` dijalankan
- Default password semua akun demo: `123456`
- Admin bisa mengedit biodata, mahasiswa hanya bisa view
- Setiap absensi per user per hari hanya ada 1 record (unique constraint)

---

## 🔗 Dependencies

- **Tkinter** - GUI Framework (built-in Python)
- **SQLite3** - Database (built-in Python)
- **Pillow** - Image processing
- **pathlib** - Path handling (built-in Python)

---

## 👨‍💻 Developer Notes

Untuk development lebih lanjut, ikuti struktur folder ini:
```
pertemuan-2/
├── databases/
│   ├── __init__.py
│   ├── database.py
│   └── absensi.db
├── controllers/
│   ├── __init__.py
│   └── biodata_controller.py
├── models/         # (to be created)
│   ├── user_model.py
│   └── absensi_model.py
├── views/          # (to be created)
│   ├── login_view.py
│   ├── dashboard_view.py
│   └── ... (other views)
├── main.py
├── test.py
└── README.md
```

---

**Last Updated:** 2026-06-24  
**Version:** 1.0  
**Status:** Development ✨
