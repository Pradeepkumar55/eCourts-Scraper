# ✅ Fixed: Offline Mode is Now Default

## What Was Fixed

The application now defaults to **offline mode** (using sample data) instead of trying to connect to a non-existent API. This means it works out of the box without any configuration!

---

## Changes Made

### 1. **CLI (src/cli.py)**
- ✅ Offline mode is now the **default**
- ✅ Added `--online` flag to explicitly enable online mode
- ✅ No need to add `--offline` flag anymore

### 2. **Web App (web_app.py)**
- ✅ Changed default `OFFLINE_MODE` from `"false"` to `"true"`
- ✅ Web interface now works immediately with sample data

### 3. **Documentation (README.md)**
- ✅ Updated examples to reflect offline mode as default
- ✅ Added note about using `--online` flag for real API

---

## How to Use Now

### ✨ Easy Mode (Just Works!)

**Command Line:**
```bash
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101
```
No `--offline` flag needed! It's the default.

**Web Interface:**
```bash
# Just double-click START_WEB.bat or run:
python web_app.py
```
Opens at http://localhost:5000 with sample data ready to use.

---

## When You Want to Use Real API

### Command Line:
```bash
# Add --online flag
python -m src.cli --cnr YOUR_REAL_CNR --when today --court-id 101 --online
```

### Web Interface:
```bash
# Set environment variable before starting
set OFFLINE_MODE=false
set ECOURTS_API_BASE=https://your-api-url.com
python web_app.py
```

---

## Testing Modes Summary

| Mode | CLI Command | Web App |
|------|-------------|---------|
| **Offline (Default)** | `python -m src.cli --cnr ... --court-id 101` | `python web_app.py` |
| **Online** | `python -m src.cli --cnr ... --court-id 101 --online` | `set OFFLINE_MODE=false` then `python web_app.py` |
| **Mock Server** | `set ECOURTS_API_BASE=http://localhost:5001` then run CLI | Same as online with mock URL |

---

## Sample Test Cases (Work Immediately!)

```bash
# Test 1: Check by CNR
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101

# Test 2: Check by Case Type/Number/Year
python -m src.cli --case-type CIV --number 123 --year 2024 --when today --court-id 101

# Test 3: Download full cause list
python -m src.cli --causelist --court-id 101 --when today

# Test 4: Check for tomorrow
python -m src.cli --cnr WXYZ9876543210987 --when tomorrow --court-id 101

# Test 5: Check both today and tomorrow
python -m src.cli --cnr PQRS5555666677778 --when both --court-id 101
```

All commands work without `--offline` flag!

---

## Benefits

✅ **No configuration needed** - works immediately after setup
✅ **No API errors** - uses reliable local sample data
✅ **Easy testing** - perfect for development and demos
✅ **Still flexible** - can switch to online mode when needed

---

**Happy Testing! 🎉**
