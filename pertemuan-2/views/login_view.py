import tkinter as tk
from tkinter import messagebox

from views.window_utils import center_window


class LoginView:
    """Tampilan halaman login."""

    def __init__(self, root, on_login, on_register):
        self.root = root
        self.on_login = on_login
        self.on_register = on_register
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.frame = None

    def show(self):
        self.root.title("Login Aplikasi Absensi")
        center_window(self.root, 420, 420)
        self.root.configure(bg="#eef2f7")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=32, pady=32)

        card = tk.Frame(
            self.frame,
            bg="white",
            highlightbackground="#d9e2ec",
            highlightthickness=1,
        )
        card.pack(fill="both", expand=True)

        title = tk.Label(
            card,
            text="Login Absensi",
            bg="white",
            fg="#0f172a",
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=(32, 6))

        subtitle = tk.Label(
            card,
            text="Masuk menggunakan akun yang terdaftar",
            bg="white",
            fg="#64748b",
            font=("Arial", 10),
        )
        subtitle.pack(pady=(0, 24))

        form = tk.Frame(card, bg="white")
        form.pack(fill="x", padx=32)

        self._add_label(form, "Username")
        username_entry = tk.Entry(
            form,
            textvariable=self.username_var,
            font=("Arial", 11),
            relief="solid",
            bd=1,
        )
        username_entry.pack(fill="x", ipady=8, pady=(0, 14))

        self._add_label(form, "Password")
        password_entry = tk.Entry(
            form,
            textvariable=self.password_var,
            show="*",
            font=("Arial", 11),
            relief="solid",
            bd=1,
        )
        password_entry.pack(fill="x", ipady=8, pady=(0, 20))

        login_button = tk.Button(
            form,
            text="Login",
            command=self._handle_login,
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            font=("Arial", 11, "bold"),
            cursor="hand2",
        )
        login_button.pack(fill="x", ipady=8)

        register_button = tk.Button(
            card,
            text="Belum punya akun? Register",
            command=self.on_register,
            bg="white",
            fg="#2563eb",
            activebackground="white",
            activeforeground="#1d4ed8",
            relief="flat",
            font=("Arial", 10, "underline"),
            cursor="hand2",
        )
        register_button.pack(pady=(18, 0))

        username_entry.focus_set()
        self.root.bind("<Return>", lambda _event: self._handle_login())

    def destroy(self):
        self.root.unbind("<Return>")
        if self.frame is not None:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Login Gagal", message)

    def show_success(self, message):
        messagebox.showinfo("Login Berhasil", message)

    def _add_label(self, parent, text):
        label = tk.Label(
            parent,
            text=text,
            bg="white",
            fg="#334155",
            font=("Arial", 10, "bold"),
            anchor="w",
        )
        label.pack(fill="x", pady=(0, 6))

    def _handle_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get()

        if not username or not password:
            self.show_error("Username dan password wajib diisi")
            return

        self.on_login(username, password)
