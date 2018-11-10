' Source : https://www.reddit.com/r/AssHatHackers/comments/1v8vk0/endless_toggle_caps_lock_loop/

Set wshShell =wscript.CreateObject("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "{CAPSLOCK}"
loop
