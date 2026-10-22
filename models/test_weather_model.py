import torch
from weather_model import WeatherModel

model = WeatherModel()

print(model)

dummy = torch.randn(1, 3, 224, 224)

output = model(dummy)

print("=" * 50)
print("Output Shape :", output.shape)