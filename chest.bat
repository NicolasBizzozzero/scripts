:: Name: chest.bat
:: Purpose: Hide a folder with a password or create-it if it doesn't exists
:: Author: BIZZOZZERO Nicolas
::
:: This script can hide precious documents from the eyes of your family,
:: relatives or any non-tech person using your computer.
:: It'll setup a directory in which you can store anything you want, then you
:: can hide or reveal the directory by simply invocating the script again.
:: This script mustn't be used for real security purposes, as it's easily
:: bypassable by any humain who can read code.

@ECHO off
@TITLE Locked chest


SETLOCAL
SET _HIDING_LOCATION="Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
SET _CHEST_NAME="chest"
SET _CHEST_PASSWORD=Veronica


IF EXIST %_HIDING_LOCATION% GOTO ask_open
IF NOT EXIST %_CHEST_NAME% GOTO create_chest

:ask_close
ECHO Do you want to close the chest, 'Yes' [Y/y] or 'No' [N/n] ?
SET /p "choice=>"
IF %choice%==Y GOTO close
IF %choice%==y GOTO close
IF %choice%==N GOTO end
IF %choice%==n GOTO end
ECHO Incorrect choice, please answer with 'Yes' [Y/y] or 'No' [N/n].
GOTO ask_close

:close
REN %_CHEST_NAME% %_HIDING_LOCATION%
ATTRIB +h +s %_HIDING_LOCATION%
ECHO Chest locked.
GOTO end

:ask_open
ECHO Please enter the chest password :
SET /p "password=>"
IF NOT %password%==%_CHEST_PASSWORD% GOTO incorrect_password
ATTRIB -h -s %_HIDING_LOCATION%
REN %_HIDING_LOCATION% %_CHEST_NAME%
ECHO Chest unlocked.
GOTO end

:incorrect_password
ECHO Incorrect password.
GOTO end

:create_chest
MD %_CHEST_NAME%
ECHO The chest directory has been created.
GOTO end

:end
ENDLOCAL
PAUSE
