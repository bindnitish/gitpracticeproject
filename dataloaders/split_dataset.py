from pathlib import Path
import sys

from torch.utils.data import random_split
from torchvision.datasets import ImageFolder

# Project Root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from preprocessing.transforms import train_transform

# ==========================
# Dataset
# ==========================
DATASET_PATH = ROOT / "datasets" / "crop"

dataset = ImageFolder(
    root=DATASET_PATH,
    transform=train_transform
)

# ==========================
# Train / Validation Split
# ==========================
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size]
)

print("=" * 50)
print("Dataset Split Successfully")
print("=" * 50)

print(f"Total Images      : {len(dataset)}")
print(f"Training Images   : {len(train_dataset)}")
print(f"Validation Images : {len(val_dataset)}")