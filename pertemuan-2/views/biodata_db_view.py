import tkinter as tk
from tkinter import messagebox

from views.window_utils import center_window


class BiodataDbView:
    def __init__(self, root, biodata, on_back):
        self.root = root
        self.biodata = biodata
        self.on_back = on_back
        self.frame = None

    def show(self):
        self.root.title("Biodata")
        center_window(self.root, 560, 620)
        self.root.minsize(460, 420)
        self.root.resizable(True, True)
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=28, pady=28)
        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)

        header = tk.Frame(card, bg="#2563eb")
        header.pack(fill="x")
        tk.Button(
            header,
            text="← Kembali ke Dashboard",
            command=self.on_back,
            bg="#1d4ed8",
            fg="white",
            activebackground="#1e40af",
            activeforeground="white",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        ).pack(anchor="w", padx=14, pady=(12, 0))
        tk.Label(header, text=self.biodata["nama"], bg="#2563eb", fg="white", font=("Arial", 20, "bold"), pady=18).pack(fill="x")

        content = tk.Frame(card, bg="white")
        content.pack(fill="both", expand=True, padx=32, pady=(18, 12))
        for label, key in [
            ("Username", "username"), ("Role", "role"), ("Nama", "nama"),
            ("Alamat", "alamat"), ("NIM", "nim"), ("Kelas", "kelas"),
            ("Jurusan", "jurusan"), ("Email", "email"), ("Telepon", "telepon"),
            ("Hobi", "hobi"),
        ]:
            value = self.biodata[key] or "-"
            self._row(content, label, value)
        tk.Button(card, text="Kembali ke Dashboard", command=self.on_back, bg="#2563eb", fg="white", relief="flat", font=("Arial", 10, "bold"), cursor="hand2").pack(fill="x", padx=40, ipady=8, pady=(0, 16))

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Biodata", message)

    def _row(self, parent, label, value):
        row = tk.Frame(parent, bg="white")
        row.pack(fill="x", pady=5)
        tk.Label(row, text=label, bg="white", fg="#64748b", font=("Arial", 9, "bold"), width=12, anchor="w").pack(side="left")
        tk.Label(row, text=value, bg="#f8fafc", fg="#0f172a", font=("Arial", 10), anchor="w", padx=10, pady=7, wraplength=320).pack(side="left", fill="x", expand=True)
