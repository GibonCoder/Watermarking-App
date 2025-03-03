from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def browse_files(exp_lbl, canvas, container):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        exp_lbl.configure(text=f"File Opened: {file_path}")
        display_image(file_path, canvas, container)


def display_image(path, canvas, container):
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    photo_width = photo.width()
    photo_height = photo.height()
    canvas.create_image((canvas.winfo_width()/2), (canvas.winfo_height()/2), image=photo)
    container.clear()
    container.append(photo)
