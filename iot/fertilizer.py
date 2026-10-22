def control_fertilizer(status):

    if status.lower() == "delay":
        print("⏳ Fertilizer : Delay Application")

    elif status.lower() == "apply if required":
        print("🌱 Fertilizer : Apply if Required")

    else:
        print("⚠ Fertilizer : No Recommendation")