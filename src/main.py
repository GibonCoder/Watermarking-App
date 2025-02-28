import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# TODO: Write functionality for displaying selected image
# TODO: Write functionality to select the way how to watermark image
# TODO: Write functionality to add watermark
# TODO: Write functionality to display watermarked image
# TODO: Write functionality to download watermarked image


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
file_explorer = ttk.Label(frm, text="Explore files")
browse_btn = ttk.Button(frm, text="Browse Folder", command=browse)
# Setting up elements on grid
file_explorer.grid(column=0, row=0)
exit_btn.grid(column=0, row=1)
browse_btn.grid(column=1, row=1)

# Running window
root.mainloop()
