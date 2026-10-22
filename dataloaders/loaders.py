from pathlib import Path
import sys

from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder

# Project Root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from preprocessing.transforms import train_transform, test_transform

# ==========================
# Dataset Path
# ==========================
DATASET_PATH = ROOT / "datasets" / "crop"

# ==========================
# Full Dataset
# ==========================
full_dataset = ImageFolder(
    root=DATASET_PATH,
    transform=train_transform
)

# ==========================
# Train / Validation Split
# ==========================
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size

train_dataset, val_dataset = random_split(
    full_dataset,
    [train_size, val_size]
)

# Validation dataset uses test transform
val_dataset.dataset.transform = test_transform

# ==========================
# DataLoaders
# ==========================
train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True,
    num_workers=0
)

val_loader = DataLoader(
    val_dataset,
    batch_size=16,
    shuffle=False,
    num_workers=0
)

# ==========================
# Test
# ==========================
train_images, train_labels = next(iter(train_loader))
val_images, val_labels = next(iter(val_loader))

print("=" * 60)
print("DataLoader Ready")
print("=" * 60)

print(f"Train Images : {train_images.shape}")
print(f"Train Labels : {train_labels.shape}")

print(f"\nValidation Images : {val_images.shape}")
print(f"Validation Labels : {val_labels.shape}")