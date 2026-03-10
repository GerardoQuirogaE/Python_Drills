import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

path = Path('images')
# files = list(path.iterdir())
files = [str(p) for p in path.iterdir()]

def load_image(string_img_path):
    image = Image.open(string_img_path)
    # image.show()
    image_array = np.array(image)
    print(f"image_array shape = {image_array.shape}")

    if image_array.dtype != np.uint8:
        raise ValueError("Image is not 8-bit.")

    img_norm_array = image_array/255.0

    return img_norm_array

def calculate_luminance(img_array):
    if img_array.ndim == 2:
        return np.mean(img_array)
    
    R = img_array[:,:,0]
    G = img_array[:,:,1]    
    B = img_array[:,:,2]
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B

    avg_luminance = np.mean(Y)
    return avg_luminance

def plot_pixel_intensity(image_array):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Show the image on the left
    if image_array.ndim == 2:  # Grayscale image
        axes[0].imshow(image_array, cmap='gray')
    else:  # RGB image
        axes[0].imshow(image_array)
    axes[0].set_title("Image")
    axes[0].axis('off')

    # Plot histogram on the right
    if image_array.ndim == 2:  # Grayscale
        gray_values = image_array.flatten()
        axes[1].hist(gray_values, bins=256, color='gray')
    else:  # RGB
        R = image_array[:, :, 0].flatten()
        G = image_array[:, :, 1].flatten()
        B = image_array[:, :, 2].flatten()

        axes[1].hist(R, bins=256, color='red', alpha=0.5)
        axes[1].hist(G, bins=256, color='green', alpha=0.5)
        axes[1].hist(B, bins=256, color='blue', alpha=0.5)

    axes[1].set_title("Pixel Intensity Histogram")
    plt.tight_layout()
    plt.show()



def main():
    
    while True:
        print("Available images:")
        for i, filename in enumerate(files, start=1):
            filename = filename.split("/")[-1]
            print(f"{i}. {filename}")

        user_input = input("Select an image (q to quit): ").strip()

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        choice = int(user_input)
        if choice < 1 or choice > len(files):
            print(f"Invalid choice. Please select a number between 1 and {len(files)}.")
            continue

        img_array = load_image(files[choice - 1])

        luminance = calculate_luminance(img_array)

        print(f"The average luminance of the image: {luminance:.3f}\n")

        plot_pixel_intensity(img_array)

if __name__ == "__main__":
    main()