from src.weather_helper import load_weather_data, summarize_weather, save_weather_summary
import os

def main():
    # Dynamically find the absolute path of the current folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "data", "weather_data.csv")
    output_file = os.path.join(base_dir, "data", "summarized_weather.csv")

    print("🌤️  Loading data...")
    data = load_weather_data(input_file)
    print(f"✅ Loaded {len(data)} records from {input_file}")

    print("🔍  Summarizing weather conditions...")
    summary = summarize_weather(data)

    print("💾  Saving results...")
    save_weather_summary(summary, output_file)

    print(f"✅  Process completed! {len(summary)} records summarized.")
    print(f"📄  Output saved to: {output_file}")

    for record in summary[:3]:
        print(record)

if __name__ == "__main__":
    main()
