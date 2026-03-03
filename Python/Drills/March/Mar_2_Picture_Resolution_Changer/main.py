import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


class ImageOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Size Optimizer")
        self.root.geometry("450x300")
        self.root.resizable(False, False)

        self.file_path = None

        # Title
        tk.Label(root, text="Image Size Optimizer", font=("Arial", 16, "bold")).pack(pady=10)

        # Select Button
        self.select_btn = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_btn.pack(pady=5)

        self.file_label = tk.Label(root, text="No file selected", wraplength=400)
        self.file_label.pack()

        # Target Size Entry
        tk.Label(root, text="Target Size (MB):").pack(pady=10)
        self.size_entry = tk.Entry(root)
        self.size_entry.pack()

        # Compress Button
        self.compress_btn = tk.Button(root, text="Compress Image", command=self.compress_image)
        self.compress_btn.pack(pady=15)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
        )
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=file_path)

    def compress_image(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        try:
            target_mb = float(self.size_entry.get())
            target_size = target_mb * 1024 * 1024
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for size.")
            return

        img = Image.open(self.file_path)

        # Convert PNG with transparency to RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        output_path = os.path.splitext(self.file_path)[0] + "_compressed.jpg"

        quality = 95
        img.save(output_path, "JPEG", quality=quality)

        # Reduce quality first
        while os.path.getsize(output_path) > target_size and quality > 10:
            quality -= 5
            img.save(output_path, "JPEG", quality=quality)

        # Then reduce resolution if needed
        while os.path.getsize(output_path) > target_size:
            width, height = img.size
            img = img.resize((int(width * 0.9), int(height * 0.9)))
            img.save(output_path, "JPEG", quality=quality)

        final_size = os.path.getsize(output_path) / (1024 * 1024)

        self.result_label.config(
            text=f"Saved!\nSize: {final_size:.2f} MB\nResolution: {img.size[0]} x {img.size[1]}"
        )

        messagebox.showinfo("Success", "Image compressed successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageOptimizerApp(root)
    root.mainloop()