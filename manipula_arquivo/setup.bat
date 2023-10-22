@echo off

mode con: lines=6 cols=40
color 06
title MANIPULA ARQUIVO

python .\arquive.py

timeout 2 > NUL
exit 0
