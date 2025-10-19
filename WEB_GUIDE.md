# eCourts Listing Checker - Web Interface Guide

## 🌐 Beautiful Web Interface Now Available!

A modern, user-friendly web application for checking eCourts case listings.

---

## 🚀 Quick Start

### Start the Web Application:

```bash
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Run in OFFLINE mode (uses sample data - easiest for testing)
set OFFLINE_MODE=true
python web_app.py

# OR run in ONLINE mode (uses API)
set ECOURTS_API_BASE=http://localhost:5001
python web_app.py
```

### Open in Browser:

```
http://localhost:5000
```

That's it! 🎉

---

## 📸 Features

### 🔍 **Case Search Page** (`/`)
- Search by CNR or Case Type/Number/Year
- Choose date: Today, Tomorrow, or Both
- Enter court details
- Beautiful, intuitive interface
- Sample cases provided for testing

### 📋 **Cause List Page** (`/causelist`)
- View complete cause list for any court
- Filter by date
- See all cases in a clean table format

### 📊 **Results Page**
- Clear display of found cases
- Detailed case information
- Serial numbers highlighted
- Party names, advocates, purpose shown
- Links to PDF documents (if available)

### ℹ️ **About Page** (`/about`)
- System information
- API endpoints documentation
- Technology stack
- Usage instructions

---

## 🎨 Design Features

- **Modern Gradient UI** - Beautiful purple gradient design
- **Responsive Layout** - Works on desktop, tablet, and mobile
- **Clean Typography** - Easy to read with proper hierarchy
- **Color-Coded Alerts** - Success (green), Warning (yellow), Error (red)
- **Smooth Animations** - Hover effects and transitions
- **Intuitive Forms** - Clear labels and helpful hints

---

## 🧪 Testing the Web Interface

### Test 1: Search by CNR (Offline Mode)

1. Start the web app:
   ```bash
   set OFFLINE_MODE=true
   python web_app.py
   ```

2. Open browser: `http://localhost:5000`

3. Enter:
   - **CNR:** `ABCD1234567890123`
   - **Court ID:** `101`
   - **When:** Today

4. Click **Search Case Listing**

5. ✅ You should see the case details with serial number 15

### Test 2: View Full Cause List

1. Click **Cause List** in navigation

2. Enter:
   - **Court ID:** `101`
   - **Date:** Today

3. Click **Get Cause List**

4. ✅ You should see all 3 cases in a table

### Test 3: Search by Case Number

1. Go back to home page

2. Enter:
   - **Case Type:** `CIV`
   - **Case Number:** `123`
   - **Year:** `2024`
   - **Court ID:** `101`
   - **When:** Today

3. Click **Search Case Listing**

4. ✅ You should see the same case as Test 1

---

## 🔌 API Endpoints

The web app also exposes JSON API endpoints:

### 1. Search Case (JSON API)

**Endpoint:** `POST /api/search`

**Request:**
```json
{
  "cnr": "ABCD1234567890123",
  "when": "today",
  "court_id": "101"
}
```

**Response:**
```json
{
  "found": true,
  "listings": [
    {
      "date": "2025-10-19",
      "court": "District Court - Kadapa",
      "serial_no": "15",
      "case": { ... }
    }
  ]
}
```

### 2. Health Check

**Endpoint:** `GET /api/health`

**Response:**
```json
{
  "status": "healthy",
  "offline_mode": true,
  "message": "eCourts Listing Checker Web App is running"
}
```

---

## 🎯 Sample Test Cases

### Court 101 - District Court Kadapa

| CNR | Case No | Parties |
|-----|---------|---------|
| `ABCD1234567890123` | CIV 123/2024 | Ram Kumar vs Shyam Singh |
| `WXYZ9876543210987` | CRLP 456/2023 | State vs Mohan Lal |
| `PQRS5555666677778` | CIV 789/2024 | Lakshmi Devi vs Municipal Corp |

### Court 102 - High Court Andhra Pradesh

| CNR | Case No | Parties |
|-----|---------|---------|
| `HCAP1111222233334` | WP 1001/2024 | Vijay Enterprises vs State of AP |

---

## 🔧 Running with Mock API Server

For more realistic testing, use the mock API server:

### Terminal 1 - Start Mock Server:
```bash
venv\Scripts\activate
python mock_api_server.py
```

### Terminal 2 - Start Web App:
```bash
venv\Scripts\activate
set ECOURTS_API_BASE=http://localhost:5001
python web_app.py
```

Now the web app will fetch data from the mock server!

---

## 📱 Mobile Responsive

The web interface is fully responsive and works great on:
- 💻 Desktop computers
- 📱 Smartphones
- 📲 Tablets

Try resizing your browser window to see the responsive design in action!

---

## 🎨 Customization

### Change Colors:

Edit `templates/base.html` and modify the CSS:

```css
/* Change gradient colors */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change button colors */
.btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Add New Pages:

1. Create a new route in `web_app.py`:
   ```python
   @app.route('/mypage')
   def mypage():
       return render_template('mypage.html')
   ```

2. Create `templates/mypage.html`:
   ```html
   {% extends "base.html" %}
   {% block content %}
   <div class="card">
       <h2>My New Page</h2>
   </div>
   {% endblock %}
   ```

---

## 🐛 Troubleshooting

### Port Already in Use:

If port 5000 is busy, change it in `web_app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Templates Not Found:

Make sure you're running from the `d:\ecourt` directory:
```bash
cd d:\ecourt
python web_app.py
```

### CSS Not Loading:

The CSS is embedded in `base.html`, so it should always work. If you see unstyled pages, check the browser console for errors.

---

## 📊 Comparison: CLI vs Web

| Feature | CLI | Web Interface |
|---------|-----|---------------|
| **Ease of Use** | Command-line | Point and click |
| **Visual Appeal** | Text only | Beautiful UI |
| **Mobile Access** | No | Yes |
| **Batch Processing** | Yes | No |
| **API Access** | Via curl | Built-in |
| **Best For** | Automation | Human users |

---

## 🚀 Deployment Options

### Local Development:
```bash
python web_app.py
```

### Production (with Gunicorn):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```

### Docker (create Dockerfile):
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "web_app.py"]
```

---

## 📚 Project Files

```
d:/ecourt/
├── web_app.py              # Main web application
├── templates/              # HTML templates
│   ├── base.html          # Base template with CSS
│   ├── index.html         # Search page
│   ├── results.html       # Search results
│   ├── causelist.html     # Cause list form
│   ├── causelist_results.html  # Cause list display
│   └── about.html         # About page
├── src/                   # Backend modules
├── sample_data/           # Sample JSON files
└── outputs/               # Query results
```

---

## ✨ Next Steps

1. ✅ Test the web interface in offline mode
2. ✅ Try the mock server mode
3. ✅ Test on mobile devices
4. ✅ Customize the colors and styling
5. ✅ Integrate with real eCourts API when available

---

**Enjoy your beautiful web interface! 🎉**

For CLI usage, see `TESTING_GUIDE.md`
For quick reference, see `QUICK_START.md`
