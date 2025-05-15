# -----------------------------------------
# 📄 Project: Image Resizer Tool
# 👨‍💻 Created by: Hashir Adnan
# 🌐 Website: www.techthf.xyz
# 🗓️ Date: May 14, 2025
# -----------------------------------------
# 🧠 Description:
# This GUI-based Python tool allows users to open an image file, resize it to
# desired width and height, and save the resized image. It supports common
# image formats like JPG, PNG, and BMP.
# -----------------------------------------
# 📦 Features:
# - Open image file dialog
# - Resize image to custom dimensions
# - Save resized image to chosen location
# - Status updates for user feedback
# -----------------------------------------
# 🧰 Tools & Modules Used:
# - tkinter: GUI interface and dialogs
# - PIL (Pillow): image processing
# -----------------------------------------
# 💡 How to Use:
# 1. Click "Open Image" to select an image file.
# 2. Enter the desired width and height.
# 3. Click "Resize and Save" to resize and save the new image.
# -----------------------------------------

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((width, height))
        return resized_img
    except Exception as e:
        status_label.config(text=f"Error loading image: {e}")
        return None

def open_file():
    global img_path  # Use global variable to store file path
    img_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    print(f"Selected file path: {img_path}")  # Debug print
    if img_path:
        try:
            img = Image.open(img_path)
            img.thumbnail((250, 250))  # Resize the image to fit into the window
            img = ImageTk.PhotoImage(img)

            panel.config(image=img)
            panel.image = img  # Keep a reference to the image to avoid garbage collection
            status_label.config(text="Image Loaded Successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {e}")

def save_resized_image(img):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        status_label.config(text="Image saved successfully!")

def resize_and_save():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        if img_path:  # Check if an image is loaded
            resized_img = resize_image(img_path, width, height)
            if resized_img:
                save_resized_image(resized_img)
        else:
            status_label.config(text="Please load an image first.")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

app = tk.Tk()
app.title("Image Resizer Tool")

img_path = None  # Initialize img_path to None

width_label = tk.Label(app, text="Width:")
width_label.pack(pady=5)
width_entry = tk.Entry(app)
width_entry.pack(pady=5)

height_label = tk.Label(app, text="Height:")
height_label.pack(pady=5)
height_entry = tk.Entry(app)
height_entry.pack(pady=5)

open_button = tk.Button(app, text="Open Image", command=open_file)
open_button.pack(pady=10)

resize_button = tk.Button(app, text="Resize and Save", command=resize_and_save)
resize_button.pack(pady=10)

status_label = tk.Label(app, text="")
status_label.pack(pady=5)

panel = tk.Label(app)
panel.pack(pady=20)

app.mainloop()
