#!/usr/bin/env Python3
import os

import PySimpleGUI as sg

sg.ChangeLookAndFeel('Topanga')

layout = [
    [sg.InputText('Locate \'cookies.txt\' (cannot contain space)'), sg.FileBrowse()],
    [sg.InputText('Save path (cannot contain space)'), sg.FolderBrowse()],
    [sg.InputText('Enter course URL ending in \'.html\'')],
    [sg.Button('Pre-Launch Safety Check'), sg.Button('Launch LYT-DL'), sg.Button('Abort Launch')]
]

window = sg.Window('LYT-DL', layout, no_titlebar=False, grab_anywhere=False, border_depth=5)

while True:
    event, values = window.read()

    cookie_path = "\"" + str(values[0]) + "\""
    cookie_path = cookie_path.replace("/", "\\")
    folder_location = str(values[1])
    course_url = str(values[2])
    folder_name = str(os.path.split(os.path.dirname(course_url))[1])
    folder_path = folder_location + "\\" + folder_name + "\\"
    folder_path = folder_path.replace("/", "\\")
    part_cookie = '.\youtube-dl.exe --download-archive archive.txt --cookies ' + cookie_path + ' -o '
    part_folder = '\"' + folder_path + '%(playlist_index)s - %(title)s.%(ext)s\" '
    part_URL = course_url + ' --playlist-start 1 --all-subs --no-check-certificate'


    def qc():
        qc_pass = True
        if os.path.exists('archive.txt'):
            open('archive.txt', 'w').close()
        if os.path.exists('temp.ps1'):
            open('temp.ps1', 'w').close()
        if ' ' in cookie_path:
            qc_pass = False
            sg.Print("Error: 'Space' found in cookie path")
        if ' ' in folder_path:
            qc_pass = False
            sg.Print("Error: 'Space' found in folder path")
        if not os.path.exists('youtube-dl.exe'):
            qc_pass = False
            sg.Print("Error: 'youtube-dl.exe' not found")
        if not os.path.exists('ffmpeg.exe'):
            qc_pass = False
            sg.Print("Error: 'ffmpeg.exe' not found")
        if not (course_url.endswith('.html')):
            qc_pass = False
            sg.Print("Error: URL doesn't end with '.html'")
        return qc_pass


    if event in (None, 'Abort Launch'):
        break
    if event in (None, 'Pre-Launch Safety Check'):
        if not qc():
            sg.Print("Pre-launch safety check failed!")
        elif qc():
            sg.Print("Pre-launch safety check passed!")
    if event in (None, 'Launch LYT-DL'):
        if not qc():
            sg.Print("Pre-launch safety check failed!")
        elif qc():
            myScript = open(r'temp.ps1', 'w+')
            myScript.write(part_cookie + part_folder + part_URL)
            myScript.close()
            os.system('cmd /k Powershell.exe -File temp.ps1')

window.close()
