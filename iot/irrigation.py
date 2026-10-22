def control_irrigation(status):

    if status.upper() == "ON":
        print("💧 Irrigation Pump : ON")

    elif status.upper() == "OFF":
        print("🚫 Irrigation Pump : OFF")

    else:
        print("⚠ Unknown Irrigation Status")