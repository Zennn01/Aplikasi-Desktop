import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class AbsensiView:
    def __init__(self, root, today_absensi, on_absen, on_back):
        self.root = root
        self.today_absensi = today_absensi
        self.on_absen = on_absen
        self.on_back = on_back
        self.frame = None
        self.status_var = tk.StringVar(value="hadir")
        self.keterangan_var = tk.StringVar()
        self.keterangan_label = None
        self.keterangan_entry = None

    def show(self):
        self.root.title("Absensi")
        self.root.geometry("520x460")
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=30, pady=30)
        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)
        tk.Label(card, text="Absensi Hari Ini", bg="white", fg="#0f172a", font=("Arial", 20, "bold")).pack(pady=(30, 8))
        tk.Label(card, text=datetime.now().strftime("%d-%m-%Y %H:%M:%S"), bg="white", fg="#64748b", font=("Arial", 11)).pack(pady=(0, 20))

        if self.today_absensi:
            text = f"Sudah absen: {self.today_absensi['status']} pukul {self.today_absensi['jam_masuk']}"
            tk.Label(card, text=text, bg="#dcfce7", fg="#166534", font=("Arial", 11, "bold"), padx=12, pady=10).pack(fill="x", padx=40, pady=(0, 18))
        else:
            form = tk.Frame(card, bg="white")
            form.pack(fill="x", padx=40)
            tk.Label(form, text="Status", bg="white", fg="#334155", font=("Arial", 10, "bold"), anchor="w").pack(fill="x")
            tk.OptionMenu(form, self.status_var, "hadir", "izin", "sakit", "alfa", command=self._toggle_keterangan).pack(fill="x", pady=(4, 12))
            self.keterangan_label = tk.Label(form, text="Keterangan", bg="white", fg="#334155", font=("Arial", 10, "bold"), anchor="w")
            self.keterangan_entry = tk.Entry(form, textvariable=self.keterangan_var, font=("Arial", 10), relief="solid", bd=1)
            self._toggle_keterangan(self.status_var.get())
            tk.Button(form, text="Absen Masuk", command=self._handle_absen, bg="#2563eb", fg="white", relief="flat", font=("Arial", 11, "bold"), cursor="hand2").pack(fill="x", ipady=8)
        tk.Button(card, text="Kembali", command=self.on_back, bg="white", fg="#2563eb", relief="flat", font=("Arial", 10, "underline"), cursor="hand2").pack(pady=18)

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Absensi Gagal", message)

    def show_success(self, message):
        messagebox.showinfo("Absensi Berhasil", message)

    def _toggle_keterangan(self, status):
        if status in ("izin", "sakit"):
            self.keterangan_label.pack(fill="x")
            self.keterangan_entry.pack(fill="x", ipady=7, pady=(4, 16))
        else:
            self.keterangan_var.set("")
            self.keterangan_label.pack_forget()
            self.keterangan_entry.pack_forget()

    def _handle_absen(self):
        status = self.status_var.get()
        keterangan = self.keterangan_var.get() if status in ("izin", "sakit") else ""
        self.on_absen(status, keterangan)
