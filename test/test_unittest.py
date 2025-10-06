import unittest
from src.weather_helper import *

class TestWeatherHelper(unittest.TestCase):
    def test_classify_temperature(self):
        self.assertEqual(classify_temperature(0), "cold")
        self.assertEqual(classify_temperature(28), "warm")

    def test_humidity_status(self):
        self.assertEqual(humidity_status(25), "dry")
        self.assertEqual(humidity_status(55), "comfortable")

    def test_comfort_index(self):
        self.assertAlmostEqual(comfort_index(22, 50), 1.0)
        self.assertRaises(ValueError, comfort_index, 22, 150)

    def test_summarize_weather(self):
        result = summarize_weather([(10, 40)])
        self.assertEqual(result[0]["temp_label"], "moderate")

if __name__ == "__main__":
    unittest.main()
