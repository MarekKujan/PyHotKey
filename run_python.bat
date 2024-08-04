@echo off
REM Check if running minimized
if not "%IS_MINIMIZED%"=="1" (
    set IS_MINIMIZED=1
    start "" /min "%~f0" %*
    exit
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run Python script
python "%~1"

exit
