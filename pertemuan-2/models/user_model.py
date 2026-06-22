import hashlib
import os
import sqlite3

from databases.database import get_connection


class UserModel:
    """Model untuk operasi data pengguna."""

    VALID_ROLES = {"mahasiswa", "admin"}
    HASH_NAME = "sha256"
    ITERATIONS = 120_000

    def hash_password(self, password):
        """Hash password menggunakan PBKDF2 dan salt acak."""
        if not password:
            raise ValueError("Password wajib diisi")

        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac(
            self.HASH_NAME,
            password.encode("utf-8"),
            salt,
            self.ITERATIONS,
        )
        return (
            f"pbkdf2_{self.HASH_NAME}"
            f"${self.ITERATIONS}"
            f"${salt.hex()}"
            f"${password_hash.hex()}"
        )

    def verify_password_hash(self, password, stored_password):
        """Verifikasi password terhadap hash yang tersimpan."""
        if not password or not stored_password:
            return False

        try:
            algorithm, iterations, salt_hex, hash_hex = stored_password.split("$", 3)
            if algorithm != f"pbkdf2_{self.HASH_NAME}":
                return False

            password_hash = hashlib.pbkdf2_hmac(
                self.HASH_NAME,
                password.encode("utf-8"),
                bytes.fromhex(salt_hex),
                int(iterations),
            )
            return password_hash.hex() == hash_hex
        except (ValueError, TypeError):
            return False

    def find_by_username(self, username):
        """Cari pengguna berdasarkan username."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return cursor.fetchone()

    def find_by_id(self, user_id):
        """Cari pengguna berdasarkan ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cursor.fetchone()

    def register(
        self,
        username,
        password,
        nama,
        alamat,
        role="mahasiswa",
        nim="",
        kelas="",
        jurusan="",
        email="",
        telepon="",
        hobi="",
    ):
        """Daftarkan pengguna baru beserta biodatanya."""
        username = (username or "").strip()
        nama = (nama or "").strip()
        alamat = (alamat or "").strip()
        role = (role or "mahasiswa").strip().lower()

        if not username:
            raise ValueError("Username wajib diisi")
        if not password:
            raise ValueError("Password wajib diisi")
        if not nama:
            raise ValueError("Nama wajib diisi")
        if not alamat:
            raise ValueError("Alamat wajib diisi")
        if role not in self.VALID_ROLES:
            raise ValueError("Role tidak valid")
        if self.find_by_username(username):
            raise ValueError("Username sudah digunakan")

        password_hash = self.hash_password(password)

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO users (
                        username, password, role, nama, alamat, nim, kelas,
                        jurusan, email, telepon, hobi
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        username,
                        password_hash,
                        role,
                        nama,
                        alamat,
                        (nim or "").strip(),
                        (kelas or "").strip(),
                        (jurusan or "").strip(),
                        (email or "").strip(),
                        (telepon or "").strip(),
                        (hobi or "").strip(),
                    ),
                )
                return cursor.lastrowid
        except sqlite3.IntegrityError as error:
            raise ValueError("Username sudah digunakan") from error

    def verify_login(self, username, password):
        """Verifikasi username dan password. Return row user jika berhasil."""
        user = self.find_by_username((username or "").strip())
        if not user:
            return None

        if self.verify_password_hash(password, user["password"]):
            return user

        return None

    def get_biodata(self, user_id):
        """Ambil biodata pengguna berdasarkan ID pengguna."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    id, username, role, nama, alamat, nim, kelas, jurusan,
                    email, telepon, hobi, created_at
                FROM users
                WHERE id = ?
                """,
                (user_id,),
            )
            return cursor.fetchone()

    def update_biodata(
        self,
        user_id,
        nama,
        alamat,
        nim="",
        kelas="",
        jurusan="",
        email="",
        telepon="",
        hobi="",
    ):
        """Update biodata pengguna berdasarkan ID."""
        nama = (nama or "").strip()
        alamat = (alamat or "").strip()

        if not user_id:
            raise ValueError("ID pengguna wajib diisi")
        if not nama:
            raise ValueError("Nama wajib diisi")
        if not alamat:
            raise ValueError("Alamat wajib diisi")

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE users
                SET nama = ?, alamat = ?, nim = ?, kelas = ?, jurusan = ?,
                    email = ?, telepon = ?, hobi = ?
                WHERE id = ?
                """,
                (
                    nama,
                    alamat,
                    (nim or "").strip(),
                    (kelas or "").strip(),
                    (jurusan or "").strip(),
                    (email or "").strip(),
                    (telepon or "").strip(),
                    (hobi or "").strip(),
                    user_id,
                ),
            )
            if cursor.rowcount == 0:
                raise ValueError("Pengguna tidak ditemukan")
            return True
