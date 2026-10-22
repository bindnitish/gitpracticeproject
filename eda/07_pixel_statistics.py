from pathlib import Path
from PIL import Image
import numpy as np

# Dataset Path
DATASET_PATH = Path("datasets/crop")

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

pixels = []

print("=" * 60)
print("PIXEL STATISTICS")
print("=" * 60)

for cls in sorted(DATASET_PATH.iterdir()):

    if cls.is_dir():

        for image_path in cls.iterdir():

            if image_path.suffix.lower() in image_extensions:

                img = Image.open(image_path).convert("RGB")

                img = np.array(img) / 255.0

                pixels.append(img)

# Stack all images
pixels = np.concatenate([img.reshape(-1,3) for img in pixels], axis=0)

mean = pixels.mean(axis=0)
std = pixels.std(axis=0)

print("\nMean (R,G,B):")
print(mean)

print("\nStd (R,G,B):")
print(std)

print("=" * 60)