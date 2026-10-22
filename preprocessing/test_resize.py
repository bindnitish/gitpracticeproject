from pathlib import Path
from PIL import Image

from transforms import resize_transform

# ---------------------------------
# Image Path
# ---------------------------------

IMAGE_PATH = Path("datasets/crop/rice")

# First image
image_path = list(IMAGE_PATH.glob("*"))[0]

# Load image
image = Image.open(image_path)

print("Original Size :", image.size)

# Apply resize
resized_image = resize_transform(image)

print("Resized Size  :", resized_image.size)