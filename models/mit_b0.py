import timm
import torch.nn as nn

# =====================================
# Crop Classification Model
# =====================================

class CropModel(nn.Module):

    def __init__(self, num_classes=5):
        super().__init__()

        # Load MiT-B0 Backbone
        self.backbone = timm.create_model(
            "mit_b0",
            pretrained=True,
            num_classes=0
        )

        # Classification Head
        self.classifier = nn.Linear(
            self.backbone.num_features,
            num_classes
        )

    def forward(self, x):

        x = self.backbone(x)

        x = self.classifier(x)

        return x