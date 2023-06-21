@echo off
setlocal

set "source_folder=C:\path\to\source\folder"
set "target_folder=C:\path\to\target\folder"
for %%A in ("%source_folder%\*.*") do (
    if not "%%~xA"=="" (
        if not exist "%target_folder%\%%~xA" (
            md "%target_folder%\%%~xA"
        )
        move /Y "%%A" "%target_folder%\%%~xA"
    )
)
