from pathlib import Path
import hashlib

# Dataset Path
DATASET_PATH = Path("datasets/crop")

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

hash_dict = {}
duplicates = []

print("=" * 60)
print("DUPLICATE IMAGE DETECTION")
print("=" * 60)

for cls in sorted(DATASET_PATH.iterdir()):

    if cls.is_dir():

        print(f"\nChecking : {cls.name}")

        for image_path in cls.iterdir():

            if image_path.suffix.lower() in image_extensions:

                with open(image_path, "rb") as f:

                    file_hash = hashlib.md5(f.read()).hexdigest()

                if file_hash in hash_dict:

                    duplicates.append((image_path, hash_dict[file_hash]))

                else:

                    hash_dict[file_hash] = image_path

print("\n" + "=" * 60)

print(f"Total Unique Images : {len(hash_dict)}")
print(f"Duplicate Images    : {len(duplicates)}")

if len(duplicates) == 0:

    print("\n✅ No Duplicate Images Found.")

else:

    print("\nDuplicate Images:\n")

    for dup, original in duplicates:

        print(f"Duplicate : {dup}")
        print(f"Original  : {original}")
        print("-" * 50)

print("=" * 60)