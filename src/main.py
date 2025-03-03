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
# Labels
file_explorer = ttk.Label(root, text="Explore files (For the best experience, use files with maximal resolution 600x600)")
label1 = ttk.Label(root, text="How do you want to watermark your photo?")
# Buttons
exit_btn = ttk.Button(root, text="Quit", command=root.destroy)
browse_btn = ttk.Button(root, text="Browse Folder", command=lambda: browse_files(file_explorer, canvas, img_container))
# Radio Buttons
radio_btn1 = ttk.Radiobutton(root, text="Using text", value='txt')
radio_btn2 = ttk.Radiobutton(root, text="Using image", value='img')


# Setting up elements on grid
file_explorer.pack()
exit_btn.pack()
browse_btn.pack()
label1.pack()
radio_btn2.pack()
radio_btn1.pack()

# Canvas setup
canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()
root.update()

# Running window
root.mainloop()
