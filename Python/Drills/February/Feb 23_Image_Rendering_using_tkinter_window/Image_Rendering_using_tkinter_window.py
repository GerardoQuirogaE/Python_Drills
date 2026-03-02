import random
import requests
from io import BytesIO
from tkinter import Tk, Label
from PIL import Image, ImageTk

buiscuit_list = [
    "https://media.giphy.com/media/1fhj2W53BjaVVib2A2/giphy.gif",
    "https://media.giphy.com/media/DdFJCeDKpcYRa/giphy.gif",
    "https://media.giphy.com/media/9Sm4nl7cr10VFpbSD6/giphy.gif",
    "https://media.giphy.com/media/7UtUgAeIXFbCU/giphy.gif"
]

gif_url = random.choice(buiscuit_list)

# Download the GIF
response = requests.get(gif_url)
img_data = response.content

# Create window
root = Tk()
root.title("Dog Biscuit Day")
root.geometry("500x500")
root.attributes("-topmost", True)

# Load image
image = Image.open(BytesIO(img_data))
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()

print("Happy National Dog Biscuit Day...")

root.mainloop()