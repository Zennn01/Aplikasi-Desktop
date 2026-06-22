from tkinter import messagebox

from models.absensi_model import AbsensiModel
from models.user_model import UserModel
from views.absensi_view import AbsensiView
from views.biodata_db_view import BiodataDbView
from views.dashboard_view import DashboardView
from views.edit_biodata_view import EditBiodataView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.riwayat_view import RiwayatView


class BioDataController:
    """Controller utama untuk session dan navigasi aplikasi."""

    def __init__(self, root):
        self.root = root
        self.user_model = UserModel()
        self.absensi_model = AbsensiModel()
        self.current_user = None
        self.view = None

    def run(self):
        self.show_login()
        self.root.mainloop()

    def require_login(self):
        if self.current_user is None:
            self.show_login()
            return False
        return True

    def refresh_current_user(self):
        if self.current_user is not None:
            self.current_user = self.user_model.find_by_id(self.current_user["id"])

    def show_login(self):
        self.clear_window()
        self.view = LoginView(self.root, self.handle_login, self.show_register)
        self.view.show()

    def handle_login(self, username, password):
        user = self.user_model.verify_login(username, password)
        if not user:
            self.view.show_error("Username atau password salah")
            return
        self.current_user = user
        self.show_dashboard()

    def show_register(self):
        self.clear_window()
        self.view = RegisterView(self.root, self.handle_register, self.show_login)
        self.view.show()

    def handle_register(self, data):
        try:
            self.user_model.register(
                username=data["username"],
                password=data["password"],
                nama=data["nama"],
                alamat=data["alamat"],
                nim=data.get("nim", ""),
                kelas=data.get("kelas", ""),
                jurusan=data.get("jurusan", ""),
                email=data.get("email", ""),
                telepon=data.get("telepon", ""),
                hobi=data.get("hobi", ""),
            )
            self.view.show_success("Registrasi berhasil. Silakan login.")
            self.show_login()
        except ValueError as error:
            self.view.show_error(str(error))

    def show_dashboard(self):
        if not self.require_login():
            return
        self.refresh_current_user()
        self.clear_window()
        today_absensi = self.absensi_model.get_absensi_hari_ini(self.current_user["id"])
        self.view = DashboardView(
            self.root,
            self.current_user,
            today_absensi,
            {
                "absensi": self.show_absensi,
                "biodata": self.show_biodata,
                "riwayat": self.show_riwayat,
                "edit_biodata": self.show_edit_biodata,
                "logout": self.logout,
            },
        )
        self.view.show()

    def show_absensi(self):
        if not self.require_login():
            return
        self.clear_window()
        today_absensi = self.absensi_model.get_absensi_hari_ini(self.current_user["id"])
        self.view = AbsensiView(self.root, today_absensi, self.handle_absen_masuk, self.show_dashboard)
        self.view.show()

    def handle_absen_masuk(self, status, keterangan):
        if not self.require_login():
            return
        try:
            self.absensi_model.absen_masuk(self.current_user["id"], status, keterangan)
            self.view.show_success("Absensi berhasil disimpan")
            self.show_absensi()
        except ValueError as error:
            self.view.show_error(str(error))

    def show_biodata(self):
        if not self.require_login():
            return
        biodata = self.user_model.get_biodata(self.current_user["id"])
        if not biodata:
            messagebox.showerror("Biodata", "Biodata pengguna tidak ditemukan")
            self.show_dashboard()
            return
        self.clear_window()
        self.view = BiodataDbView(self.root, biodata, self.show_dashboard)
        self.view.show()

    def show_riwayat(self):
        if not self.require_login():
            return
        riwayat = self.absensi_model.get_riwayat_by_user(self.current_user["id"])
        self.clear_window()
        self.view = RiwayatView(self.root, riwayat, self.show_dashboard)
        self.view.show()

    def show_edit_biodata(self):
        if not self.require_login():
            return
        if self.current_user["role"] != "admin":
            messagebox.showerror("Akses Ditolak", "Hanya admin yang boleh mengedit biodata")
            self.show_dashboard()
            return
        biodata = self.user_model.get_biodata(self.current_user["id"])
        self.clear_window()
        self.view = EditBiodataView(self.root, biodata, self.handle_update_biodata, self.show_dashboard)
        self.view.show()

    def handle_update_biodata(self, data):
        if not self.require_login():
            return
        try:
            self.user_model.update_biodata(self.current_user["id"], **data)
            self.refresh_current_user()
            self.view.show_success("Biodata berhasil diperbarui")
            self.show_dashboard()
        except ValueError as error:
            self.view.show_error(str(error))

    def logout(self):
        self.current_user = None
        self.show_login()

    def clear_window(self):
        if self.view and hasattr(self.view, "destroy"):
            self.view.destroy()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.view = None
