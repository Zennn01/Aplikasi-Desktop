import tkinter as tk
from tkinter import messagebox

from views.window_utils import center_window


class EditBiodataView:
    def __init__(self, root, biodata, on_save, on_back):
        self.root = root
        self.biodata = biodata
        self.on_save = on_save
        self.on_back = on_back
        self.frame = None
        self.vars = {}

    def show(self):
        self.root.title("Edit Biodata")
        center_window(self.root, 560, 620)
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=28, pady=20)
        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)
        tk.Label(card, text="Edit Biodata Saya", bg="white", fg="#0f172a", font=("Arial", 18, "bold")).pack(pady=(20, 12))
        form = tk.Frame(card, bg="white")
        form.pack(fill="both", expand=True, padx=30)
        for key in ("nama", "alamat", "nim", "kelas", "jurusan", "email", "telepon", "hobi"):
            self.vars[key] = tk.StringVar(value=self.biodata[key] or "")
            label = key.replace("_", " ").title()
            tk.Label(form, text=label, bg="white", fg="#334155", font=("Arial", 9, "bold"), anchor="w").pack(fill="x", pady=(0, 3))
            tk.Entry(form, textvariable=self.vars[key], font=("Arial", 10), relief="solid", bd=1).pack(fill="x", ipady=6, pady=(0, 8))
        tk.Button(form, text="Simpan", command=self._save, bg="#2563eb", fg="white", relief="flat", font=("Arial", 10, "bold"), cursor="hand2").pack(fill="x", ipady=8, pady=(4, 8))
        tk.Button(form, text="Kembali", command=self.on_back, bg="white", fg="#2563eb", relief="flat", font=("Arial", 10, "underline"), cursor="hand2").pack()

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Edit Biodata Gagal", message)

    def show_success(self, message):
        messagebox.showinfo("Edit Biodata Berhasil", message)

    def _save(self):
        self.on_save({key: var.get().strip() for key, var in self.vars.items()})
