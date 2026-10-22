from pathlib import Path
import sys

# Project Root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from preprocessing.transforms import train_transform
from torchvision.datasets import ImageFolder

# ==========================
# Dataset Path
# ==========================
DATASET_PATH = ROOT / "datasets" / "crop"

# ==========================
# Load Dataset
# ==========================
dataset = ImageFolder(
    root=DATASET_PATH,
    transform=train_transform
)

# ==========================
# Dataset Information
# ==========================
print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(f"Total Images : {len(dataset)}")
print(f"Classes      : {dataset.classes}")
print(f"Class Index  : {dataset.class_to_idx}")