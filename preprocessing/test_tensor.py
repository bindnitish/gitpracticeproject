from pathlib import Path
from PIL import Image
from torchvision import transforms

# ---------------------------------
# Image Path
# ---------------------------------

IMAGE_PATH = Path("datasets/crop/rice")

image_path = list(IMAGE_PATH.glob("*"))[0]

# Load Image
image = Image.open(image_path).convert("RGB")

print("=" * 50)
print("Original Image")
print("=" * 50)

print("Type :", type(image))
print("Size :", image.size)

# -----------------------------
# Transform
# -----------------------------

transform = transforms.ToTensor()

tensor = transform(image)

print("\n" + "=" * 50)
print("Tensor")
print("=" * 50)

print("Type :", type(tensor))
print("Shape:", tensor.shape)
print("Data Type:", tensor.dtype)

print("\nMinimum Pixel :", tensor.min().item())
print("Maximum Pixel :", tensor.max().item())