import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

image_folder = ""
image_list = []
current_image_index = 0

def select_folder():
    global image_folder, image_list, current_image_index
    image_folder = filedialog.askdirectory(title="Select Image Folder")
    if not image_folder:
        return

    image_list = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))
    ]

    if not image_list:
        messagebox.showinfo("No Images", "The selected folder contains no supported images.")
        return

    current_image_index = 0
    show_image()

    prev_button.config(state=tk.NORMAL)
    next_button.config(state=tk.NORMAL)

def show_image():
    global current_image_index, image_list
    if not image_list:
        return

    image_path = image_list[current_image_index]
    image = Image.open(image_path)

    image.thumbnail((500, 400))
    photo = ImageTk.PhotoImage(image)

    canvas.delete("all")
    canvas.create_image(250, 200, image=photo)
    canvas.image = photo  # Keep a reference to avoid garbage collection

def show_next_image():
    global current_image_index, image_list
    if current_image_index < len(image_list) - 1:
        current_image_index += 1
        show_image()

def show_previous_image():
    global current_image_index, image_list
    if current_image_index > 0:
        current_image_index -= 1
        show_image()

root = tk.Tk()
root.title("Image Browser")
root.geometry("600x550")
root.minsize(600, 530)

canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

prev_button = tk.Button(button_frame, text="Previous", command=show_previous_image, state=tk.DISABLED)
prev_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(button_frame, text="Next", command=show_next_image, state=tk.DISABLED)
next_button.pack(side=tk.LEFT, padx=10)

select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=10)

root.mainloop()