from tkinter.filedialog import askopenfilename


def browse_files():
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if file_path != "":
        return True, file_path
    return False, None
