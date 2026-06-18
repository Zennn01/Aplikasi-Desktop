import sqlite3
import tkinter as tk
from tkinter import messagebox

from PIL import Image


# Inisialisasi jendela utama
root = tk.Tk()
root.title("Sanity Check - Sistem Absensi")
root.geometry("400x200")


def cek_sistem():
    messagebox.showinfo(
        "Sukses",
        "Environment Python, Tkinter, SQLite3 & Pillow siap!",
    )


btn_test = tk.Button(
    root,
    text="Uji Kesiapan Tools",
    command=cek_sistem,
    padx=10,
    pady=10,
)
btn_test.pack(expand=True)


# Menjaga aplikasi tetap berjalan
root.mainloop()
