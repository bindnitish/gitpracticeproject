import timm
import torch.nn as nn


class WeatherModel(nn.Module):

    def __init__(self, num_classes=11):
        super().__init__()

        self.backbone = timm.create_model(
            "efficientnet_b0",
            pretrained=True,
            num_classes=0
        )

        self.classifier = nn.Linear(
            self.backbone.num_features,
            num_classes
        )

    def forward(self, x):

        x = self.backbone(x)

        x = self.classifier(x)

        return x
