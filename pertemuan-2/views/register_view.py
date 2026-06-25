import tkinter as tk
from tkinter import messagebox

from views.window_utils import center_window


class RegisterView:
    """Tampilan halaman register."""

    def __init__(self, root, on_register, on_back):
        self.root = root
        self.on_register = on_register
        self.on_back = on_back
        self.frame = None
        self.vars = {field: tk.StringVar() for field in (
            "username", "password", "confirm_password", "nama", "alamat",
            "nim", "kelas", "jurusan", "email", "telepon", "hobi"
        )}

    def show(self):
        self.root.title("Register Aplikasi Absensi")
        center_window(self.root, 560, 620)
        self.root.minsize(460, 420)
        self.root.configure(bg="#eef2f7")
        self.root.resizable(True, True)

        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=18, pady=16)

        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)

        tk.Label(card, text="Register", bg="white", fg="#0f172a", font=("Arial", 20, "bold")).pack(pady=(20, 4))
        tk.Label(card, text="Buat akun baru untuk absensi", bg="white", fg="#64748b", font=("Arial", 10)).pack(pady=(0, 14))

        canvas = tk.Canvas(card, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(card, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True, padx=(30, 18), pady=(0, 18))

        form = tk.Frame(canvas, bg="white")
        canvas_window = canvas.create_window((0, 0), window=form, anchor="nw")

        form.bind(
            "<Configure>",
            lambda _event: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(canvas_window, width=event.width),
        )
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        canvas.bind_all("<Button-4>", lambda _event: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda _event: canvas.yview_scroll(1, "units"))

        self._entry(form, "Username *", "username")
        self._entry(form, "Password *", "password", show="*")
        self._entry(form, "Konfirmasi Password *", "confirm_password", show="*")
        self._entry(form, "Nama *", "nama")
        self._entry(form, "Alamat *", "alamat")
        self._entry(form, "NIM", "nim")
        self._entry(form, "Kelas", "kelas")
        self._entry(form, "Jurusan", "jurusan")
        self._entry(form, "Email", "email")
        self._entry(form, "Telepon", "telepon")
        self._entry(form, "Hobi", "hobi")

        tk.Button(form, text="Register", command=self._handle_register, bg="#2563eb", fg="white", relief="flat", font=("Arial", 11, "bold"), cursor="hand2").pack(fill="x", ipady=8, pady=(8, 8))
        tk.Button(form, text="Kembali ke Login", command=self.on_back, bg="white", fg="#2563eb", relief="flat", font=("Arial", 10, "underline"), cursor="hand2").pack(pady=(0, 12))

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Register Gagal", message)

    def show_success(self, message):
        messagebox.showinfo("Register Berhasil", message)

    def _entry(self, parent, label, key, show=None):
        tk.Label(parent, text=label, bg="white", fg="#334155", font=("Arial", 9, "bold"), anchor="w").pack(fill="x", pady=(0, 3))
        tk.Entry(parent, textvariable=self.vars[key], show=show, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", ipady=5, pady=(0, 7))

    def _handle_register(self):
        data = {key: var.get().strip() for key, var in self.vars.items()}
        if not data["username"] or not data["password"] or not data["nama"] or not data["alamat"]:
            self.show_error("Username, password, nama, dan alamat wajib diisi")
            return
        if data["password"] != data["confirm_password"]:
            self.show_error("Konfirmasi password tidak sama")
            return
        self.on_register(data)
