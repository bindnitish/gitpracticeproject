from pathlib import Path
import sys

from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

# Project Root
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from preprocessing.transforms import train_transform

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
# Create DataLoader
# ==========================
train_loader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)

# ==========================
# Test DataLoader
# ==========================
images, labels = next(iter(train_loader))

print("=" * 50)
print("DataLoader Created Successfully")
print("=" * 50)

print(f"Image Batch Shape : {images.shape}")
print(f"Label Shape       : {labels.shape}")

print("\nLabels:")
print(labels)