from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont


def browse_files(container, **kwargs):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        if 'label' in kwargs and 'canvas' in kwargs:
            kwargs['label'].configure(text=f"File Opened: {file_path}")
            display_image(file_path, kwargs['canvas'], container)


def display_image(path, canvas, container):
    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)
    photo_width = photo.width()
    photo_height = photo.height()
    canvas.create_image((canvas.winfo_width()/2), (canvas.winfo_height()/2), image=photo)
    container.clear()
    container.append(photo)


# TODO: Think about required arguments, and about setting kwargs
def add_watermark(method, img_path, watermark_img, watermark_txt):
    img = Image.open(img_path)
    if method == 'txt':
        text_pos = (100, 100)
        font = ImageFont.load_default()
        draw = ImageDraw.Draw(img)
        draw.text(text_pos, watermark_txt, font=font, fill=(255, 255, 255))

        img.save('watermarked-image.jpg')
        # TODO: Write functionality to add text watermark
    elif method == 'img':
        pass
        # TODO: Write functionality to add image watermark
