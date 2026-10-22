from irrigation import control_irrigation
from fertilizer import control_fertilizer
from alert import send_alert

print("=" * 60)
print("SMART AGRICULTURE IoT TEST")
print("=" * 60)

control_irrigation("OFF")

control_fertilizer("Delay")

send_alert(
    "Heavy rain detected.\nCheck field drainage."
)