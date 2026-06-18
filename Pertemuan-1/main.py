import tkinter as tk

from controllers.biodata_controller import BioDataController


def main():
    root = tk.Tk()
    app = BioDataController(root)
    app.run()


if __name__ == "__main__":
    main()
