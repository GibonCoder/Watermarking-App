import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from file_actions import browse_files

# TODO: Write functionality for displaying selected image
# TODO: Write functionality to select the way how to watermark image
# TODO: Write functionality to add watermark
# TODO: Write functionality to display watermarked image
# TODO: Write functionality to download watermarked image


# Window initialisation and setup
root = tk.Tk()
root.title("Watermark Your Images!")
root.geometry("600x600")
# root.resizable(False, False)
# Frame setup
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# Canvas setup
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

# Elements Initialisation
exit_btn = ttk.Button(root, text="Quit", command=root.destroy)
file_explorer = ttk.Label(root, text="Explore files")
browse_btn = ttk.Button(root, text="Browse Folder", command=lambda: browse_files(file_explorer, canvas))
# Setting up elements on grid
file_explorer.pack()
exit_btn.pack()
browse_btn.pack()
# Running window
root.mainloop()
