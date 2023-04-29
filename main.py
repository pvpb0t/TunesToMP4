import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont


def browse_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    image_label.config(text=image_path)

def browse_audio():
    global audio_path
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav")])
    audio_label.config(text=audio_path)

def create_video():
    global image_path, audio_path, stretch_var

    img = Image.open(image_path)
    img_w, img_h = img.size
    target_w, target_h = 1920, 1080

    if stretch_var.get():
        img = img.resize((target_w, target_h))
    else:
        scale = min(target_w / img_w, target_h / img_h)
        new_w, new_h = int(img_w * scale), int(img_h * scale)

        background = Image.new('RGB', (target_w, target_h), (0, 0, 0))
        img = img.resize((new_w, new_h), Image.ANTIALIAS)
        background.paste(img, ((target_w - new_w) // 2, (target_h - new_h) // 2))
        img = background

    img.save("resized_image.png")

    image = ImageClip("resized_image.png")

    audio = AudioFileClip(audio_path)
    duration = audio.duration

    image = image.set_duration(duration).set_audio(audio)

    watermark_img = Image.new('RGBA', (400, 50), (0, 0, 0, 255))
    draw = ImageDraw.Draw(watermark_img)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((10, 10), "github.com/pvpb0t/TunesToMP4", font=font, fill=(255, 255, 255, 255))

    watermark_img.save("watermark.png")
    watermark = ImageClip("watermark.png").set_duration(duration).set_position(("right", "top"))

    final_video = CompositeVideoClip([image, watermark])

    final_video.write_videofile("output.mp4", fps=24, codec="libx264", audio_codec="aac")



root = tk.Tk()
root.title("TunesToMP4")

image_path = ""
audio_path = ""

image_label = tk.Label(root, text="No image selected")
image_label.pack()
image_button = tk.Button(root, text="Browse Image", command=browse_image)
image_button.pack()

stretch_var = tk.BooleanVar()
stretch_checkbutton = tk.Checkbutton(root, text="Stretch Image", variable=stretch_var)
stretch_checkbutton.pack()

audio_label = tk.Label(root, text="No audio selected")
audio_label.pack()
audio_button = tk.Button(root, text="Browse Audio", command=browse_audio)
audio_button.pack()

create_button = tk.Button(root, text="Create Video", command=create_video)
create_button.pack()

root.mainloop()
