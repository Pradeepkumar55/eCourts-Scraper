@echo off
echo ============================================================
echo eCourts Listing Checker - Quick Start
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
echo Installing dependencies...
pip install -q -r requirements.txt
echo Dependencies installed!
echo.

echo ============================================================
echo Choose a testing mode:
echo ============================================================
echo 1. OFFLINE MODE (easiest - uses local sample data)
echo 2. MOCK SERVER MODE (realistic - starts local API server)
echo 3. EXIT
echo.
set /p choice="Enter your choice (1, 2, or 3): "

if "%choice%"=="1" goto offline
if "%choice%"=="2" goto mockserver
if "%choice%"=="3" goto end

:offline
echo.
echo ============================================================
echo Running in OFFLINE MODE
echo ============================================================
echo.
echo Testing with sample CNR: ABCD1234567890123
echo.
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
echo.
echo ============================================================
echo Test complete! Check the outputs/ folder for results.
echo ============================================================
echo.
echo Try more commands:
echo   python -m src.cli --cnr WXYZ9876543210987 --when today --court-id 101 --offline
echo   python -m src.cli --causelist --court-id 101 --when today --offline
echo.
pause
goto end

:mockserver
echo.
echo ============================================================
echo Starting MOCK API SERVER
echo ============================================================
echo.
echo The mock server will start on http://localhost:5001
echo.
echo After the server starts, open ANOTHER terminal and run:
echo   venv\Scripts\activate
echo   set ECOURTS_API_BASE=http://localhost:5001
echo   python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101
echo.
echo Press Ctrl+C to stop the server when done.
echo.
pause
python mock_api_server.py
goto end

:end
echo.
echo Goodbye!
pause
