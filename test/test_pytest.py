import pytest
from src.weather_helper import *

@pytest.mark.parametrize("temp, expected", [
    (-5, "freezing"), (5, "cold"), (15, "moderate"),
    (30, "warm"), (40, "hot")
])
def test_classify_temperature(temp, expected):
    assert classify_temperature(temp) == expected


@pytest.mark.parametrize("humidity, expected", [
    (20, "dry"), (50, "comfortable"), (80, "humid")
])
def test_humidity_status(humidity, expected):
    assert humidity_status(humidity) == expected


def test_comfort_index_valid():
    assert comfort_index(22, 50) == 1.0


def test_comfort_index_invalid_humidity():
    with pytest.raises(ValueError):
        comfort_index(22, 150)


def test_summarize_weather():
    data = [(10, 40), (30, 70)]
    summary = summarize_weather(data)
    assert len(summary) == 2
    assert summary[0]["temp_label"] == "moderate"
    assert summary[1]["humidity_label"] == "humid"


def test_load_weather_data(tmp_path):
    sample_file = tmp_path / "sample.csv"
    sample_file.write_text("temperature,humidity\n20,50\n25,60\n")
    data = load_weather_data(sample_file)
    assert data[0] == (20.0, 50.0)


def test_save_weather_summary(tmp_path):
    summary = [
        {"temperature": 10, "humidity": 40, "temp_label": "moderate",
         "humidity_label": "comfortable", "comfort": 0.9}
    ]
    output = tmp_path / "out.csv"
    save_weather_summary(summary, output)
    assert output.exists()
