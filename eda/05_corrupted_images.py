from pathlib import Path
from PIL import Image

# Dataset Path
DATASET_PATH = Path("datasets/crop")

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

total_images = 0
corrupted_images = []

print("=" * 60)
print("CORRUPTED IMAGE DETECTION")
print("=" * 60)

for cls in sorted(DATASET_PATH.iterdir()):

    if cls.is_dir():

        print(f"\nChecking : {cls.name}")

        for image_path in cls.iterdir():

            if image_path.suffix.lower() in image_extensions:

                total_images += 1

                try:

                    img = Image.open(image_path)
                    img.verify()

                except Exception:

                    corrupted_images.append(image_path)

                    print(f"❌ Corrupted : {image_path.name}")

print("\n" + "=" * 60)

print(f"Total Images      : {total_images}")
print(f"Corrupted Images  : {len(corrupted_images)}")

if len(corrupted_images) == 0:

    print("\n✅ Dataset is clean.")

else:

    print("\nList of Corrupted Images:")

    for img in corrupted_images:
        print(img)

print("=" * 60)