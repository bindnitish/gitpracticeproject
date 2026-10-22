from pathlib import Path
import sys
import torch
from PIL import Image

# ==========================
# Project Root
# ==========================
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from models.weather_model import WeatherModel
from preprocessing.transforms import test_transform

# ==========================
# Weather Classes
# ==========================
classes = [
    "dew",
    "fogsmog",
    "frost",
    "glaze",
    "hail",
    "lightning",
    "rain",
    "rainbow",
    "rime",
    "sandstorm",
    "snow"
]

# ==========================
# Device
# ==========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ==========================
# Load Model
# ==========================
model = WeatherModel().to(device)

model.load_state_dict(
    torch.load(
        ROOT / "models" / "weather_model.pth",
        map_location=device
    )
)

model.eval()


# ==========================
# Prediction Function
# ==========================
def predict_weather(image_path):

    image = Image.open(image_path).convert("RGB")

    image = test_transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        prediction = torch.argmax(output, dim=1).item()

    return classes[prediction]


# ==========================
# Test
# ==========================
if __name__ == "__main__":

    image = list((ROOT / "datasets" / "weather" / "rain").glob("*"))[0]

    prediction = predict_weather(image)

    print("Prediction :", prediction)