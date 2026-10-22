from agent.rules import RULES


def get_decision(crop, weather):

    key = (crop.lower(), weather.lower())

    if key in RULES:
        return RULES[key]

    return {
        "irrigation": "Unknown",
        "fertilizer": "Unknown",
        "action": "No Rule Available"
    }