from agent.decision_engine import get_decision


class SmartAgricultureAgent:

    def __init__(self):
        pass

    def run(self, crop_prediction, weather_prediction):

        decision = get_decision(
            crop_prediction,
            weather_prediction
        )

        return decision