@echo off

if %1 == 1 goto get_devices
if %1 == 2 goto get_folder
if %1 == 3 goto save_arquive
if %1 == 4 goto get_database
if %1 == 5 goto set_file_download
if %1 == 6 goto clean_log
if %1 == 7 goto get_share
if %1 == 8 goto save_arquive_shared
if %1 == 9 goto set_file_database
if %1 == 10 goto set_file_shared

:get_devices
adb devices > "text\temp.txt"
goto close

:get_folder
adb -s %2 shell ls /data/data/ > "text\folder.txt"
goto close

:save_arquive
adb -s %2 pull /data/data/%3/databases/%4 %5 >> "text\log.txt"
goto close

:save_arquive_shared
adb -s %2 pull /data/data/%3/shared_prefs/%4 %5 >> "text\log.txt"
goto close

:get_database
adb -s %2 shell ls /data/data/%3/databases/ > "text\database.txt"
goto close

:get_share
adb -s %2 shell ls /data/data/%3/shared_prefs/ > "text\shared.txt"
goto close

:set_file_download
adb -s %2 push %3 /sdcard/Download/ >> "text\log.txt"
goto close

:set_file_database
adb -s %2 push %3 /data/data/%4/databases/ >> "text\log.txt"
goto close

:set_file_shared
adb -s %2 push %3 /data/data/%4/shared_prefs/ >> "text\log.txt"
goto close

:clean_log
echo / > "text\log.txt"
goto close

:close
timeout 2 > NUL
exit 0
