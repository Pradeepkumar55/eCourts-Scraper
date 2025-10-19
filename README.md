# eCourts Listing Checker

**What this project does**

- Accepts a case query (CNR or Case Type + Number + Year) via CLI.
- Checks whether the case is listed **today** or **tomorrow** (or both).
- If listed, prints **serial number** and **court name**.
- Optionally downloads associated case PDF(s) if available.
- Optionally downloads the entire cause list for a court/date and saves it as JSON.
- Saves summary results as JSON files into `outputs/`.
- Includes an optional Flask API (`app.py`) that exposes the check as an endpoint.

---

## Quick start

### 🌐 Web Interface (Easiest!)

1. **Double-click:** `START_WEB.bat` (Windows)
2. **Open browser:** `http://localhost:5000`
3. **Start searching!** ✨

### 💻 Command Line Interface

1. Clone repository or extract ZIP.

2. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure API:

The project is designed to work with a public eCourts JSON API. The API URL is configured in `src/config.py` as `API_BASE`.

If you have an API provider or wrapper, set `API_BASE` to its base URL or set environment variable `ECOURTS_API_BASE`.

5. Example CLI usage:

**Note:** The CLI now defaults to **offline mode** (using sample data). To connect to a real API, add the `--online` flag.

```bash
# Check by CNR for today (offline mode - default)
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101

# Check by case type/number/year for tomorrow
python -m src.cli --case-type CIV --number 123 --year 2024 --when tomorrow --court-id 101

# Download full cause list for given court/date
python -m src.cli --causelist --court-id 101 --when today

# Use online mode with real API
python -m src.cli --cnr YOUR_CNR --when today --court-id 101 --online
```

6. Run the Flask API (optional):

```bash
export FLASK_APP=src.app    # macOS/Linux
set FLASK_APP=src.app       # Windows
flask run
```

Then POST or GET `/check` with query params (see README section "Flask API").

---

## Files in this project

- `requirements.txt` - Python dependencies
- `src/cli.py` - Command-line interface
- `src/config.py` - API configuration (set API_BASE here)
- `src/ecourts_api.py` - Thin wrapper around the chosen public eCourts API
- `src/downloader.py` - File download helpers
- `src/utils.py` - Utility functions (date helpers, saving JSON)
- `src/app.py` - Simple Flask API
- `.gitignore`
- `examples/` - sample output files

---

## Notes about the API

- There is no single official public JSON API for every eCourts feature. Many community wrappers exist. This project uses a configurable `API_BASE` and example endpoint patterns.
- If your chosen API uses different path or parameter names, update `src/config.py` or `src/ecourts_api.py` accordingly.
- If an API is unavailable for a particular court/date, the tool will report that the cause list could not be retrieved and save the raw response (if any) under `outputs/`.

---

## Limitations and legal considerations

This project uses public APIs. Do NOT attempt to bypass CAPTCHA on the official eCourts website. If you need direct official access, obtain API credentials from the appropriate authority.

---

## Submission checklist

- README.md (this file)
- `src/` code files
- Example runs in `examples/`
- `requirements.txt`

---

## Contact / Support

If something doesn't work, paste the exact CLI command you ran and any error messages; I can help adapt the parsing to fit the API you choose.
"# eCourts-Scraper" 
"# eCourts-Scraper" 
"# eCourts-Scraper" 
