:: Name: coupleday.bat
::
:: Purpose: Check if it's your couple's anniversary and if it is, open a
:: window with a custom message in it.
::
:: Dependencies :
:: * window.vbs
::
:: Author: BIZZOZZERO Nicolas


@ECHO off

SETLOCAL enabledelayedexpansion

SET PATH_SCRIPT_WINDOW=window.vbs

SET PARTNER_NAME=Sarah
SET COUPLEDAY_YEAR=2015
SET COUPLEDAY_MONTH=11
SET COUPLEDAY_DAY=11
SET MESSAGE=Joyeux YEARS an(s) et MONTHS mois ma %PARTNER_NAME%


:: Retrieve the current year/month/day
for /F "skip=1 delims=" %%F in ('
    wmic PATH Win32_LocalTime GET Day^,Month^,Year /FORMAT:TABLE
') do (
    for /F "tokens=1-3" %%L in ("%%F") do (
        set current_day=%%L
        set current_month=%%M
        set current_year=%%N
    )
)


:: Test if it's not your coupleday
if %current_day% NEQ %COUPLEDAY_DAY% goto :end

:: Build the custom message
IF %current_month% GEQ %COUPLEDAY_MONTH% (
    SET /A months_with_partner=%current_month% - %COUPLEDAY_MONTH%
    SET /A years_with_partner=%current_year% - %COUPLEDAY_YEAR%
) ELSE (
    SET /A months_with_partner=12 - %COUPLEDAY_MONTH% + %current_month%
    SET /A years_with_partner=%current_year% - %COUPLEDAY_YEAR% - 1
)
SET MESSAGE=!MESSAGE:YEARS=%years_with_partner%!
SET MESSAGE=!MESSAGE:MONTHS=%months_with_partner%!

:: Finally, print the message in a new window, happy coupleday !
cscript %PATH_SCRIPT_WINDOW% "%message%"


:end
ENDLOCAL
