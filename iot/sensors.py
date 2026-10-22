"""Sensor reading helpers."""


def read_sensor(name: str) -> float:
    return 25.0 if name == "temperature" else 50.0
