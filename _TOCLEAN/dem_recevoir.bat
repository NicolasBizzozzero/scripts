@echo off
REM cipher /d C:\Users\Nicolas\Documents\passwords
set /p password=<C:\Users\Nicolas\Documents\passwords\passwd_sessionfac.txt
"C:\Program Files\pscp\pscp.exe" -r -pw %password% "3504923@ssh.ufr-info-p6.jussieu.fr:../../Etu1/3501501/nicobox" C:\Users\Nicolas\Documents\zone_de_reception
REM "C:\Program Files\psftp\psftp.exe" -pw %password% "3504923@ssh.ufr-info-p6.jussieu.fr"
REM cipher /e C:\Users\Nicolas\Documents\passwords