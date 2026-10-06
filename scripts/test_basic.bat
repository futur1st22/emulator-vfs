@echo off
rem Basic start script with all command line options
cd /d "%~dp0.."
py src\emulator.py --vfs vfs\minimal.zip --script scripts\basic.txt
