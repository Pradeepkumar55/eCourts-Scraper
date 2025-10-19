# Troubleshooting Guide - eCourts Listing Checker

## Problem: "Today" and "Tomorrow" searches show no data

### ✅ Solution

The issue occurs when the web app cannot connect to the mock API server. Follow these steps:

### Step 1: Stop All Running Servers
- Press `Ctrl+C` in all terminal windows running the app
- Close any command windows

### Step 2: Start Everything Correctly
Double-click: **`START_WITH_MOCK_API.bat`**

This will:
1. Start the Mock API Server on port 5001
2. Start the Web App on port 5000 (configured to use the mock server)

### Step 3: Verify Setup
Open browser and go to: `http://localhost:5000`

### Step 4: Test with Sample Data

**For CNR Search:**
- CNR: `ABCD1234567890123`
- Court ID: `101`
- When: `Today`
- Click "Search"

**For Cause List:**
- Go to "Cause List" page
- Court ID: `101`
- When: `Today`
- Click "Get Cause List"

---

## Common Issues

### Issue 1: "No data found"

**Cause:** Web app is not connected to mock server

**Fix:**
1. Check if mock server is running (you should see a separate window)
2. Restart using `START_WITH_MOCK_API.bat`

### Issue 2: "Connection Error" or "Max retries exceeded"

**Cause:** Web app is trying to connect to fake API URL

**Fix:**
1. Stop the web app
2. Use `START_WITH_MOCK_API.bat` instead of running `python web_app.py` directly

### Issue 3: Mock server starts but web app doesn't connect

**Cause:** Environment variable not set

**Fix:**
Run these commands in PowerShell:
```powershell
# Stop current web app (Ctrl+C)
$env:ECOURTS_API_BASE="http://localhost:5001"
python web_app.py
```

---

## Manual Setup (Advanced)

If the batch file doesn't work, follow these manual steps:

### Terminal 1 - Mock API Server
```powershell
cd d:\ecourt
python mock_api_server.py
```
Keep this running!

### Terminal 2 - Web Application
```powershell
cd d:\ecourt
$env:ECOURTS_API_BASE="http://localhost:5001"
python web_app.py
```

---

## Verify Everything is Working

### Method 1: Use Test Script
Double-click: `TEST_SETUP.bat`

### Method 2: Manual Check

**Check Mock Server:**
Open browser: `http://localhost:5001/health`

Should show:
```json
{
  "status": "healthy",
  "message": "Mock eCourts API Server is running",
  "available_courts": ["101", "102"]
}
```

**Check Web App:**
Open browser: `http://localhost:5000/api/health`

Should show:
```json
{
  "status": "healthy",
  "offline_mode": false,
  "message": "eCourts Listing Checker Web App is running"
}
```

---

## Available Test Data

### Court 101 - District Court, Kadapa

| CNR | Case No | Type | Serial No |
|-----|---------|------|-----------|
| ABCD1234567890123 | CIV 123/2024 | Civil | 15 |
| WXYZ9876543210987 | CRLP 456/2023 | Criminal | 22 |
| PQRS5555666677778 | CIV 789/2024 | Civil | 8 |

### Court 102 - High Court, Andhra Pradesh

| CNR | Case No | Type | Serial No |
|-----|---------|------|-----------|
| HCAP1111222233334 | WP 1001/2024 | Writ Petition | 5 |

---

## Alternative: Use Offline Mode

If you don't want to use the mock server, you can use offline mode with sample data files:

### Step 1: Check Sample Data
Make sure files exist in `sample_data/` folder:
- `causelist_101_today.json`
- `causelist_102_today.json`

### Step 2: Start in Offline Mode
Double-click: **`START_WEB.bat`**

This uses local JSON files instead of the API.

---

## Still Having Issues?

### Check Python Version
```powershell
python --version
```
Should be Python 3.7 or higher

### Check Dependencies
```powershell
pip install -r requirements.txt
```

### Check Ports
Make sure ports 5000 and 5001 are not in use:
```powershell
netstat -ano | findstr :5000
netstat -ano | findstr :5001
```

If ports are in use, kill the processes or change ports in the code.

---

## Quick Reference

| File | Purpose |
|------|---------|
| `START_WITH_MOCK_API.bat` | **Best option** - Starts both servers correctly |
| `START_WEB.bat` | Offline mode (no API needed) |
| `TEST_SETUP.bat` | Verify everything is working |
| `SAMPLE_DATA.html` | Interactive test data (click to copy) |

---

## Contact

If you're still experiencing issues, check:
1. Are both servers running?
2. Is the web app showing "API Base URL: http://localhost:5001"?
3. Can you access http://localhost:5001/health in your browser?

All three should be YES for the system to work correctly.
