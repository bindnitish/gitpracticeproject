from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import random

# Dataset Path
DATASET_PATH = Path("datasets/crop")

# Supported image formats
image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

classes = sorted([folder for folder in DATASET_PATH.iterdir() if folder.is_dir()])

for cls in classes:

    images = []

    for ext in image_extensions:
        images.extend(cls.glob(f"*{ext}"))

    if len(images) == 0:
        continue

    # Maximum 5 random images
    sample_images = random.sample(images, min(5, len(images)))

    plt.figure(figsize=(15,3))

    for i, img_path in enumerate(sample_images):

        img = Image.open(img_path)

        plt.subplot(1, len(sample_images), i+1)

        plt.imshow(img)

        plt.title(cls.name)

        plt.axis("off")

    plt.suptitle(f"Sample Images : {cls.name}", fontsize=14)

    plt.tight_layout()

    plt.show()