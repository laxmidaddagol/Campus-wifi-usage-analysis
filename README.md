# Campus Wi-Fi Usage Analysis

**One-line:** Analyze campus Wi‑Fi connection logs to find peak hours, device mix, and high-traffic locations.

## What this repo contains
- `data/wifi_logs.csv` — synthetic sample dataset (generated for demonstration)
- `scripts/analyze_wifi.py` — a concise, human-written analysis script
- `results/` — where charts and CSV summaries are saved after running the script
- `requirements.txt`
- `.gitignore`, `LICENSE`

## Quick start

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate
   pip install -r requirements.txt
   ```

2. Run the analysis:
   ```bash
   python scripts/analyze_wifi.py --input data/wifi_logs.csv --out results/
   ```

3. Open the `results/` folder to view:
   - `usage_by_hour.png`
   - `device_distribution.png`
   - `location_usage.png`
   - summary CSVs for each analysis

## About the dataset
The included dataset is synthetic and intended to demonstrate the analysis pipeline. Replace `data/wifi_logs.csv` with real logs when available. Expected columns:
- `timestamp` (YYYY-MM-DD HH:MM:SS)
- `device_id`
- `user_type` (student/faculty/staff)
- `location`
- `device_type` (Smartphone, Laptop, Tablet, IoT Device)

## How to present this on your resume
- *“Analyzed 5K+ campus Wi-Fi connection records to identify peak hours, device distribution, and high-traffic locations. Automated visual report generation using Python (pandas, matplotlib).”*

## License
MIT — see LICENSE file.

## Notes
Personalize `README.md` and `scripts/analyze_wifi.py` with your name and any dataset sources before publishing.