@echo off
echo ============================================================
echo Starting Web App with Mock API Connection
echo ============================================================
echo.
echo Connecting to Mock API at: http://localhost:5001
echo Web App will run on: http://localhost:5000
echo.
echo Make sure Mock API Server is running first!
echo (Run: python mock_api_server.py in another terminal)
echo.
echo ============================================================
echo.

set ECOURTS_API_BASE=http://localhost:5001
python web_app.py

pause
