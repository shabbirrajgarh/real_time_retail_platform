@echo off
cd /d C:\Users\ACER\projects\real_time_retail_platform\retail_dbt

:loop
dbt run
timeout /t 30 > nul
goto loop