from PIL import Image
import numpy as np

image = Image.open('beau.png')
print(type(image))  # Output: <class 'PIL.PngImagePlugin.PngImageFile'>
print(image.size)  # Output: (width, height)

image_array = np.array(image)
print(type(image_array))  # Output: <class 'numpy.ndarray'>
print(image_array.shape)  # Output: (height, width, depth)

# Create a random RGB image array
image_array = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Convert the array to a PIL image
image = Image.fromarray(image_array)
print(type(image))  # Output: <class 'PIL.Image.Image'>