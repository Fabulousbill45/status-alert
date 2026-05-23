@echo off
echo Installing required packages (requests) if not already installed...
pip install requests >nul 2>&1
python check_status.py
pause
