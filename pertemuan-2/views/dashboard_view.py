import tkinter as tk

from views.window_utils import center_window


class DashboardView:
    def __init__(self, root, user, today_absensi, display_datetime, handlers):
        self.root = root
        self.user = user
        self.today_absensi = today_absensi
        self.display_datetime = display_datetime
        self.handlers = handlers
        self.frame = None
        self.clock_label = None
        self.clock_after_id = None

    def show(self):
        self.root.title("Dashboard Absensi")
        center_window(self.root, 560, 480)
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=30, pady=30)
        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)

        tk.Label(card, text=f"Halo, {self.user['nama']}", bg="white", fg="#0f172a", font=("Arial", 20, "bold")).pack(pady=(32, 8))
        self.clock_label = tk.Label(card, text="", bg="white", fg="#334155", font=("Arial", 12, "bold"))
        self.clock_label.pack(pady=(0, 10))
        self._update_clock()

        if self.user["role"] == "admin":
            info = "Kelola absensi mahasiswa"
        else:
            info = "Belum absen hari ini"
            if self.today_absensi:
                info = f"Hari ini: {self.today_absensi['status']} pukul {self.today_absensi['jam_masuk']}"
        tk.Label(card, text=info, bg="white", fg="#64748b", font=("Arial", 11)).pack(pady=(0, 24))

        if self.user["role"] == "admin":
            self._button(card, "Absensi Mahasiswa", self.handlers["absensi"], "#334155")
            self._button(card, "Edit Biodata Pengguna", self.handlers["edit_biodata"], "#ea580c")
        else:
            self._button(card, "Absensi", self.handlers["absensi"], "#2563eb")
            self._button(card, "Biodata", self.handlers["biodata"], "#0f766e")
            self._button(card, "Riwayat Absensi", self.handlers["riwayat"], "#7c3aed")
        self._button(card, "Logout", self.handlers["logout"], "#dc2626")

    def destroy(self):
        if self.clock_after_id:
            self.root.after_cancel(self.clock_after_id)
            self.clock_after_id = None
        if self.frame:
            self.frame.destroy()

    def _button(self, parent, text, command, bg):
        tk.Button(parent, text=text, command=command, bg=bg, fg="white", relief="flat", font=("Arial", 11, "bold"), cursor="hand2").pack(fill="x", padx=70, ipady=8, pady=6)

    def _update_clock(self):
        if not self.clock_label or not self.clock_label.winfo_exists():
            return
        self.clock_label.configure(text=self.display_datetime())
        self.clock_after_id = self.root.after(1000, self._update_clock)
