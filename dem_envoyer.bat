@echo off
REM cipher /d C:\Users\Nicolas\Documents\passwords
set /p password=<C:\Users\Nicolas\Documents\passwords\passwd_sessionfac.txt
"C:\Program Files\pscp\pscp.exe" -r -pw %password% C:\Users\Nicolas\Documents\zone_d_envoi\* "3504923@ssh.ufr-info-p6.jussieu.fr:Documents/zone_de_reception"
REM cipher /e C:\Users\Nicolas\Documents\passwords