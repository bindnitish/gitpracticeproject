from pathlib import Path
from PIL import Image

# ===========================
# Dataset Path
# ===========================
DATASET_PATH = Path("datasets/crop")

print("=" * 60)
print("IMAGE SIZE ANALYSIS")
print("=" * 60)

all_widths = []
all_heights = []

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

for cls in sorted(DATASET_PATH.iterdir()):

    if cls.is_dir():

        print(f"\nClass : {cls.name}")

        widths = []
        heights = []

        for image_path in cls.iterdir():

            if image_path.suffix.lower() in image_extensions:

                try:
                    img = Image.open(image_path)

                    width, height = img.size

                    widths.append(width)
                    heights.append(height)

                    all_widths.append(width)
                    all_heights.append(height)

                except Exception:
                    print(f"Cannot open: {image_path.name}")

        print(f"Images       : {len(widths)}")
        print(f"Min Size     : {min(widths)} x {min(heights)}")
        print(f"Max Size     : {max(widths)} x {max(heights)}")
        print(f"Average Size : {sum(widths)//len(widths)} x {sum(heights)//len(heights)}")

print("\n" + "=" * 60)
print("OVERALL DATASET")
print("=" * 60)

print(f"Minimum Width  : {min(all_widths)}")
print(f"Maximum Width  : {max(all_widths)}")

print(f"Minimum Height : {min(all_heights)}")
print(f"Maximum Height : {max(all_heights)}")

print(f"Average Width  : {sum(all_widths)//len(all_widths)}")
print(f"Average Height : {sum(all_heights)//len(all_heights)}")