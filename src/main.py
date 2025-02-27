import tkinter as tk
from tkinter import ttk

# Window initialisation and setup
root = tk.Tk()
root.title("Watermark Your Images!")
root.geometry("600x600")
root.resizable(False, False)
# Frame setup
frm = ttk.Frame(root, padding=10)
frm.grid()
# Elements Initialisation
exit_btn = ttk.Button(frm, text="Quit", command=root.destroy)
# Setting up elements on grid
exit_btn.grid(column=0, row=0)

# Running window
root.mainloop()
