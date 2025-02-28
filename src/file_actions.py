from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def browse_files(exp_lbl, canvas):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        exp_lbl.configure(text=f"File Opened: {file_path}")
        display_image(file_path, canvas)


def display_image(path, canvas):
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, image=photo)
