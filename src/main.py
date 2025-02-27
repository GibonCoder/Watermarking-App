import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


def browse():
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=(('Image Files', '*.jpg'), ('Image Files', '*.jpeg'), ('All Files', '*.*'))
    )
    file_explorer.configure(text="File Opened: "+file_path)


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
