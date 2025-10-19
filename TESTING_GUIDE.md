# eCourts Listing Checker - Testing Guide

This guide shows you how to test the project using **three different methods**.

---

## Method 1: Offline Mode (Easiest - No Server Required)

Use local sample JSON files without any API server.

### Steps:

1. **Activate virtual environment** (if not already active):
   ```bash
   venv\Scripts\activate
   ```

2. **Run with `--offline` flag**:
   ```bash
   # Check a case by CNR (offline mode)
   python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline

   # Check another case
   python -m src.cli --cnr WXYZ9876543210987 --when today --court-id 101 --offline

   # Check by case type/number/year
   python -m src.cli --case-type CIV --number 123 --year 2024 --when today --court-id 101 --offline

   # Download full cause list
   python -m src.cli --causelist --court-id 101 --when today --offline
   ```

3. **Check results**:
   - Results are saved in `outputs/` folder
   - Open the JSON files to see the case details

### Available Sample Cases (Offline Mode):

**Court 101 (District Court - Kadapa):**
- CNR: `ABCD1234567890123` - CIV 123/2024
- CNR: `WXYZ9876543210987` - CRLP 456/2023
- CNR: `PQRS5555666677778` - CIV 789/2024

**Court 102 (High Court - Andhra Pradesh):**
- CNR: `HCAP1111222233334` - WP 1001/2024

---

## Method 2: Mock API Server (Realistic Testing)

Run a local Flask server that simulates the eCourts API.

### Steps:

1. **Open TWO terminal windows** (both with virtual environment activated)

2. **Terminal 1 - Start the Mock API Server**:
   ```bash
   venv\Scripts\activate
   python mock_api_server.py
   ```
   
   You should see:
   ```
   ============================================================
   Mock eCourts API Server Starting...
   ============================================================
   Server URL: http://localhost:5001
   ...
   ```

3. **Terminal 2 - Run the CLI with Mock Server**:
   ```bash
   venv\Scripts\activate
   set ECOURTS_API_BASE=http://localhost:5001
   
   # Now run your queries
   python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101
   
   # Check another case
   python -m src.cli --cnr WXYZ9876543210987 --when today --court-id 101
   
   # Download full cause list
   python -m src.cli --causelist --court-id 101 --when today
   ```

4. **Test the health endpoint**:
   Open browser and go to: `http://localhost:5001/health`

### Available Sample Cases (Mock Server):

Same as offline mode - see list above.

---

## Method 3: Real eCourts API (Production)

If you have access to a real eCourts API:

1. **Set the API base URL**:
   ```bash
   set ECOURTS_API_BASE=https://your-real-api-url.com
   set ECOURTS_API_KEY=your-api-key-if-needed
   ```

2. **Run normally**:
   ```bash
   python -m src.cli --cnr YOUR_REAL_CNR --when today --court-id YOUR_COURT_ID
   ```

---

## Testing the Flask API Endpoint

The project includes a Flask API (`src/app.py`) that you can test.

### With Mock Server Running:

1. **Start mock server** (Terminal 1):
   ```bash
   python mock_api_server.py
   ```

2. **Start Flask API** (Terminal 2):
   ```bash
   set ECOURTS_API_BASE=http://localhost:5001
   set FLASK_APP=src.app
   flask run
   ```

3. **Test with curl or browser** (Terminal 3):
   ```bash
   # GET request
   curl "http://localhost:5000/check?cnr=ABCD1234567890123&when=today&court_id=101"
   
   # Or open in browser:
   # http://localhost:5000/check?cnr=ABCD1234567890123&when=today&court_id=101
   ```

### With Offline Mode:

You can also test the Flask API in offline mode by setting the environment variable:

```bash
set OFFLINE_MODE=true
set FLASK_APP=src.app
flask run
```

---

## Expected Output

### Successful Case Found:

```
Checking date: 2025-10-19
Saved cause list to D:\ecourt\outputs\causelist_101_2025-10-19.json
Saved query summary to D:\ecourt\outputs\query_result_ABCD1234567890123_20251019100445.json
Case listed. See details in the saved JSON.
```

### Case Not Found:

```
Checking date: 2025-10-19
No matching case found in the cause list for this date.
Saved query summary to D:\ecourt\outputs\query_result_query_20251019100500.json
Case not listed on the requested date(s).
```

---

## Troubleshooting

### Error: "Failed to fetch cause list"
- **Solution**: Use `--offline` flag OR start the mock server first

### Error: "No module named 'src'"
- **Solution**: Make sure you're in the `d:\ecourt` directory and virtual environment is activated

### Error: "Failed to resolve example-ecourts-api.example.com"
- **Solution**: Either use `--offline` flag OR set `ECOURTS_API_BASE` to mock server URL

### Mock server not starting
- **Solution**: Make sure port 5001 is not in use. Change port in `mock_api_server.py` if needed

---

## Quick Test Commands

### Test Everything (Offline Mode):

```bash
# Activate environment
venv\Scripts\activate

# Test 1: Check specific case
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline

# Test 2: Check by case number
python -m src.cli --case-type CIV --number 123 --year 2024 --when today --court-id 101 --offline

# Test 3: Download full cause list
python -m src.cli --causelist --court-id 101 --when today --offline

# Test 4: Check for tomorrow
python -m src.cli --cnr WXYZ9876543210987 --when tomorrow --court-id 101 --offline

# Test 5: Check both today and tomorrow
python -m src.cli --cnr PQRS5555666677778 --when both --court-id 101 --offline
```

### Check Results:

```bash
# View output files
dir outputs

# View a result file (replace with actual filename)
type outputs\query_result_ABCD1234567890123_20251019100445.json
```

---

## Next Steps

1. ✅ Test with offline mode first (easiest)
2. ✅ Try the mock server (more realistic)
3. ✅ Integrate with real API when available
4. ✅ Customize the sample data in `sample_data/` folder
5. ✅ Modify `mock_api_server.py` to add more test cases

Happy Testing! 🎉
