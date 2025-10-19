# 🚀 START HERE - eCourts Listing Checker

Welcome! This guide will get you up and running in **under 2 minutes**.

---

## ✨ What You Get

✅ **Beautiful Web Interface** - Modern, responsive design  
✅ **Command Line Tool** - For automation and scripting  
✅ **REST API** - JSON endpoints for integration  
✅ **Offline Mode** - Test with sample data (no API needed)  
✅ **Mock Server** - Realistic testing environment  

---

## 🎯 Choose Your Path

### 🌐 Option 1: Web Interface (RECOMMENDED)

**Best for:** Everyone, especially first-time users

**Steps:**
1. Double-click `START_WEB.bat`
2. Open browser: `http://localhost:5000`
3. Start searching!

**Time:** 30 seconds ⚡

---

### 💻 Option 2: Command Line

**Best for:** Developers, automation, scripting

**Steps:**
```bash
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Run a search (offline mode)
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
```

**Time:** 1 minute ⚡

---

### 🔧 Option 3: Mock API Server

**Best for:** Testing API integration

**Terminal 1:**
```bash
python mock_api_server.py
```

**Terminal 2:**
```bash
set ECOURTS_API_BASE=http://localhost:5001
python web_app.py
```

**Time:** 2 minutes ⚡

---

## 📚 Documentation

| Guide | Purpose |
|-------|---------|
| **WEB_GUIDE.md** | Complete web interface documentation |
| **TESTING_GUIDE.md** | CLI testing and examples |
| **QUICK_START.md** | Quick reference card |
| **README.md** | Full project documentation |

---

## 🎯 Sample Test Cases

Try these CNRs in the web interface or CLI:

### Court 101 (District Court Kadapa)
- `ABCD1234567890123` - CIV 123/2024
- `WXYZ9876543210987` - CRLP 456/2023
- `PQRS5555666677778` - CIV 789/2024

### Court 102 (High Court AP)
- `HCAP1111222233334` - WP 1001/2024

---

## 🎨 Screenshots

### Web Interface Features:
- 🔍 **Search Page** - Clean, intuitive form
- 📊 **Results Page** - Detailed case information
- 📋 **Cause List** - Complete court listings
- ℹ️ **About Page** - System information

---

## 🚀 Quick Commands

### Web Interface:
```bash
# Start web app (offline mode)
START_WEB.bat

# Or manually:
set OFFLINE_MODE=true
python web_app.py
```

### CLI:
```bash
# Search by CNR
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline

# View cause list
python -m src.cli --causelist --court-id 101 --when today --offline
```

### Mock Server:
```bash
# Start mock API
python mock_api_server.py

# Test health endpoint
curl http://localhost:5001/health
```

---

## 📁 Project Structure

```
d:/ecourt/
├── 🌐 WEB INTERFACE
│   ├── web_app.py              # Main web application
│   ├── templates/              # HTML templates
│   └── START_WEB.bat          # Quick launcher
│
├── 💻 CLI TOOLS
│   ├── src/cli.py             # Command-line interface
│   ├── src/ecourts_api.py     # API wrapper
│   └── src/utils.py           # Utilities
│
├── 🔧 TESTING
│   ├── mock_api_server.py     # Mock API server
│   ├── sample_data/           # Sample JSON files
│   └── RUN_PROJECT.bat        # CLI launcher
│
└── 📚 DOCUMENTATION
    ├── START_HERE.md          # This file!
    ├── WEB_GUIDE.md           # Web interface guide
    ├── TESTING_GUIDE.md       # CLI testing guide
    ├── QUICK_START.md         # Quick reference
    └── README.md              # Full documentation
```

---

## 🎓 Learning Path

### Day 1: Get Started (5 minutes)
1. ✅ Run `START_WEB.bat`
2. ✅ Try searching with sample CNR
3. ✅ View a cause list

### Day 2: Explore CLI (10 minutes)
1. ✅ Run CLI commands
2. ✅ Check output files in `outputs/`
3. ✅ Try different search options

### Day 3: Advanced (15 minutes)
1. ✅ Start mock API server
2. ✅ Test API endpoints with curl
3. ✅ Customize sample data

---

## 🐛 Troubleshooting

### Web app won't start?
```bash
# Check if port 5000 is busy
netstat -ano | findstr :5000

# Use different port
# Edit web_app.py, change port to 5001
```

### Dependencies missing?
```bash
pip install -r requirements.txt
```

### Can't find templates?
```bash
# Make sure you're in the right directory
cd d:\ecourt
python web_app.py
```

---

## 💡 Pro Tips

1. **Use Offline Mode** for testing - no API needed!
2. **Check outputs/ folder** for saved results
3. **Try the About page** for API documentation
4. **Use mock server** for realistic testing
5. **Customize sample_data/** for your test cases

---

## 🎯 Next Steps

After you're comfortable with the basics:

1. 📖 Read **WEB_GUIDE.md** for advanced web features
2. 🧪 Read **TESTING_GUIDE.md** for CLI mastery
3. 🔌 Integrate with real eCourts API (when available)
4. 🎨 Customize the UI colors and styling
5. 🚀 Deploy to production server

---

## ❓ Need Help?

- **Web Interface:** See `WEB_GUIDE.md`
- **CLI Usage:** See `TESTING_GUIDE.md`
- **Quick Reference:** See `QUICK_START.md`
- **Full Docs:** See `README.md`

---

## 🎉 You're Ready!

**Choose your path above and start exploring!**

The easiest way: Just double-click `START_WEB.bat` 🚀

---

**Happy Searching! ⚖️**
