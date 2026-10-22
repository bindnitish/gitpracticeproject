from pathlib import Path
import sys

# ==========================
# Project Root
# ==========================
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# ==========================
# AI Models
# ==========================
from inference.predict_crop import predict_crop
from inference.predict_weather import predict_weather

# ==========================
# Agent
# ==========================
from agent.agent import SmartAgricultureAgent

# ==========================
# IoT
# ==========================
from iot.irrigation import control_irrigation
from iot.fertilizer import control_fertilizer
from iot.alert import send_alert

# ==========================
# Sample Images
# ==========================
crop_image = list((ROOT / "datasets" / "crop" / "rice").glob("*"))[0]

weather_image = list((ROOT / "datasets" / "weather" / "rain").glob("*"))[0]

# ==========================
# AI Prediction
# ==========================
crop_prediction = predict_crop(crop_image)

weather_prediction = predict_weather(weather_image)

# ==========================
# Agent Decision
# ==========================
agent = SmartAgricultureAgent()

decision = agent.run(
    crop_prediction,
    weather_prediction
)

# ==========================
# Display
# ==========================
print("=" * 60)
print("SMART AGRICULTURE SYSTEM")
print("=" * 60)

print(f"Crop Prediction    : {crop_prediction}")
print(f"Weather Prediction : {weather_prediction}")

print()

print("Agent Decision")
print("-" * 60)

print(f"Irrigation : {decision['irrigation']}")
print(f"Fertilizer : {decision['fertilizer']}")
print(f"Action     : {decision['action']}")

print()

# ==========================
# IoT Actions
# ==========================
control_irrigation(decision["irrigation"])

control_fertilizer(decision["fertilizer"])

send_alert(decision["action"])

print()
print("=" * 60)
print("SMART AGRICULTURE PIPELINE COMPLETED")
print("=" * 60)