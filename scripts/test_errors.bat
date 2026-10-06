@echo off
rem Errors: bad commands in script, missing script, unknown option
cd /d "%~dp0.."
py src\emulator.py --vfs vfs\minimal.zip --script scripts\errors.txt
echo.
py src\emulator.py --vfs vfs\minimal.zip --script scripts\missing.txt
echo exit code: %errorlevel%
echo.
py src\emulator.py --vfs vfs\minimal.zip --unknown
echo exit code: %errorlevel%
