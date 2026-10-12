@echo off
cd /d "%~dp0"
py -3 tools\pigeon_gui.py
if errorlevel 1 pause
