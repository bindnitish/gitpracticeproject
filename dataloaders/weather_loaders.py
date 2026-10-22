from pathlib import Path
import sys

from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder

# ==========================
# Project Root
# ==========================
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from preprocessing.transforms import train_transform, test_transform

# ==========================
# Dataset
# ==========================
DATASET_PATH = ROOT / "datasets" / "weather"

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

# Validation Transform
val_dataset.dataset.transform = test_transform

# ==========================
# DataLoaders
# ==========================
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=0
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False,
    num_workers=0
)

# ==========================
# Test
# ==========================
images, labels = next(iter(train_loader))

print("=" * 50)
print("Weather DataLoader Ready")
print("=" * 50)

print("Images :", images.shape)
print("Labels :", labels.shape)