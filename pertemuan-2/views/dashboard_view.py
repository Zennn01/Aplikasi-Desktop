import tkinter as tk


class DashboardView:
    def __init__(self, root, user, today_absensi, handlers):
        self.root = root
        self.user = user
        self.today_absensi = today_absensi
        self.handlers = handlers
        self.frame = None

    def show(self):
        self.root.title("Dashboard Absensi")
        self.root.geometry("560x480")
        self.root.configure(bg="#eef2f7")
        self.frame = tk.Frame(self.root, bg="#eef2f7")
        self.frame.pack(fill="both", expand=True, padx=30, pady=30)
        card = tk.Frame(self.frame, bg="white", highlightbackground="#d9e2ec", highlightthickness=1)
        card.pack(fill="both", expand=True)

        tk.Label(card, text=f"Halo, {self.user['nama']}", bg="white", fg="#0f172a", font=("Arial", 20, "bold")).pack(pady=(32, 8))
        info = "Belum absen hari ini"
        if self.today_absensi:
            info = f"Hari ini: {self.today_absensi['status']} pukul {self.today_absensi['jam_masuk']}"
        tk.Label(card, text=info, bg="white", fg="#64748b", font=("Arial", 11)).pack(pady=(0, 24))

        self._button(card, "Absensi", self.handlers["absensi"], "#2563eb")
        self._button(card, "Biodata", self.handlers["biodata"], "#0f766e")
        self._button(card, "Riwayat Absensi", self.handlers["riwayat"], "#7c3aed")
        if self.user["role"] == "admin":
            self._button(card, "Edit Biodata Pengguna", self.handlers["edit_biodata"], "#ea580c")
        self._button(card, "Logout", self.handlers["logout"], "#dc2626")

    def destroy(self):
        if self.frame:
            self.frame.destroy()

    def _button(self, parent, text, command, bg):
        tk.Button(parent, text=text, command=command, bg=bg, fg="white", relief="flat", font=("Arial", 11, "bold"), cursor="hand2").pack(fill="x", padx=70, ipady=8, pady=6)
