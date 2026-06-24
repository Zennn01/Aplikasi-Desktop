import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class EditAbsensiView:
    def __init__(self, root, record, on_save, on_back):
        self.root = root
        self.record = record
        self.on_save = on_save
        self.on_back = on_back
        self.frame = None
        self.status_var = tk.StringVar()
        self.keterangan_var = tk.StringVar()

    def show(self):
        self.root.title("Edit Validasi Absensi")
        self.root.geometry("560x520")
        self.root.minsize(460, 420)
        self.root.resizable(True, True)
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=28, pady=24)

        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)

        header = tk.Frame(card, bg="white")
        header.pack(fill="x", padx=30, pady=(18, 8))
        tk.Label(
            header,
            text="Edit Validasi Absensi",
            bg="white",
            fg="#0f172a",
            font=("Arial", 18, "bold"),
        ).pack(anchor="w")
        tk.Label(
            header,
            text=f"{self.record['nama']} ({self.record['username']}) - {self.record['tanggal']}",
            bg="white",
            fg="#64748b",
            font=("Arial", 10),
        ).pack(anchor="w", pady=(4, 0))

        canvas = tk.Canvas(card, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(card, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True, padx=(30, 0), pady=(0, 18))

        form = tk.Frame(canvas, bg="white")
        form_window = canvas.create_window((0, 0), window=form, anchor="nw")

        form.bind(
            "<Configure>",
            lambda _event: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(form_window, width=event.width),
        )
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        canvas.bind_all("<Button-4>", lambda _event: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda _event: canvas.yview_scroll(1, "units"))

        current_status = self.record["status"] or "hadir"
        if current_status == "-":
            current_status = "hadir"
        self.status_var.set(current_status)
        self.keterangan_var.set(self.record["keterangan"] or "")

        self._label_value(form, "Nama", self.record["nama"] or "-")
        self._label_value(form, "Username", self.record["username"] or "-")
        self._label_value(form, "Tanggal", self.record["tanggal"] or "-")

        tk.Label(form, text="Status", bg="white", fg="#334155", font=("Arial", 9, "bold"), anchor="w").pack(fill="x", pady=(8, 3))
        ttk.Combobox(
            form,
            textvariable=self.status_var,
            values=("hadir", "izin", "sakit", "alfa"),
            state="readonly",
        ).pack(fill="x", ipady=4, pady=(0, 10))

        tk.Label(form, text="Keterangan", bg="white", fg="#334155", font=("Arial", 9, "bold"), anchor="w").pack(fill="x", pady=(0, 3))
        tk.Entry(form, textvariable=self.keterangan_var, font=("Arial", 10), relief="solid", bd=1).pack(fill="x", ipady=6, pady=(0, 14))

        tk.Button(
            form,
            text="Simpan",
            command=self._save,
            bg="#2563eb",
            fg="white",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
        ).pack(fill="x", ipady=8, pady=(0, 8))
        tk.Button(
            form,
            text="Kembali",
            command=self.on_back,
            bg="white",
            fg="#2563eb",
            relief="flat",
            font=("Arial", 10, "underline"),
            cursor="hand2",
        ).pack()

    def destroy(self):
        self.root.unbind_all("<MouseWheel>")
        self.root.unbind_all("<Button-4>")
        self.root.unbind_all("<Button-5>")
        if self.frame:
            self.frame.destroy()

    def show_error(self, message):
        messagebox.showerror("Edit Absensi Gagal", message)

    def show_success(self, message):
        messagebox.showinfo("Edit Absensi Berhasil", message)

    def _label_value(self, parent, label, value):
        tk.Label(parent, text=label, bg="white", fg="#334155", font=("Arial", 9, "bold"), anchor="w").pack(fill="x", pady=(0, 3))
        tk.Label(parent, text=value, bg="#f8fafc", fg="#0f172a", font=("Arial", 10), anchor="w", padx=10, pady=7).pack(fill="x", pady=(0, 8))

    def _save(self):
        self.on_save(
            {
                "status": self.status_var.get().strip(),
                "keterangan": self.keterangan_var.get().strip(),
            }
        )
