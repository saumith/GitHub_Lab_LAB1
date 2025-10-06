"""
Weather Helper Module
---------------------
Provides functions to classify weather conditions and
analyze temperature/humidity comfort metrics.
"""

import csv
import os

def classify_temperature(temp_c):
    """Classify temperature into categories."""
    if temp_c < 0:
        return "freezing"
    elif 0 <= temp_c < 10:
        return "cold"
    elif 10 <= temp_c < 25:
        return "moderate"
    elif 25 <= temp_c < 35:
        return "warm"
    else:
        return "hot"


def humidity_status(humidity):
    """Return humidity condition."""
    if humidity < 30:
        return "dry"
    elif 30 <= humidity <= 60:
        return "comfortable"
    else:
        return "humid"


def comfort_index(temp_c, humidity):
    """
    Simple comfort metric combining temperature and humidity.
    Returns a float value between 0 (bad) and 1 (comfortable).
    """
    if not (0 <= humidity <= 100):
        raise ValueError("Humidity must be between 0 and 100")
    score = 1 - (abs(temp_c - 22) / 50 + abs(humidity - 50) / 100)
    return round(max(0, min(score, 1)), 2)


def summarize_weather(data_list):
    """
    Accepts a list of (temp_c, humidity) tuples and
    returns a list of dictionaries summarizing each reading.
    """
    summary = []
    for temp, hum in data_list:
        summary.append({
            "temperature": temp,
            "humidity": hum,
            "temp_label": classify_temperature(temp),
            "humidity_label": humidity_status(hum),
            "comfort": comfort_index(temp, hum)
        })
    return summary


def load_weather_data(file_path):
    """
    Load temperature and humidity data from a CSV file.
    Expected columns: temperature, humidity
    Returns a list of (temp_c, humidity) tuples.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                temp = float(row["temperature"])
                hum = float(row["humidity"])
                data.append((temp, hum))
            except (KeyError, ValueError):
                continue
    return data


def save_weather_summary(summary, output_path):
    """
    Save summarized weather data (list of dicts) to a CSV file.
    """
    if not summary:
        raise ValueError("Summary data is empty")

    fieldnames = ["temperature", "humidity", "temp_label", "humidity_label", "comfort"]
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary)
