@echo off

if %1 == 1 goto list_emulator
if %1 == 2 goto init_emulator

:list_emulator
C:\Users\user\AppData\Local\Android\Sdk\emulator\emulator -list-avds > "text\emulator.txt"
goto close

:init_emulator
C:\Users\user\AppData\Local\Android\Sdk\emulator\emulator -avd %2
taskkill /f /im python.exe
goto close

:close
timeout 2 > NUL
exit 0
