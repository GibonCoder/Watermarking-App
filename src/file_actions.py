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
def add_watermark(method, saved_img, watermark, watermark_txt):
    watermarked = saved_img.copy()
    font = ImageFont.load_default(40)
    font_col = (128, 128, 128)
    if method == 'txt':
        draw = ImageDraw.Draw(watermarked)
        # Calculate text size
        ascent, descent = font.getmetrics()

        text_w = font.getmask(watermark_txt).getbox()[2]
        text_h = font.getmask(watermark_txt).getbox()[3] + descent
        # Calculate text position
        x = (watermarked.width() - text_w) / 2
        y = (watermarked.height() - text_h) / 2

        draw.text((x, y), watermark_txt, font=font, fill=font_col)
        watermarked.save()
        # TODO: Write functionality to add text watermark
    elif method == 'img':
        pass
        # TODO: Write functionality to add image watermark
