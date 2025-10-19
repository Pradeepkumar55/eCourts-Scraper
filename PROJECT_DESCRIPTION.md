# eCourts Listing Checker - Project Description

## 📋 Overview

**eCourts Listing Checker** is a comprehensive web application and command-line tool designed to help lawyers, litigants, and court staff check case listings from Indian eCourts services. The system allows users to search for specific cases and view daily cause lists across multiple courts.

---

## 🎯 Purpose

The application solves the problem of manually checking court websites for case listings by providing:

1. **Automated Case Search** - Find your case by CNR number or case details
2. **Daily Cause Lists** - View all cases listed for a specific court and date
3. **Multiple Access Methods** - Web interface, REST API, and command-line tool
4. **Offline Testing** - Mock data for development and testing without real API access

---

## ✨ Key Features

### 1. **Web Interface**
- Modern, responsive design with clean UI
- Search cases by CNR (Case Number Reference) or case details
- View full cause lists for any court
- Support for "Today", "Tomorrow", or "Both" date options
- Real-time search results with case details

### 2. **Search Capabilities**
- **By CNR Number**: Direct search using unique case identifier
- **By Case Details**: Search using Case Type, Number, and Year
- **Court-specific**: Filter by Court ID
- **Date-based**: Check listings for today, tomorrow, or both
- **Optional Filters**: State and District filtering

### 3. **Mock API Server**
- Simulates real eCourts API for testing
- Pre-loaded sample data for 4 test cases
- Supports 2 courts (District Court and High Court)
- RESTful endpoints for integration testing

### 4. **Command-Line Interface (CLI)**
- Automation-friendly for scripts and batch processing
- Same search capabilities as web interface
- JSON output for easy parsing
- Offline mode support

### 5. **REST API**
- JSON endpoints for third-party integration
- Health check endpoint for monitoring
- Programmatic access to all features

---

## 🏗️ Architecture

### Components

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Web Browser  │  │  CLI Tool    │  │  REST API    │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
└─────────┼──────────────────┼──────────────────┼─────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Web App       │
                    │  (Flask)        │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  eCourts API    │
                    │   Wrapper       │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
    ┌─────▼─────┐    ┌──────▼──────┐    ┌─────▼─────┐
    │ Mock API  │    │  Real API   │    │  Offline  │
    │  Server   │    │  (External) │    │   Mode    │
    └───────────┘    └─────────────┘    └───────────┘
```

### Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **API Client**: Requests library
- **Data Format**: JSON
- **Testing**: Mock API server with sample data

---

## 📁 Project Structure

```
ecourt/
├── src/                          # Core application code
│   ├── ecourts_api.py           # API wrapper and client
│   ├── cli.py                   # Command-line interface
│   ├── config.py                # Configuration settings
│   ├── utils.py                 # Helper functions
│   └── downloader.py            # PDF download functionality
│
├── templates/                    # HTML templates for web UI
│   ├── index.html               # Home page with search form
│   ├── results.html             # Search results display
│   ├── causelist.html           # Cause list form
│   └── causelist_results.html   # Cause list display
│
├── sample_data/                  # Offline mode data files
│   ├── causelist_101_today.json # Sample data for Court 101
│   └── causelist_102_today.json # Sample data for Court 102
│
├── outputs/                      # Search results saved here
├── downloads/                    # Downloaded PDFs stored here
│
├── web_app.py                   # Main Flask web application
├── mock_api_server.py           # Mock API for testing
│
├── START_WITH_MOCK_API.bat      # Launch with mock server
├── START_WEB.bat                # Launch in offline mode
├── TEST_SETUP.bat               # Verify installation
│
└── Documentation files
    ├── README_FIRST.txt         # Quick start guide
    ├── README.md                # Full documentation
    ├── TROUBLESHOOTING.md       # Problem solving guide
    ├── SAMPLE_DATA.html         # Interactive test data
    └── Various guides...
```

---

## 🔧 How It Works

### Search Flow

1. **User Input**
   - User enters CNR or case details via web form/CLI
   - Selects court ID and date range

2. **API Request**
   - Application queries the configured API endpoint
   - Supports mock server, real API, or offline mode

3. **Data Processing**
   - Receives cause list data in JSON format
   - Searches for matching cases
   - Extracts relevant information

4. **Result Display**
   - Shows case details (case number, serial number, parties, etc.)
   - Displays for each date checked (today/tomorrow)
   - Provides download links for court orders (if available)

### Operating Modes

#### 1. **Mock API Mode** (Recommended for Testing)
- Uses local mock server on port 5001
- Pre-loaded with 4 sample cases
- No internet connection required
- Perfect for development and testing

#### 2. **Online Mode**
- Connects to real eCourts API
- Requires valid API endpoint URL
- Set via `ECOURTS_API_BASE` environment variable

#### 3. **Offline Mode**
- Uses local JSON files from `sample_data/` folder
- No API server needed
- Limited to pre-configured test cases

---

## 📊 Sample Data

### Court 101 - District Court, Kadapa

| CNR | Case No | Type | Serial No | Parties |
|-----|---------|------|-----------|---------|
| ABCD1234567890123 | CIV 123/2024 | Civil | 15 | Ram Kumar vs Shyam Singh |
| WXYZ9876543210987 | CRLP 456/2023 | Criminal | 22 | State vs Mohan Lal |
| PQRS5555666677778 | CIV 789/2024 | Civil | 8 | Lakshmi Devi vs Municipal Corporation |

### Court 102 - High Court, Andhra Pradesh

| CNR | Case No | Type | Serial No | Parties |
|-----|---------|------|-----------|---------|
| HCAP1111222233334 | WP 1001/2024 | Writ Petition | 5 | Vijay Enterprises vs State of AP |

---

## 🚀 Use Cases

### 1. **For Lawyers**
- Check if their cases are listed for hearing
- Get serial numbers for court appearances
- Download cause lists for planning
- Automate daily case checking via CLI

### 2. **For Litigants**
- Track their case status
- Know when to appear in court
- Get hearing dates and serial numbers

### 3. **For Court Staff**
- Verify cause list accuracy
- Cross-reference case information
- Generate reports using API

### 4. **For Developers**
- Test eCourts API integration
- Build custom applications
- Prototype court management systems

---

## 🔐 Security Features

- No hardcoded credentials
- Environment variable support for API keys
- Optional API key authentication
- Local data storage (no cloud dependency)
- Configurable timeout settings

---

## 📈 Benefits

### Efficiency
- ✅ Saves time vs manual website checking
- ✅ Batch processing via CLI
- ✅ Automated notifications possible

### Accuracy
- ✅ Direct API integration (when using real API)
- ✅ Structured data format
- ✅ Reduced manual errors

### Flexibility
- ✅ Multiple access methods (Web/CLI/API)
- ✅ Works offline for testing
- ✅ Customizable and extensible

### User-Friendly
- ✅ Clean, modern web interface
- ✅ Interactive sample data
- ✅ Comprehensive documentation
- ✅ One-click launchers

---

## 🛠️ Configuration Options

### Environment Variables

- **`ECOURTS_API_BASE`** - API endpoint URL (default: mock server)
- **`OFFLINE_MODE`** - Enable offline mode (true/false)
- **`ECOURTS_API_KEY`** - API authentication key (if required)

### Customization

- **API Endpoints** - Configure in `src/config.py`
- **Timeout Settings** - Adjust request timeout
- **Output Directories** - Change save locations
- **Sample Data** - Add more test cases

---

## 📝 API Endpoints

### Mock API Server (Port 5001)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Health check |
| `/cnr/<cnr>` | GET | Search by CNR |
| `/cause-list` | GET | Get cause list (params: court_id, date) |

### Web Application (Port 5000)

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Home page |
| `/search` | POST | Search form submission |
| `/causelist` | GET/POST | Cause list page |
| `/api/search` | POST/GET | JSON search API |
| `/api/health` | GET | Health check |

---

## 🎓 Learning Resources

The project includes extensive documentation:

- **README_FIRST.txt** - Start here for quick setup
- **QUICK_START.md** - 5-minute getting started guide
- **WEB_GUIDE.md** - Complete web interface guide
- **TESTING_GUIDE.md** - CLI usage and testing
- **TROUBLESHOOTING.md** - Common issues and solutions
- **SAMPLE_DATA.html** - Interactive test data browser

---

## 🔄 Future Enhancements

Potential improvements:

1. **Notifications** - Email/SMS alerts for case listings
2. **Calendar Integration** - Sync hearing dates to calendar
3. **Multi-language Support** - Regional language interfaces
4. **Mobile App** - Native iOS/Android applications
5. **Advanced Filters** - Search by advocate, party name, etc.
6. **Analytics Dashboard** - Case statistics and trends
7. **Bulk Operations** - Process multiple CNRs at once
8. **PDF Parsing** - Extract data from court order PDFs

---

## 📞 Support

For issues or questions:

1. Check **TROUBLESHOOTING.md** for common problems
2. Review **README.md** for detailed documentation
3. Use **TEST_SETUP.bat** to verify installation
4. Check the **INDEX.md** for complete file reference

---

## 📄 License

This is a demonstration/educational project for working with eCourts data.

---

## 🙏 Acknowledgments

- Built for Indian eCourts system
- Sample data based on typical court case formats
- Designed for ease of use and testing

---

**Version**: 1.0  
**Last Updated**: October 2025  
**Status**: Production Ready (with mock data for testing)
