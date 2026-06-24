import sqlite3
from datetime import datetime

from databases.database import get_connection


class AbsensiModel:
    """Model untuk operasi data absensi."""

    VALID_STATUS = {"hadir", "izin", "sakit", "alfa"}

    def absen_masuk(self, user_id, status="hadir", keterangan=""):
        """Catat absen masuk pengguna untuk tanggal hari ini."""
        if not user_id:
            raise ValueError("ID pengguna wajib diisi")

        status = (status or "hadir").strip().lower()
        if status not in self.VALID_STATUS:
            raise ValueError("Status absensi tidak valid")

        now = datetime.now()
        tanggal = now.date().isoformat()
        jam_masuk = now.time().replace(microsecond=0).isoformat()

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO absensi (
                        user_id, tanggal, jam_masuk, status, keterangan
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        user_id,
                        tanggal,
                        jam_masuk,
                        status,
                        (keterangan or "").strip(),
                    ),
                )
                return cursor.lastrowid
        except sqlite3.IntegrityError as error:
            raise ValueError("Pengguna sudah absen pada tanggal ini") from error

    def absen_pulang(self, user_id):
        """
        Pertahankan kompatibilitas model lama.

        Berdasarkan keputusan Tahap 1, fitur jam pulang tidak dipakai.
        """
        raise NotImplementedError("Fitur jam pulang tidak dipakai")

    def get_absensi_hari_ini(self, user_id):
        """Ambil absensi pengguna untuk tanggal hari ini."""
        tanggal = datetime.now().date().isoformat()
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT *
                FROM absensi
                WHERE user_id = ? AND tanggal = ?
                """,
                (user_id, tanggal),
            )
            return cursor.fetchone()

    def get_riwayat_by_user(self, user_id):
        """Ambil riwayat absensi milik satu pengguna dari tanggal terbaru."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, tanggal, jam_masuk, jam_pulang, status,
                       keterangan, created_at
                FROM absensi
                WHERE user_id = ?
                ORDER BY tanggal DESC, jam_masuk DESC
                """,
                (user_id,),
            )
            return cursor.fetchall()

    def get_rekap_mahasiswa(self, tanggal=None):
        """Ambil rekap absensi mahasiswa untuk tanggal tertentu."""
        tanggal = tanggal or datetime.now().date().isoformat()
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    u.id AS user_id,
                    u.username,
                    u.nama,
                    a.id AS absensi_id,
                    ? AS tanggal,
                    a.jam_masuk,
                    a.status,
                    a.keterangan
                FROM users u
                LEFT JOIN absensi a
                    ON a.user_id = u.id AND a.tanggal = ?
                WHERE u.role = 'mahasiswa'
                ORDER BY u.nama ASC, u.username ASC
                """,
                (tanggal, tanggal),
            )
            return cursor.fetchall()

    def get_absensi_by_user_and_date(self, user_id, tanggal):
        """Ambil absensi satu pengguna pada tanggal tertentu."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT *
                FROM absensi
                WHERE user_id = ? AND tanggal = ?
                """,
                (user_id, tanggal),
            )
            return cursor.fetchone()

    def save_validasi_absensi(self, user_id, tanggal, status, keterangan="", jam_masuk=None):
        """Simpan atau perbarui absensi untuk keperluan validasi admin."""
        if not user_id:
            raise ValueError("ID pengguna wajib diisi")
        if not tanggal:
            raise ValueError("Tanggal wajib diisi")

        status = (status or "").strip().lower()
        if status not in self.VALID_STATUS:
            raise ValueError("Status absensi tidak valid")

        current = self.get_absensi_by_user_and_date(user_id, tanggal)
        jam_masuk_value = jam_masuk
        if jam_masuk_value is None and current and current["jam_masuk"]:
            jam_masuk_value = current["jam_masuk"]
        if jam_masuk_value is None:
            jam_masuk_value = datetime.now().time().replace(microsecond=0).isoformat()

        with get_connection() as conn:
            cursor = conn.cursor()
            if current:
                cursor.execute(
                    """
                    UPDATE absensi
                    SET jam_masuk = ?, status = ?, keterangan = ?
                    WHERE id = ?
                    """,
                    (
                        jam_masuk_value,
                        status,
                        (keterangan or "").strip(),
                        current["id"],
                    ),
                )
                return current["id"]

            cursor.execute(
                """
                INSERT INTO absensi (user_id, tanggal, jam_masuk, status, keterangan)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    tanggal,
                    jam_masuk_value,
                    status,
                    (keterangan or "").strip(),
                ),
            )
            return cursor.lastrowid
