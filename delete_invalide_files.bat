:: Name: delete_invalide_files.bat
:: Purpose: Delete all invalide files and directory on a disk
:: Author: BIZZOZZERO Nicolas


set disk=%1
chkdsk %disk% /b
