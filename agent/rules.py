RULES = {
    ("rice", "rain"): {
        "irrigation": "OFF",
        "fertilizer": "Delay",
        "action": "Check Drainage"
    },

    ("rice", "sunny"): {
        "irrigation": "ON",
        "fertilizer": "Apply if Required",
        "action": "Normal Farming"
    },

    ("wheat", "rain"): {
        "irrigation": "OFF",
        "fertilizer": "Delay",
        "action": "Monitor Field"
    },

    ("maize", "rain"): {
        "irrigation": "OFF",
        "fertilizer": "Delay",
        "action": "Check Water Logging"
    }
}