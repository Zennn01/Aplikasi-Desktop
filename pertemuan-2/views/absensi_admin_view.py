import tkinter as tk
from tkinter import ttk


class AbsensiAdminView:
    def __init__(self, root, absensi_rows, on_edit, on_back):
        self.root = root
        self.absensi_rows = absensi_rows
        self.on_edit = on_edit
        self.on_back = on_back
        self.frame = None
        self.tree = None

    def show(self):
        self.root.title("Absensi Mahasiswa")
        self.root.geometry("960x540")
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=24, pady=24)

        tk.Label(
            self.frame,
            text="Absensi Mahasiswa",
            bg="#eef2f7",
            fg="#0f172a",
            font=("Arial", 18, "bold"),
        ).pack(pady=(0, 8))
        tk.Label(
            self.frame,
            text="Status '-' berarti mahasiswa belum absen pada tanggal ini.",
            bg="#eef2f7",
            fg="#64748b",
            font=("Arial", 10),
        ).pack(pady=(0, 12))

        table_wrap = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        table_wrap.pack(fill="both", expand=True)

        columns = ("nama", "username", "tanggal", "jam_masuk", "status", "keterangan")
        self.tree = ttk.Treeview(table_wrap, columns=columns, show="headings", height=15)
        for col, title, width in [
            ("nama", "Nama", 180),
            ("username", "Username", 120),
            ("tanggal", "Tanggal", 120),
            ("jam_masuk", "Jam Masuk", 120),
            ("status", "Status", 100),
            ("keterangan", "Keterangan", 280),
        ]:
            self.tree.heading(col, text=title)
            self.tree.column(col, width=width, anchor="w")
        self.tree.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(table_wrap, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        for item in self.absensi_rows:
            self.tree.insert(
                "",
                "end",
                iid=str(item["user_id"]),
                values=(
                    item["nama"],
                    item["username"],
                    item["tanggal"] or "-",
                    item["jam_masuk"] or "-",
                    item["status"] or "-",
                    item["keterangan"] or "-",
                ),
            )

        footer = tk.Frame(self.frame, bg="#eef2f7")
        footer.pack(fill="x", pady=(12, 0))
        tk.Button(
            footer,
            text="Edit Validasi",
            command=self._handle_edit,
            bg="#ea580c",
            fg="white",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        ).pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 8))
        tk.Button(
            footer,
            text="Kembali ke Dashboard",
            command=self.on_back,
            bg="#2563eb",
            fg="white",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        ).pack(side="left", fill="x", expand=True, ipady=8)

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        from tkinter import messagebox

        messagebox.showerror("Absensi", message)

    def show_success(self, message):
        from tkinter import messagebox

        messagebox.showinfo("Absensi", message)

    def get_selected_record(self):
        if not self.tree:
            return None
        selected = self.tree.selection()
        if not selected:
            return None
        user_id = int(selected[0])
        for row in self.absensi_rows:
            if row["user_id"] == user_id:
                return row
        return None

    def _handle_edit(self):
        record = self.get_selected_record()
        if not record:
            self.show_error("Pilih satu mahasiswa terlebih dahulu")
            return
        self.on_edit(record)
