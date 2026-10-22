from pathlib import Path
import sys
import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from models.crop_model import CropModel
from preprocessing.transforms import test_transform

classes = [
    "jute",
    "maize",
    "rice",
    "sugarcane",
    "wheat"
]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CropModel().to(device)

model.load_state_dict(
    torch.load(
        ROOT / "models" / "crop_model.pth",
        map_location=device
    )
)

model.eval()


def predict_crop(image_path):

    image = Image.open(image_path).convert("RGB")

    image = test_transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        output = model(image)

        prediction = torch.argmax(output, dim=1).item()

    return classes[prediction]


if __name__ == "__main__":

    image = list((ROOT / "datasets" / "crop" / "rice").glob("*"))[0]

    prediction = predict_crop(image)

    print("Prediction :", prediction)