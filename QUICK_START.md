# eCourts Listing Checker - Quick Start Guide

## ✅ Project is Ready to Run!

---

## 🚀 Fastest Way to Test (30 seconds)

### Option 1: Use the Batch File (Windows)
Just double-click: **`RUN_PROJECT.bat`**

### Option 2: Manual Commands

```bash
# 1. Activate virtual environment (if not already active)
venv\Scripts\activate

# 2. Run a test query (offline mode - no server needed)
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
```

**That's it!** Check the `outputs/` folder for results.

---

## 📋 Sample Test Commands

```bash
# Test 1: Check by CNR
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline

# Test 2: Check by Case Type/Number/Year
python -m src.cli --case-type CIV --number 123 --year 2024 --when today --court-id 101 --offline

# Test 3: Download full cause list
python -m src.cli --causelist --court-id 101 --when today --offline

# Test 4: Check for tomorrow
python -m src.cli --cnr WXYZ9876543210987 --when tomorrow --court-id 101 --offline

# Test 5: Check both today and tomorrow
python -m src.cli --cnr PQRS5555666677778 --when both --court-id 101 --offline
```

---

## 🎯 Available Sample Cases (for testing)

### Court 101 - District Court Kadapa
- **CNR:** `ABCD1234567890123` → CIV 123/2024 (Ram Kumar vs Shyam Singh)
- **CNR:** `WXYZ9876543210987` → CRLP 456/2023 (State vs Mohan Lal)
- **CNR:** `PQRS5555666677778` → CIV 789/2024 (Lakshmi Devi vs Municipal Corporation)

### Court 102 - High Court Andhra Pradesh
- **CNR:** `HCAP1111222233334` → WP 1001/2024 (Vijay Enterprises vs State of AP)

---

## 🔧 Three Testing Modes

### 1. **Offline Mode** (Easiest - No Server)
Uses local JSON files from `sample_data/` folder.
```bash
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
```

### 2. **Mock Server Mode** (Realistic)
Runs a local Flask API server.

**Terminal 1:**
```bash
python mock_api_server.py
```

**Terminal 2:**
```bash
set ECOURTS_API_BASE=http://localhost:5001
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101
```

### 3. **Real API Mode** (Production)
Connect to actual eCourts API.
```bash
set ECOURTS_API_BASE=https://your-api-url.com
set ECOURTS_API_KEY=your-key-if-needed
python -m src.cli --cnr YOUR_REAL_CNR --when today --court-id YOUR_COURT_ID
```

---

## 📁 Project Structure

```
d:/ecourt/
├── src/                    # Main source code
│   ├── cli.py             # Command-line interface
│   ├── app.py             # Flask API
│   ├── ecourts_api.py     # API wrapper
│   ├── config.py          # Configuration
│   ├── utils.py           # Utilities
│   └── downloader.py      # File downloads
├── sample_data/           # Sample JSON files
├── outputs/               # Query results (auto-created)
├── downloads/             # Downloaded PDFs (auto-created)
├── mock_api_server.py     # Mock API for testing
├── RUN_PROJECT.bat        # Quick start script
├── TESTING_GUIDE.md       # Detailed testing guide
└── README.md              # Full documentation
```

---

## 📊 Check Results

```bash
# List output files
dir outputs

# View a result file
type outputs\query_result_ABCD1234567890123_20251019100935.json
```

---

## 🐛 Common Issues

| Issue | Solution |
|-------|----------|
| "No module named 'dateutil'" | Run: `pip install -r requirements.txt` |
| "Failed to fetch cause list" | Add `--offline` flag or start mock server |
| "Failed to resolve example-ecourts-api.example.com" | Use `--offline` mode or set `ECOURTS_API_BASE` |

---

## 📚 More Information

- **Full Testing Guide:** See `TESTING_GUIDE.md`
- **Project Documentation:** See `README.md`
- **Sample Data:** Check `sample_data/` folder
- **Mock Server:** Run `python mock_api_server.py`

---

## ✨ Next Steps

1. ✅ Test with offline mode (done!)
2. ✅ Try the mock server
3. ✅ Customize sample data in `sample_data/`
4. ✅ Integrate with real eCourts API when available
5. ✅ Test the Flask API endpoint (`src/app.py`)

---

**Need Help?** Check `TESTING_GUIDE.md` for detailed instructions!

Happy Testing! 🎉
