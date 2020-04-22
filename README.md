# LYT-DL
### A Lynda.com (LinkedIn Learning) Course Downloader

![LYT-DL_ScreenShot](https://raw.githubusercontent.com/shfqrkhn/LYT-DL/master/LYT-DL_v1.04.png)
![LYT-DL_ScreenShot](https://raw.githubusercontent.com/shfqrkhn/LYT-DL/master/LYT-DL_v1.04.gif)

## Workflow
1. Gather all prerequisites (see below).
2. Log in to Lynda with Firefox or Chrome and get 'cookies.txt' extension.
3. Select cookies.txt path within LYT-DL. The path must not contain space.
4. Select the save folder path within LYT-DL. The path must not contain space. Example: C:\Lynda. A course-specific folder will be created automatically within the selected folder.
5. Copy/Paste (CTRL+C / CTRL+V) course URL within LYT-DL. URL must end in '.html'. Example: https://www.lynda.com/Python-tutorials/Learning-Python/661773-2.html.
6. 'Pre-Launch Safety Check': Check if files exist and other requirements validations (see above requirements).
7. 'Launch LYT-DL': begin download.

## Prerequisites    
### Download LYT-DL Release Archive and Extract:
https://github.com/shfqrkhn/lytdl/releases

### Google Chrome + 'cookies.txt' Extension:    
https://www.google.com/chrome/    
https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg    
#### OR,    
### Firefox + 'cookies.txt' Extension:    
https://www.mozilla.org/en-CA/firefox/new/    
https://addons.mozilla.org/en-CA/firefox/addon/cookies-txt/

### Python3:    
https://www.python.org/downloads/windows/

### YouTube-DL (optional) + FFmpeg (optional) + VCRedist (very important- see Common Issues below):    
https://ytdl-org.github.io/youtube-dl/download.html    
https://ffmpeg.zeranoe.com/builds/    
https://aka.ms/vs/16/release/vc_redist.x86.exe    
https://aka.ms/vs/16/release/vc_redist.x64.exe    


## Common Issues
#### Note: Avoid path-related issues by placing everything as close to the root of the drive (example- C:\Lynda\) as possible.

### PowerShell execution policy: Allow PowerShell to run command scripts
1. Open PowerShell in Administrator mode, input command: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned (source: https://docs.microsoft.com/en-ca/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7)
### MSVCR100.dll missing (i.e. nothing is happening): Visual C Runtime is missing
1. Make sure Windows and VCRedist are up to date
2. Visit for more info: https://www.kapilarya.com/the-program-cant-start-because-mfc100u-dll-is-missing-from-your-computer-windows-10


## Code Snippets
### Empty a text file:
open('archive.txt', 'w').close()

### Delete file if exists:
import os
os.remove("archive.txt")

### Check if a file exists:
import os.path
os.path.exists(file_path)

### Extract folder name from URL
path = "https://www.lynda.com/Python-tutorials/Learning-Python/661773-2.html"
sg.Print(os.path.split(os.path.dirname(path))[1])

### Create a PowerShell script
import subprocess, sys
myScript = open(r'myScript.ps1', 'w+')
myScript.write('ping yahoo.com \n pause')
myScript.close()

### Run cmd command
import os
os.system('cmd /k Powershell.exe -File temp.ps1')

### Check if link ends with html
text = "Python is easy to learn."
result = text.endswith('to learn.')
print(result) # returns True

### Using PyInstaller
In cmd: PyInstaller --onefile --uac-admin -w LYTDL.py

## Command Templates
PowerShell:
.\Youtube-dl --download-archive archive.txt --cookies cookies.txt -o "C:\Lynda\%(playlist_index)s - %(title)s.%(ext)s" https:www.YourCourseURL.com --playlist-start 1 --all-subs
