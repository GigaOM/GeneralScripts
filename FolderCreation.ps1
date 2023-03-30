###Create a partent folder, and point to that folder, then create create the client folder. 
### This script will bring up a graphical interface that can be used to point to a parent folder,
### Then create a sub-folder, and those $subdirs will be created under the sub directory.  
### Give it try


### VARS ###
$subdirs = "Graphics","Results","Scripts","Software"

### FUNCTIONS ###

# Stole this function from https://code.adonline.id.au/folder-file-browser-dialogues-powershell/
function Find-Folders {
    [Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") | Out-Null
    [System.Windows.Forms.Application]::EnableVisualStyles()
    $browse = New-Object System.Windows.Forms.FolderBrowserDialog
    $browse.SelectedPath = "C:\"
    $browse.ShowNewFolderButton = $false
    $browse.Description = "Choose a parent directory"

    $loop = $true
    while($loop)
    {
        if ($browse.ShowDialog() -eq "OK")
        {
        $loop = $false

        #Insert your script here

        } else
        {
            $res = [System.Windows.Forms.MessageBox]::Show("You clicked Cancel. Would you like to try again or exit?", "Select a location", [System.Windows.Forms.MessageBoxButtons]::RetryCancel)
            if($res -eq "Cancel")
            {
                #Ends script
                return
            }
        }
    }
    $browse.SelectedPath
    $browse.Dispose()
}


# Stole this function from https://stackoverflow.com/questions/30534273/simple-inputbox-function
Function Get-NewDirName (){
    [void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')
    $title = 'New Directory'
    $msg   = 'New directory name:'
    [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
}


### MAIN ###
$parentDir = Find-Folders

if ($parentDir) {

    #Get the new directory name
    $NewDirName = Get-NewDirName
    if ($NewDirName) {

        #Creates the parent directory
        New-Item -Path $parentDir\$NewDirName -ItemType Directory

        #A parent directory was found
        ForEach ($dir in $subdirs) {
            New-Item -Path $parentDir\$NewDirName\$dir -ItemType Directory
        }
    } else {
        Write-Error "No directory name was specified"
    }
} else {
    Write-Error "No parent directory was specified"
}