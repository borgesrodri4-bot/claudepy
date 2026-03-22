@echo off
cd /d "C:\Users\borge\OneDrive\Desktop\codigos py vs\claudepy"
echo Bot iniciando...
:loop
python bot.py
echo Bot parou. Reiniciando em 5 segundos...
timeout /t 5 /nobreak
goto loop
