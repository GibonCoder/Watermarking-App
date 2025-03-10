import tkinter as tk
from tkinter import ttk
from file_actions import browse_files, add_watermark

# Window initialisation and setup
root = tk.Tk()
root.title("Watermark Your Images!")
root.geometry("800x800")
# root.resizable(False, False)

# Variables
input_text = tk.StringVar(root)
option_var = tk.StringVar(root)


def choose_option():
    radio_btn_val = option_var.get()
    if radio_btn_val == 'txt':
        watermark_txt.configure(state='normal')
        watermark_txt.update()
        watermark_container.append(0)

        paths_container.append(None)

        browse_watermarks_btn.configure(state='disabled')
        browse_watermarks_btn.update()
    else:
        watermark_txt.configure(state='disabled')
        watermark_txt.update()

        if None in paths_container:
            paths_container.remove(None)

        browse_watermarks_btn.configure(state='normal')
        browse_watermarks_btn.update()

# TODO: Write functionality to add watermark
# TODO: Write functionality to display watermarked image
# TODO: Write functionality to download watermarked image


img_container = []  # List to hold image references
paths_container = []
watermark_container = []  # List to hold watermark reference
# Elements Initialisation
# Labels
file_explorer = ttk.Label(root, text="Explore files (For the best experience, use files with maximal resolution 600x600)")
label1 = ttk.Label(root, text="How do you want to watermark your photo?")
# Buttons
exit_btn = ttk.Button(root, text="Quit", command=root.destroy)
browse_files_btn = ttk.Button(root, text="Browse Files", command=lambda: browse_files(img_container, canvas=canvas, label=file_explorer, paths_container=paths_container))
browse_watermarks_btn = ttk.Button(root, text="Browse watermarks", command=lambda: browse_files(watermark_container, paths_container), state='disabled')
add_watermark_btn = ttk.Button(root, text="Add your watermark", command=lambda: add_watermark(option_var.get(), paths_container[0], paths_container[1], input_text.get()))
# Radio Buttons
radio_btn1 = ttk.Radiobutton(root, text="Using text", variable=option_var, value='txt', command=choose_option)
radio_btn2 = ttk.Radiobutton(root, text="Using image", variable=option_var, value='img', command=choose_option)
# Entries
watermark_txt = ttk.Entry(root, textvariable=input_text, state='disabled')

# Setting up elements on grid
file_explorer.pack()
exit_btn.pack()
browse_files_btn.pack()
label1.pack()
radio_btn2.pack()
browse_watermarks_btn.pack()
radio_btn1.pack()
watermark_txt.pack()
add_watermark_btn.pack()


# Canvas setup
canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()
root.update()

# Running window
root.mainloop()
