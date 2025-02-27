import tkinter as tk
from tkinter import ttk


class Interface:
    def __init__(self):
        self._root = tk.Tk()

    def setup_window(self):
        # Window Setup
        self._root.title("Watermark Your Images!")
        self._root.geometry("800x800")
        self._root.resizable(False, False)
        # Frame Setup
        frm = ttk.Frame(self._root, padding=10)
        frm.grid()
        # Elements Setup
        ttk.Label(frm, text="Select Image:").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self._root.destroy).grid(column=1, row=0)
        self._root.mainloop()
