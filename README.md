# 🌦️ Weather Helper

A Python-based project that analyzes simple weather data (temperature and humidity) and summarizes the results.  
This project demonstrates environment setup, testing with Pytest & Unittest, and CI/CD automation using GitHub Actions.

---

## 🧩 Features

- Loads local CSV data (`data/weather_data.csv`)
- Computes daily and average temperature/humidity
- Summarizes weather conditions (cold, warm, hot, humid, dry)
- Generates summarized CSV outputs
- Includes both **Pytest** and **Unittest** test suites
- Integrated with **GitHub Actions** for automated testing

---

## 🧪 Testing Frameworks

| Framework | Command | Purpose |
|------------|----------|----------|
| Pytest | `pytest` | Function-level testing |
| Unittest | `python -m unittest discover` | Class-based testing |

---

## ⚙️ CI/CD Workflows

Two GitHub Actions workflows ensure continuous integration:

- **Testing with Pytest** → runs all `test_pytest.py` tests  
- **Python Unittests** → runs `test_unittest.py` suite  

Both workflows are defined under `.github/workflows/` and trigger automatically on every push to `main`.

---

## 🧰 Project Setup

```bash
# 1. Create and activate virtual environment
python -m venv lab_env
source lab_env/bin/activate   # macOS/Linux
lab_env\Scripts\activate      # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run main script
python main.py
```
## 🧪 Testing

This project includes two test frameworks, but only **Unittest** is required to validate functionality. You can run either depending on your setup.

**▶️ Unittest (Recommended)** — Run `python -m unittest discover -s test` to execute all test cases under the `test/` folder.

**▶️ Pytest (Recommendedl)** — Pytest is included to demonstrate additional testing integration. Run `PYTHONPATH=. pytest` (may require setting `PYTHONPATH=.` depending on your environment). **🟡 Note:** In some CI environments,Pytest command may fail so instead it is safe to use the above method
