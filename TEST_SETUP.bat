@echo off
echo ============================================================
echo Testing eCourts Setup
echo ============================================================
echo.

REM Test 1: Check if mock server is running
echo Test 1: Checking if Mock API Server is running...
curl -s http://localhost:5001/health >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Mock API Server is running on port 5001
) else (
    echo [FAIL] Mock API Server is NOT running
    echo        Please start it first: python mock_api_server.py
)
echo.

REM Test 2: Check if web app is running
echo Test 2: Checking if Web App is running...
curl -s http://localhost:5000/api/health >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Web App is running on port 5000
) else (
    echo [FAIL] Web App is NOT running
    echo        Please start it with: START_WITH_MOCK_API.bat
)
echo.

REM Test 3: Test mock API data
echo Test 3: Testing Mock API data...
curl -s "http://localhost:5001/cause-list?court_id=101&date=%date:~0,4%-%date:~5,2%-%date:~8,2%" >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Mock API is returning data
) else (
    echo [FAIL] Mock API is not responding correctly
)
echo.

echo ============================================================
echo Test Complete
echo ============================================================
echo.
echo If all tests passed, your setup is correct!
echo If any test failed, follow the instructions above.
echo.
pause
