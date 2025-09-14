"""analyze_wifi.py
Human-focused, readable script to analyze campus Wi-Fi logs.

This script:
- computes peak hours
- summarizes device type distribution
- summarizes location-wise usage
- saves plots to a results/ folder

Usage:
    python scripts/analyze_wifi.py --input data/wifi_logs.csv --out results/
"""

import argparse
import logging
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path, parse_dates=["timestamp"])
    logging.info("Loaded %d rows from %s", len(df), path)
    return df

def ensure_results(out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir

def summarize_peak_hours(df):
    df = df.copy()
    df["hour"] = df["timestamp"].dt.hour
    summary = df.groupby("hour").size().rename("connections")
    return summary

def device_type_distribution(df):
    return df["device_type"].value_counts()

def location_usage(df):
    return df["location"].value_counts()

def save_bar(series, title, xlabel, ylabel, out_path):
    plt.figure(figsize=(8, 4))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def save_pie(series, title, out_path):
    plt.figure(figsize=(6, 6))
    series.plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main(args):
    df = load_data(args.input)
    out_dir = ensure_results(args.out)

    # Peak hours
    peak = summarize_peak_hours(df)
    logging.info("Top hours (by connections):\n%s", peak.sort_values(ascending=False).head(5).to_string())
    save_bar(peak, "Wi-Fi Usage by Hour", "Hour of Day", "Connections", out_dir / "usage_by_hour.png")

    # Device types
    devices = device_type_distribution(df)
    logging.info("Device distribution:\n%s", devices.to_string())
    save_pie(devices, "Device Type Distribution", out_dir / "device_distribution.png")

    # Locations
    locs = location_usage(df)
    logging.info("Top locations:\n%s", locs.head(10).to_string())
    save_bar(locs.head(20), "Wi-Fi Usage by Location (Top 20)", "Location", "Connections", out_dir / "location_usage.png")

    # small CSV summary files
    peak.to_csv(out_dir / "peak_hours_summary.csv", header=True)
    devices.to_csv(out_dir / "device_distribution_summary.csv", header=True)
    locs.to_csv(out_dir / "location_usage_summary.csv", header=True)

    logging.info("All outputs written to %s", out_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze campus Wi-Fi usage logs.")
    parser.add_argument("--input", required=True, help="Path to wifi_logs.csv")
    parser.add_argument("--out", required=True, help="Output directory for results")
    args = parser.parse_args()
    main(args)