from pathlib import Path
import hashlib
import os
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = BASE_DIR / "absensi.db"

USER_COLUMNS = {
    "alamat": "TEXT NOT NULL DEFAULT ''",
    "nim": "TEXT DEFAULT ''",
    "kelas": "TEXT DEFAULT ''",
    "jurusan": "TEXT DEFAULT ''",
    "email": "TEXT DEFAULT ''",
    "telepon": "TEXT DEFAULT ''",
    "hobi": "TEXT DEFAULT ''",
}

ABSENSI_COLUMNS = {
    "jam_pulang": "TIME",
    "keterangan": "TEXT DEFAULT ''",
}


def hash_password(password):
    """Hash password default tanpa bergantung ke model."""
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        120_000,
    )
    return f"pbkdf2_sha256$120000${salt.hex()}${password_hash.hex()}"

def get_connection():
    """Get database connection with consistent settings."""
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def get_table_columns(cursor, table_name):
    """Return existing column names for a trusted table name."""
    cursor.execute(f"PRAGMA table_info({table_name})")
    return {row[1] for row in cursor.fetchall()}


def add_column_if_missing(cursor, table_name, column_name, column_definition):
    """Add a missing column without dropping existing data."""
    columns = get_table_columns(cursor, table_name)
    if column_name not in columns:
        cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_definition}"
        )


def migrate_database(cursor):
    """Apply lightweight migrations while preserving old data."""
    for column_name, column_definition in USER_COLUMNS.items():
        add_column_if_missing(cursor, "users", column_name, column_definition)

    for column_name, column_definition in ABSENSI_COLUMNS.items():
        add_column_if_missing(cursor, "absensi", column_name, column_definition)

    cursor.execute("UPDATE users SET role = ? WHERE role = ?", ("admin", "dosen"))
    cursor.execute(
        """
        UPDATE users
        SET role = ?
        WHERE role NOT IN (?, ?)
        """,
        ("mahasiswa", "mahasiswa", "admin"),
    )

    cursor.execute("UPDATE users SET alamat = ? WHERE alamat IS NULL", ("",))

def init_database():
    """Initialize database with tables and safe migrations."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'mahasiswa',
            nama TEXT NOT NULL,
            alamat TEXT NOT NULL DEFAULT '',
            nim TEXT DEFAULT '',
            kelas TEXT DEFAULT '',
            jurusan TEXT DEFAULT '',
            email TEXT DEFAULT '',
            telepon TEXT DEFAULT '',
            hobi TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create Absensi table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS absensi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tanggal DATE NOT NULL,
            jam_masuk TIME,
            jam_pulang TIME,
            status TEXT DEFAULT 'hadir',
            keterangan TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, tanggal)
        )
    ''')

    migrate_database(cursor)
    
    conn.commit()
    conn.close()

def insert_default_data():
    """Insert default users for local development."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        defaults = [
            ('admin', 'admin', 'Administrator', 'Kampus'),
            ('mahasiswa1', 'mahasiswa', 'Andi Pratama', 'Jakarta'),
            ('mahasiswa2', 'mahasiswa', 'Siti Nurhaliza', 'Bandung'),
        ]
        for username, role, nama, alamat in defaults:
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                cursor.execute(
                    """
                    UPDATE users
                    SET password = ?, role = ?, nama = ?, alamat = ?
                    WHERE username = ?
                    """,
                    (hash_password('123456'), role, nama, alamat, username),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO users (username, password, role, nama, alamat)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (username, hash_password('123456'), role, nama, alamat),
                )

        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

if __name__ == "__main__":
    init_database()
    insert_default_data()
    print("Database initialized successfully!")
