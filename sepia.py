from PIL import Image
import os

# --- Set your image path ---
input_path = r"C:\Users\student\Desktop\New folder (2)\smokey.gif"
output_path = r"C:\Users\student\Desktop\New folder (2)\smokey_sepia.gif"

# Check if the file exists
if not os.path.exists(input_path):
    print("File not found:", input_path)
    exit()

# --- Function to convert image to grayscale ---
def grayscale(image):
    width, height = image.size
    gray_image = image.copy()
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = int((r + g + b) / 3)
            gray_image.putpixel((x, y), (gray, gray, gray))
    return gray_image

# --- Function to apply sepia ---
def sepia(image):
    gray_image = grayscale(image)
    sepia_image = gray_image.copy()
    width, height = sepia_image.size

    for y in range(height):
        for x in range(width):
            r, g, b = sepia_image.getpixel((x, y))

            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)

            sepia_image.putpixel((x, y), (r, g, b))

    return sepia_image

# --- Load image ---
img = Image.open(input_path).convert("RGB")

# --- Convert to sepia ---
sepia_img = sepia(img)

# --- Save the new image ---
sepia_img.save(output_path)
print("Sepia image saved to:", output_path)

# --- Optionally display ---
sepia_img.show()
