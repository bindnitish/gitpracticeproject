from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

from transforms import train_transform

image_path = list(Path("datasets/crop/rice").glob("*"))[0]

image = Image.open(image_path).convert("RGB")

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

for i in range(3):

    aug = train_transform(image)

    aug = aug.permute(1,2,0).numpy()

    mean = [0.485,0.456,0.406]
    std = [0.229,0.224,0.225]

    aug = aug * std + mean
    aug = aug.clip(0,1)

    plt.subplot(1,4,i+2)
    plt.imshow(aug)
    plt.title(f"Aug {i+1}")
    plt.axis("off")

plt.tight_layout()
plt.show()