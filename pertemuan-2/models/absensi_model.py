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
