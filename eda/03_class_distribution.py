from pathlib import Path
import matplotlib.pyplot as plt

# Dataset Path
DATASET_PATH = Path("datasets/crop")

classes = []
counts = []

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

for folder in sorted(DATASET_PATH.iterdir()):

    if folder.is_dir():

        image_count = 0

        for image in folder.iterdir():

            if image.suffix.lower() in image_extensions:
                image_count += 1

        classes.append(folder.name)
        counts.append(image_count)

# Print Table
print("=" * 45)
print("CLASS DISTRIBUTION")
print("=" * 45)

for cls, count in zip(classes, counts):
    print(f"{cls:<15} : {count}")

# Plot
plt.figure(figsize=(8,5))

bars = plt.bar(classes, counts)

plt.title("Crop Dataset Class Distribution")
plt.xlabel("Crop Classes")
plt.ylabel("Number of Images")

# Values on bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.2,
        str(int(bar.get_height())),
        ha='center'
    )

plt.tight_layout()
plt.show()