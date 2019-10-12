:: fast_delete.bat
:: Quickly delete a folder from a Windows file system.
::
:: Source :
:: https://www.ghacks.net/2017/07/18/how-to-delete-large-folders-in-windows-super-fast/

@ECHO OFF
ECHO Delete Folder: %CD%?
PAUSE
SET FOLDER=%CD%
CD /
DEL /F/Q/S "%FOLDER%" > NUL
RMDIR /Q/S "%FOLDER%"
EXIT
