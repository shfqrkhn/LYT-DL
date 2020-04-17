# LYT-DL
###A Lynda Course Downloader
---------------------------


##Workflow
1. Gather all prerequisites
2. Login to Lynda with FF or Chrome and get 'cookies.txt' extension
3. Get cookies.txt path
4. Get save folder path
5. Get course URL and extract folder name
6. Check if files exist: youtube-dl.exe, ffmpeg.exe, cookies.txt
7. Delete file contents in archive.txt, temp.bat
8. Generate exe using PyInstaller


##Prerequisites
###Google Chrome + 'cookies.txt' Extension:    
https://www.google.com/chrome/
https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg

###Firefox + 'cookies.txt' Extension:    
https://www.mozilla.org/en-CA/firefox/new/
https://addons.mozilla.org/en-CA/firefox/addon/cookies-txt/

###Python3:    
https://www.python.org/downloads/windows/

###YouTube-DL + FFmpeg + VCRedist:    
https://ytdl-org.github.io/youtube-dl/download.html
https://ffmpeg.zeranoe.com/builds/
https://aka.ms/vs/16/release/vc_redist.x86.exe
https://aka.ms/vs/16/release/vc_redist.x64.exe


##Code Snippets
###Empty a text file:
open('archive.txt', 'w').close()


###Delete file if exists:
import os
os.remove("archive.txt")


###Check if a file exists:
import os.path
os.path.exists(file_path)


###Extract folder name from URL
path = "https://www.lynda.com/Python-tutorials/Learning-Python/661773-2.html"
sg.Print(os.path.split(os.path.dirname(path))[1])


###Create a PowerShell script
import subprocess, sys
myScript = open(r'myScript.ps1', 'w+')
myScript.write('ping yahoo.com \n pause')
myScript.close()


###Run cmd command
import os
os.system('cmd /k Powershell.exe -File temp.ps1')


###Check if link ends with html
text = "Python is easy to learn."
result = text.endswith('to learn.')
print(result) # returns True


###Using PyInstaller
In cmd: PyInstaller --onefile --uac-admin -w LYTDL.py


##Command Templates
PowerShell:
.\Youtube-dl --download-archive archive.txt --cookies cookies.txt -o "C:\Lynda\%(playlist_index)s - %(title)s.%(ext)s" https:www.YourCourseURL.com --playlist-start 1 --all-subs

