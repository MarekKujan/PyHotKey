#Requires AutoHotkey v2.0
#SingleInstance Force

; ctr + alt + E
^!e::Run ".\run_python.bat .\public_scripts\create_tmp_email.py"
