import tkinter as tk


class BioDataView:
    def __init__(self, root):
        self.root = root
        self.root.title("Biodata Saya")
        self.root.geometry("520x620")
        self.root.configure(bg="#eef2f7")
        self.root.resizable(False, False)

    def show_card(self, biodata):
        wrapper = tk.Frame(self.root, bg="#eef2f7")
        wrapper.pack(fill="both", expand=True, padx=28, pady=28)

        card = tk.Frame(
            wrapper,
            bg="white",
            highlightbackground="#d9e2ec",
            highlightthickness=1,
        )
        card.pack(fill="both", expand=True)

        header = tk.Frame(card, bg="#2563eb", height=150)
        header.pack(fill="x")
        header.pack_propagate(False)

        avatar = tk.Label(
            header,
            text="BD",
            bg="white",
            fg="#2563eb",
            font=("Arial", 24, "bold"),
            width=4,
            height=2,
        )
        avatar.pack(pady=(22, 8))

        title = tk.Label(
            header,
            text=biodata["nama"],
            bg="#2563eb",
            fg="white",
            font=("Arial", 18, "bold"),
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text=f'{biodata["jurusan"]} - {biodata["kelas"]}',
            bg="#2563eb",
            fg="#dbeafe",
            font=("Arial", 11),
        )
        subtitle.pack(pady=(4, 0))

        content = tk.Frame(card, bg="white")
        content.pack(fill="both", expand=True, padx=30, pady=24)

        fields = [
            ("NIM", biodata["nim"]),
            ("Email", biodata["email"]),
            ("Telepon", biodata["telepon"]),
            ("Alamat", biodata["alamat"]),
            ("Hobi", biodata["hobi"]),
        ]

        for label, value in fields:
            self._add_info_row(content, label, value)

        footer = tk.Label(
            card,
            text="Silakan ubah data di models/biodata_model.py",
            bg="white",
            fg="#64748b",
            font=("Arial", 10),
        )
        footer.pack(pady=(0, 20))

    def _add_info_row(self, parent, label, value):
        row = tk.Frame(parent, bg="white")
        row.pack(fill="x", pady=8)

        label_widget = tk.Label(
            row,
            text=label,
            bg="white",
            fg="#64748b",
            font=("Arial", 10, "bold"),
            width=10,
            anchor="w",
        )
        label_widget.pack(side="left")

        value_widget = tk.Label(
            row,
            text=value,
            bg="#f8fafc",
            fg="#0f172a",
            font=("Arial", 11),
            anchor="w",
            padx=12,
            pady=10,
            wraplength=310,
        )
        value_widget.pack(side="left", fill="x", expand=True)
