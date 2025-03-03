import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from file_actions import browse_files

# TODO: Write functionality for displaying selected image [Finished]
# TODO: Write functionality to select the way how to watermark image
# TODO: Write functionality to add watermark
# TODO: Write functionality to display watermarked image
# TODO: Write functionality to download watermarked image


# Window initialisation and setup
root = tk.Tk()
root.title("Watermark Your Images!")
root.geometry("800x800")
# root.resizable(False, False)

img_container = []  # List to hold image references
# Elements Initialisation
exit_btn = ttk.Button(root, text="Quit", command=root.destroy)
file_explorer = ttk.Label(root, text="Explore files (For the best experience, use files with maximal resolution 600x600)")
browse_btn = ttk.Button(root, text="Browse Folder", command=lambda: browse_files(file_explorer, canvas, img_container))

# Setting up elements on grid
file_explorer.pack()
exit_btn.pack()
browse_btn.pack()

# Canvas setup
canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()
root.update()

# Running window
root.mainloop()
