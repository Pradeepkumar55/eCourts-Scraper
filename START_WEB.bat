@echo off
echo ============================================================
echo eCourts Listing Checker - Web Interface
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install dependencies
echo Checking dependencies...
pip install -q -r requirements.txt
echo Dependencies OK!
echo.

echo ============================================================
echo Starting Web Application
echo ============================================================
echo.
echo Mode: OFFLINE (using sample data)
echo URL: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

REM Set offline mode and start web app
set OFFLINE_MODE=true
python web_app.py

pause
