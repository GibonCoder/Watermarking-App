from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def browse_files(label):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        label.configure(text=f"File Opened: {file_path}")


def display_image(path, label):
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    label.configure(image=photo)
