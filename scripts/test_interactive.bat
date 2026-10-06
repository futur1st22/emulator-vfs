@echo off
rem Start script without exit, then interactive mode
cd /d "%~dp0.."
py src\emulator.py --vfs C:\data\my_disk.zip --script scripts\init.txt
