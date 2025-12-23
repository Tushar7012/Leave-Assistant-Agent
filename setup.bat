@echo off
echo ================================================
echo Multi-Agent Leave Assistant - Setup Script
echo ================================================
echo.

echo Step 1: Installing Flask CORS...
pip install flask-cors
echo.

echo Step 2: Installing Frontend Dependencies...
cd frontend
call npm install
echo.

echo Step 3: Creating .env.local file...
echo NEXT_PUBLIC_API_URL=http://localhost:5000 > .env.local
echo.

echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Open TWO Command Prompt windows
echo 2. In Window 1, run: start_backend.bat
echo 3. In Window 2, run: start_frontend.bat
echo 4. Open browser to http://localhost:3000
echo.
pause
