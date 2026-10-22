from pathlib import Path
from PIL import Image

from transforms import train_transform

# ---------------------------------
# Image Path
# ---------------------------------

IMAGE_PATH = Path("datasets/crop/rice")

image_path = list(IMAGE_PATH.glob("*"))[0]

image = Image.open(image_path).convert("RGB")

tensor = train_transform(image)

print("=" * 50)
print("Normalized Tensor")
print("=" * 50)

print("Shape :", tensor.shape)

print("Data Type :", tensor.dtype)

print("Minimum :", tensor.min().item())

print("Maximum :", tensor.max().item())

print("Mean :", tensor.mean().item())

print("Std :", tensor.std().item())