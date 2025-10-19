@echo off
echo ============================================================
echo eCourts Listing Checker - Starting with Mock API Server
echo ============================================================
echo.
echo This will start BOTH servers:
echo   1. Mock API Server on http://localhost:5001
echo   2. Web Application on http://localhost:5000
echo.
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
echo STEP 1: Starting Mock API Server
echo ============================================================
echo.
echo Starting mock server in background...
start "Mock API Server" cmd /k "venv\Scripts\activate && python mock_api_server.py"
echo.
echo Waiting 3 seconds for mock server to start...
timeout /t 3 /nobreak >nul
echo Mock API Server is running on http://localhost:5001
echo.

echo ============================================================
echo STEP 2: Starting Web Application
echo ============================================================
echo.
echo Configuring web app to use mock API...
set ECOURTS_API_BASE=http://localhost:5001
echo.
echo Starting web application...
echo URL: http://localhost:5000
echo.
echo ============================================================
echo READY TO USE!
echo ============================================================
echo.
echo 1. Open your browser: http://localhost:5000
echo.
echo 2. Test with sample data:
echo    - CNR: ABCD1234567890123
echo    - Court ID: 101
echo    - When: Today
echo.
echo 3. Or view full cause list:
echo    - Go to "Cause List" page
echo    - Court ID: 101
echo    - When: Today
echo.
echo Available Courts:
echo   - Court 101: District Court, Kadapa (3 cases)
echo   - Court 102: High Court, Andhra Pradesh (1 case)
echo.
echo Press Ctrl+C to stop the web server
echo (The mock API server will keep running in another window)
echo.
echo If you see "No data found", check TROUBLESHOOTING.md
echo ============================================================
echo.

python web_app.py

pause
