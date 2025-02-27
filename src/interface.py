import tkinter as tk


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Watermark Your Images!")
        self.root.geometry("800x800")
        self.root.resizable(False, False)
        self.root.mainloop()
