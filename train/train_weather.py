from pathlib import Path
import sys
import torch

# ==========================
# Project Root
# ==========================
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from models.weather_model import WeatherModel
from dataloaders.weather_loaders import train_loader
from train.loss import criterion
from train.optimizer import get_optimizer
from train.engine import train_one_epoch

# ==========================
# Device
# ==========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ==========================
# Model
# ==========================
model = WeatherModel().to(device)

optimizer = get_optimizer(model)

EPOCHS = 10

best_loss = float("inf")

for epoch in range(EPOCHS):

    loss, acc = train_one_epoch(
        model,
        train_loader,
        criterion,
        optimizer,
        device
    )

    print(f"Epoch [{epoch+1}/{EPOCHS}]")
    print(f"Loss     : {loss:.4f}")
    print(f"Accuracy : {acc:.2f}%")
    print("-" * 50)

    if loss < best_loss:

        best_loss = loss

        torch.save(
            model.state_dict(),
            ROOT / "models" / "weather_model.pth"
        )

print("=" * 60)
print("Weather Training Finished")
print("=" * 60)

print("Best Loss :", best_loss)