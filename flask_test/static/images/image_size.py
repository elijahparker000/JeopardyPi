#This script will tell you the size of an image (X_Pixels x Y_Pixels)
from PIL import Image
import sys

def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            print(f"The size of the image is: {width} x {height} pixels")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_size.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        get_image_size(image_path)
