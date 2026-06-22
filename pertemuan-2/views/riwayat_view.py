import tkinter as tk
from tkinter import ttk


class RiwayatView:
    def __init__(self, root, riwayat, on_back):
        self.root = root
        self.riwayat = riwayat
        self.on_back = on_back
        self.frame = None

    def show(self):
        self.root.title("Riwayat Absensi")
        self.root.geometry("760x480")
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=24, pady=24)
        tk.Label(self.frame, text="Riwayat Absensi", bg="#eef2f7", fg="#0f172a", font=("Arial", 18, "bold")).pack(pady=(0, 12))
        columns = ("tanggal", "jam_masuk", "status", "keterangan")
        tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=14)
        for col, title, width in [("tanggal", "Tanggal", 130), ("jam_masuk", "Jam Masuk", 130), ("status", "Status", 110), ("keterangan", "Keterangan", 330)]:
            tree.heading(col, text=title)
            tree.column(col, width=width)
        tree.pack(fill="both", expand=True)
        if self.riwayat:
            for item in self.riwayat:
                tree.insert("", "end", values=(item["tanggal"], item["jam_masuk"] or "-", item["status"], item["keterangan"] or "-"))
        else:
            tree.insert("", "end", values=("Belum ada riwayat", "-", "-", "-"))
        tk.Button(self.frame, text="Kembali", command=self.on_back, bg="#2563eb", fg="white", relief="flat", font=("Arial", 10, "bold"), cursor="hand2").pack(fill="x", ipady=8, pady=(12, 0))

    def destroy(self):
        if self.frame:
            self.frame.destroy()
