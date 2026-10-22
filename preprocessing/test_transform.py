from pathlib import Path
from PIL import Image

from transforms import train_transform

image_path = list(Path("datasets/crop/rice").glob("*"))[0]

image = Image.open(image_path).convert("RGB")

print("Before Transform")
print(type(image))
print(image.size)

tensor = train_transform(image)

print("\nAfter Transform")
print(type(tensor))
print(tensor.shape)

print("\nMin :", tensor.min().item())
print("Max :", tensor.max().item())
print("Mean:", tensor.mean().item())
print("Std :", tensor.std().item())