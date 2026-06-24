import tkinter as tk

from controllers.biodata_controller import BioDataController
from databases.database import init_database, insert_default_data


def main():
    init_database()
    insert_default_data()
    root = tk.Tk()
    app = BioDataController(root)
    app.run()


if __name__ == "__main__":
    main()
