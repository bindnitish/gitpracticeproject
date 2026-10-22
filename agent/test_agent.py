from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agent.agent import SmartAgricultureAgent

agent = SmartAgricultureAgent()

decision = agent.run(
    crop_prediction="rice",
    weather_prediction="rain"
)

print("=" * 50)
print("SMART AGRICULTURE AGENT")
print("=" * 50)

for key, value in decision.items():
    print(f"{key:<12}: {value}")