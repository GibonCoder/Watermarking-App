from tkinter.filedialog import askopenfilename


def browse_files(label):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        label.configure(text=f"File Opened: {file_path}")
