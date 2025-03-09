from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os


def browse_files(img_container, paths_container, **kwargs):
    file_path = askopenfilename(
        initialdir='/',
        title="Select File",
        filetypes=[('Image Files', '*.jpg *.jpeg *.png')]
    )
    if not len(file_path) == 0:
        if 'label' in kwargs and 'canvas' in kwargs:
            kwargs['label'].configure(text=f"File Opened: {file_path}")
            display_image(file_path, kwargs['canvas'], img_container, paths_container)


def display_image(photo_path, canvas, img_container, paths_cont):
    paths_cont.append(photo_path)
    img = Image.open(photo_path)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image((canvas.winfo_width()/2), (canvas.winfo_height()/2), image=photo)
    img_container.clear()
    img_container.append(photo)


# TODO: Think about required arguments, and about setting kwargs
def add_watermark(method, img_path, watermark_path, watermark_txt):
    image = Image.open(img_path)
    if method == 'txt':
        font = ImageFont.truetype("arial.ttf", 30)
        f_color = (128, 128, 128, 128)
        draw = ImageDraw.Draw(image)
        for x in range(10, image.width-10, 150):
            for y in range(10, image.height-10, 150):
                pos = (x, y)
                draw.text(pos, watermark_txt, font=font, fill=f_color)
        rgb_watermarked = image.convert("RGB")
        save_image(rgb_watermarked)

    elif method == 'img':
        watermark = Image.open(watermark_path)
        target_width = 200
        # adjustments
        aspect_ratio = float(target_width) / watermark.width
        target_height = int(watermark.height * aspect_ratio)
        watermark = watermark.resize((target_width, target_height), Image.Resampling.LANCZOS)
        pos = (int(image.width/2), int(image.height/2))
        image.paste(watermark, pos, watermark)
        # TODO: Need fix
        save_image(image)


def save_image(watermarked_img):
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "watermarked_img.jpg")

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    watermarked_img.save(save_path, "JPEG")
    print(f"Image saved to: {save_path}")


