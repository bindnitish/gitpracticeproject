import torch

from crop_model import CropModel

model = CropModel()

print(model)

dummy = torch.randn(1, 3, 224, 224)

output = model(dummy)

print("=" * 50)
print("Output Shape:", output.shape)