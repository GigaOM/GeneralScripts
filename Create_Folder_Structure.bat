::===============================================================
:: Note:This script is still being built 
:: The below example will setup a folder structure.
:: The Paths can be edited to your liking. 
::
::===============================================================   

(
    echo What do you want the folder to be called?
    set /P folderName=
    md "%USERPROFILE%\desktop\%folderName%"
)

@echo off
set /p project="Current Gigaom Projects:"

MkDir "%USERPROFILE%\desktop\%folderName%\Results\"
MkDir "%USERPROFILE%\desktop\%folderName%\Graphics\"
MkDir "%USERPROFILE%\desktop\%folderName%\RawData\"
MkDir "%USERPROFILE%\desktop\%folderName%\Scripts\"
MkDir "%USERPROFILE%\desktop\%folderName%\Applications\"
MkDir "%USERPROFILE%\desktop\%folderName%\Results\"
MkDir "%USERPROFILE%\desktop\%folderName%\HelpFiles\"
MkDir "%USERPROFILE%\desktop\%folderName%\SnapShots\"
MkDir "%USERPROFILE%\desktop\%folderName%\ZoomRecordings\"


 
