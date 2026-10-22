from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agent.decision_engine import get_decision

crop = "rice"
weather = "rain"

decision = get_decision(crop, weather)

print("=" * 50)
print("Agentic AI Decision")
print("=" * 50)

print("Crop       :", crop)
print("Weather    :", weather)
print("Irrigation :", decision["irrigation"])
print("Fertilizer :", decision["fertilizer"])
print("Action     :", decision["action"])