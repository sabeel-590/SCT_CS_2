from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

selected_image = None

# ------------------------
# Select Image
# ------------------------
def select_image():
    global selected_image

    selected_image = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp")
        ]
    )

    if selected_image:
        image_name.config(
            text=os.path.basename(selected_image)
        )


# ------------------------
# Encrypt Image
# ------------------------
def encrypt_image():

    global selected_image

    if not selected_image:
        messagebox.showerror(
            "Error",
            "Please select an image first"
        )
        return

    try:

        key = int(key_entry.get())

        img = Image.open(selected_image)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):

                r, g, b = pixels[x, y][:3]

                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                pixels[x, y] = (r, g, b)

        save_path = "encrypted_image.png"

        img.save(save_path)

        result_label.config(
            text=f"Encrypted Saved:\n{save_path}",
            fg="#22c55e"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ------------------------
# Decrypt Image
# ------------------------
def decrypt_image():

    global selected_image

    if not selected_image:
        messagebox.showerror(
            "Error",
            "Please select an image first"
        )
        return

    try:

        key = int(key_entry.get())

        img = Image.open(selected_image)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):

                r, g, b = pixels[x, y][:3]

                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                pixels[x, y] = (r, g, b)

        save_path = "decrypted_image.png"

        img.save(save_path)

        result_label.config(
            text=f"Decrypted Saved:\n{save_path}",
            fg="#38bdf8"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ------------------------
# Clear
# ------------------------
def clear_all():
    image_name.config(text="No Image Selected")
    key_entry.delete(0, END)
    result_label.config(text="")
    global selected_image
    selected_image = None


# ------------------------
# GUI
# ------------------------

root = Tk()

root.title("Image Encryption Tool")
root.geometry("850x650")
root.configure(bg="#0f172a")
root.resizable(False, False)

# Heading
Label(
    root,
    text="IMAGE ENCRYPTION TOOL",
    font=("Segoe UI", 26, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=20)

Label(
    root,
    text="SkillCraft Technology - Cyber Security Internship",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
).pack()

# Main Frame
main_frame = Frame(
    root,
    bg="#1e293b",
    width=750,
    height=400
)

main_frame.pack(pady=35)
main_frame.pack_propagate(False)

Label(
    main_frame,
    text="Select Image",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="white"
).pack(pady=(25,10))

Button(
    main_frame,
    text="Browse Image",
    command=select_image,
    bg="#2563eb",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=15,
    pady=8
).pack()

image_name = Label(
    main_frame,
    text="No Image Selected",
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="#cbd5e1"
)

image_name.pack(pady=15)

Label(
    main_frame,
    text="Encryption Key",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="white"
).pack()

key_entry = Entry(
    main_frame,
    width=20,
    font=("Segoe UI", 12)
)

key_entry.pack(pady=10)

button_frame = Frame(
    main_frame,
    bg="#1e293b"
)

button_frame.pack(pady=30)

Button(
    button_frame,
    text="Encrypt Image",
    command=encrypt_image,
    bg="#16a34a",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=10
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Decrypt Image",
    command=decrypt_image,
    bg="#dc2626",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=10
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="Clear",
    command=clear_all,
    bg="#f59e0b",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    padx=20,
    pady=10
).grid(row=0, column=2, padx=10)

result_label = Label(
    main_frame,
    text="",
    bg="#1e293b",
    fg="white",
    font=("Segoe UI", 12, "bold")
)

result_label.pack(pady=20)

Label(
    root,
    text="Supports PNG, JPG, JPEG and BMP Images",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 10)
).pack(side=BOTTOM, pady=10)

root.mainloop()
