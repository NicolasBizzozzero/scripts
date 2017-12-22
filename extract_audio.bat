:: Name: extract_audio.bat
:: Purpose: Extract audio flux from multiple video files.
:: Author: BIZZOZZERO Nicolas


@ECHO off
@TITLE "Extract audio"


SETLOCAL
SET _VIDEO_FORMATS=(.3g2 .3gp .amv .asf .avi .drc .f4a .f4b .f4p .f4v .flv .gif .gifv .m2v .m4p .m4v .mkv .mov .mp2 .mpe .mpeg .mpg .mpv .mng .mp4 .mxf .nsv .ogg .ogv .qt .rm .rmvb .roq .svi .vob .webm .wmv .yuv)


for %%f in (%*) do (
    for %%e in %_VIDEO_FORMATS% do (
        if %%~xf == %%e (
            ffmpeg -i "%%f" -vn -c:a copy "%%~nf.m4a"
        )
    )
)

ENDLOCAL
