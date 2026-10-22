from pathlib import Path

# ===== Dataset Path =====
DATASET_PATH = Path("datasets/crop")

# Agar weather check karna ho to:
# DATASET_PATH = Path("datasets/weather")

print("=" * 50)
print("      DATASET INFORMATION")
print("=" * 50)

# Sirf folders (classes) lo
classes = sorted([folder for folder in DATASET_PATH.iterdir() if folder.is_dir()])

print(f"\nTotal Classes : {len(classes)}\n")

total_images = 0

# Valid image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

for cls in classes:

    image_count = 0

    for image in cls.iterdir():

        if image.suffix.lower() in image_extensions:
            image_count += 1

    print(f"{cls.name:<15} : {image_count} images")

    total_images += image_count

print("\n" + "-" * 50)
print(f"Total Images : {total_images}")
print("-" * 50)