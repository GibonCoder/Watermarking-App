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


def display_image(photo, canvas, img_container, paths_cont):
    paths_cont.append(photo)
    img = Image.open(photo)
    photo = ImageTk.PhotoImage(img)
    photo_width = photo.width()
    photo_height = photo.height()
    canvas.create_image((canvas.winfo_width()/2), (canvas.winfo_height()/2), image=photo)
    img_container.clear()
    img_container.append(photo)


# TODO: Think about required arguments, and about setting kwargs
# TODO: Replace objects with paths to work w/ them within the func
def add_watermark(method, img_path, watermark, watermark_txt):
    watermarked = Image.open(img_path)
    if method == 'txt':
        tex_position = (watermarked.width/2, watermarked.height/2)
        font = ImageFont.truetype("arial.ttf", 100)
        f_color = (255, 255, 255)
        draw = ImageDraw.Draw(watermarked)
        draw.text(tex_position, watermark_txt, font=font, fill=f_color)
        rgb_watermarked = watermarked.convert("RGB")
        save_image(rgb_watermarked)
        # watermarked.save("watermarked_image.jpg")

        # TODO: Write functionality to add text watermark
    elif method == 'img':
        pass
        # TODO: Write functionality to add image watermark


def save_image(watermarked_img):
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "watermarked_img.jpg")

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    watermarked_img.save(save_path, "JPEG")
    print(f"Image saved to: {save_path}")


