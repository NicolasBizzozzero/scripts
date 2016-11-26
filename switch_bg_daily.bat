@echo off

REM Get day of the week
echo.|command /C date|find /i "current" >%temp%\dow.txt
for /f "tokens=1-4 delims=/ " %%i in (%temp%\dow.txt) do set DOW=%%l


REM Change wallpaper based off the day of the week
REM Monday
if "%DOW%" == "Mon" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\blue.jpg"
    goto setwp
)
REM Tuesday
if "%DOW%" == "Tue" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\red.png"
    goto setwp
)
REM Wednesday
if "%DOW%" == "Wed" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\green.png"
    goto setwp
)
REM Thursday
if "%DOW%" == "Thu" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\blue2.jpg"
    goto setwp
)
REM Friday
if "%DOW%" == "Fri" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\blue3.jpg"
    goto setwp
)
REM Saturday
if "%DOW%" == "Sat" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\orange.jpg"
    goto setwp
)
REM Sunday
if "%DOW%" == "Sun" (
    set WPP="C:\Users\Nicolas\Google Drive\Wallpapers\Album Qlufr - Imgur\colored2.jpg"
    goto setwp
)


REM Set the wallpaper
:setwp
set PATHTOAPP="C:\Program Files\wallpaperchanger\WallpaperChanger.exe"
%PATHTOAPP% %WPP%