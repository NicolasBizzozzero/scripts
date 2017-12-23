;
; Description:
;     Keep two keys `key1` and `key2` pressed.
;
; Start the program with ctrl+o
; Exit the program with  ctrl+p
;


key1 = s
key2 = d
looooong_time = 1000000000000

; Exit the application
^o::
    ExitApp

; Keep key1 and key2 pressed
^p::
    Send {%key1% down}   ; Press down key1
    Send {%key2% down}   ; Press down key2
    Sleep looooong_time  ; Keep them down for a looooong time

Return
