@echo off
REM Get the current year/month/day
for /F "skip=1 delims=" %%F in ('
    wmic PATH Win32_LocalTime GET Day^,Month^,Year /FORMAT:TABLE
') do (
    for /F "tokens=1-3" %%L in ("%%F") do (
        set CurrDay=0%%L
        set CurrMonth=0%%M
        set CurrYear=%%N
    )
)
set CurrDay=%CurrDay:~-2%
set CurrMonth=%CurrMonth:~-2%
REM Test if it's not our coupleday
REM if "%CurrMonth%" NEQ "11" goto :eof
REM if "%CurrDay%" NEQ "11" goto :eof
REM If yes, then end script
REM If no, then find how many years we are together
set /a numberOfYearsWithSarah=%CurrYear%-2015
REM Then build the message which will be printed
set "message=Joyeux %numberOfYearsWithSarah% an(s) ma petite Sarah !"
REM Finally, print this message 
cscript output_text_into_popup_window.vbs "%message%"