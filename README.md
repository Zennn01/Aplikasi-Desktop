# 📋 Aplikasi Desktop — Biodata & Absensi

Repositori berisi aplikasi desktop untuk manajemen biodata (profil pengguna) dan absensi menggunakan Python (Tkinter) & SQLite. Dokumentasi ini menyelaraskan istilah sehingga "Biodata" dan "Absensi" dijelaskan bersama — controller utama dinamai `BioDataController` karena menangani keduanya.

---

## 📂 Struktur Project (root)

```
Aplikasi-Desktop/
├── Pertemuan-1/          # Versi 1 (folder kapital P)
├── pertemuan-2/          # Versi 2 (folder lowercase)
│   └── README.md         # Dokumentasi detil versi 2
└── README.md             # File ini (ringkasan & quick start)
```

---

## 🎯 Ringkasan Fitur

Project ini menggabungkan dua fitur utama:
- Biodata: pengelolaan profil pengguna (nama, alamat, NIM, dsb.)
- Absensi: pencatatan kehadiran (jam masuk/pulang, status, riwayat)

Kedua fitur dihubungkan oleh controller utama `BioDataController` yang melakukan navigasi antar view dan memanggil model untuk operasi database.

---

## 📁 Penjelasan singkat per folder

- Pertemuan-1/ — Versi awal (simple)
  - main.py — entry point versi 1
  - test.py — sanity check
  - controllers/, models/, views/, databases/ — struktur aplikasi

- pertemuan-2/ — Versi perbaikan (rekomendasi gunakan ini)
  - main.py — entry point versi 2
  - test.py — sanity check
  - controllers/
    - biodata_controller.py — controller utama (mengelola Biodata & Absensi)
  - databases/
    - database.py — init & migrasi SQLite
    - absensi.db — file database (jika ada)
  - models/, views/ — operasi data & layar GUI

> Catatan: Nama controller berisi "biodata" karena class yang mengatur alur diberi nama `BioDataController` meskipun fungsionalitasnya juga mencakup absensi.

---

## 🚀 Quick start (jalankan aplikasi)

1. Clone repo:
```bash
git clone https://github.com/Zennn01/Aplikasi-Desktop.git
cd Aplikasi-Desktop
```

2. Install dependency (Pillow):
```bash
pip install pillow
```

3. Inisialisasi database (gunakan folder yang diinginkan):
```bash
# Versi 2 (direkomendasikan)
cd pertemuan-2
python databases/database.py
```

4. Jalankan aplikasi:
```bash
python main.py
```

5. Jalankan sanity check:
```bash
python test.py
```

---

## 👥 Akun demo (data seed)

- Admin: `admin` / `123456`
- Mahasiswa 1: `mahasiswa1` / `123456`
- Mahasiswa 2: `mahasiswa2` / `123456`

---

## 🛠 Troubleshooting singkat

- ModuleNotFoundError: No module named 'PIL' → pip install pillow
- ModuleNotFoundError: No module named 'tkinter' → pasang paket tkinter sesuai OS
- Database is locked → tutup proses lain yang mengakses file database

---

## 🔗 Dokumentasi detil

Untuk dokumentasi dan penjelasan per-file yang lebih lengkap, buka:
- pertemuan-2/README.md — dokumentasi lengkap versi 2 (rekomendasi)

---

## 📌 Catatan developer

- `BioDataController` menangani navigasi dan logika untuk biodata serta absensi.
- Database default dan akun seed dibuat oleh `databases/database.py`.
- Password disimpan plain-text untuk keperluan development; jangan dipakai di produksi.

---

**Last Updated:** 2026-06-24
