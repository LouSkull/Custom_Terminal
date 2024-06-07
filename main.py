import os
import getpass
import sys
import time
import socket
import ctypes
import subprocess
import platform
import random

folder_path_user_tree = rf"C:\terminal-tree"
version = "V6.5.2"
command_not_supporting = "This command is not supporting yet..."
directory = os.getcwd()
username = getpass.getuser()
computer_name = socket.gethostname()
os_name = platform.system() if platform.system() else os.name

os.system(f"title {directory}")

from colorama import init, Fore
import os
import subprocess
import time

init()

if not os.path.exists(folder_path_user_tree):
    def clone_repo(github_url, destination_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        os.chdir(destination_folder)
        
        result = subprocess.run(['git', 'clone', github_url], capture_output=True, text=True)
        
        if result.returncode == 0:
            pass
        else:
            print(f"Error installing repository: {result.stderr}")

    if __name__ == "__main__":
        github_url = "https://github.com/statusvisualeffect/terminal-tree"
        destination_folder = "C:\\"

        clone_repo(github_url, destination_folder)

        os.system("pip install colorama")

        os.system("cls")
        print(f"{Fore.BLUE}Operation completed successfully!")

        time.sleep(2)

        print(f"{Fore.LIGHTRED_EX}Please restart the terminal to continue.")

        input()
        sys.exit(1)

with open(rf'C:\terminal-tree\config.txt', 'r') as file:
    for line in file:
        if 'terminal_size:' in line:
            _, value = line.split(':')
            columns, rows = value.strip().split(',')
            command = f"mode con: cols={columns} lines={rows}"
            subprocess.run(command, shell=True)
            break


STD_OUTPUT_HANDLE = -11
console_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

buffer_size = COORD(200, 3000)
ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_handle, buffer_size)

import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

hwnd = ctypes.windll.kernel32.GetConsoleWindow()

with open('C:\\terminal-tree\\config.txt', 'r') as file:
    for line in file:
        if 'visible:' in line:
            _, value = line.split(':')
            visibility = int(value.strip())

opacity = int(255 * visibility / 100)

style = user32.GetWindowLongW(hwnd, -20)
user32.SetWindowLongW(hwnd, -20, style | 0x00080000)

user32.SetLayeredWindowAttributes(hwnd, 0, opacity, 0x02)

user32.ShowWindow(hwnd, 5)
user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 5)

from colorama import Fore

if not os.path.exists(folder_path_user_tree):
    print(f"{Fore.RED}DON'T FORGET TO TYPE COMMAND: terminal --get-update")
    print(f"{Fore.RED}DON'T FORGET TO TYPE COMMAND: terminal --get-update")
    print(f"{Fore.RED}DON'T FORGET TO TYPE COMMAND: terminal --get-update")
    print()

print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}For cmd help, Type{Fore.WHITE} {Fore.LIGHTCYAN_EX}help{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}For help, Type{Fore.WHITE} {Fore.LIGHTCYAN_EX}terminal --help{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}Version: {Fore.WHITE}{Fore.LIGHTCYAN_EX}[{version}]{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print()
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}By: {Fore.WHITE}{Fore.LIGHTCYAN_EX}@ggrolton123{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print()

while True:
    print(f"{Fore.LIGHTGREEN_EX}┌──{Fore.LIGHTBLUE_EX}({computer_name}**{username})-[~/{directory}]")
    cmd = input(f"{Fore.LIGHTGREEN_EX}└─$ {Fore.LIGHTYELLOW_EX}")
    
    sys.stdout.write("\033[97m\033[97m")
    sys.stdout.flush() 
    
    if cmd.lower() == "clear" or cmd.lower() == "clean":
        os.system("cls")
        
    elif cmd.lower() == "exit":
        sys.exit(1)
        
    elif cmd.lower() == "terminal --help":
        import os
        from colorama import Fore

        config_path = rf"C:\terminal-tree\config.txt"
        help_file_path = rf"C:\terminal-tree\help_command.txt"

        def read_config():
            try:
                with open(config_path, 'r') as file:
                    config = file.read()
                    if "show_help_txt_or_print" in config:
                        value = config.split('show_help_txt_or_print:')[1].strip()
                        return value
                    else:
                        return ""
            except FileNotFoundError:
                return ""

        def write_config(value):
            with open(config_path, 'a') as file:
                file.write(f"\nshow_help_txt_or_print: {value}\n")

        def main():
            config_value = read_config()
            
            if config_value == "1":
                print_help()
            elif config_value == "0":
                open_help_file()
            else:
                print("1, Open txt file \n2, Print")
                help_command_input = input("Your choice: ")
                
                if help_command_input == "1":
                    open_help_file()
                    write_config("0")
                elif help_command_input == "2":
                    print_help()
                    write_config("1")
                else:
                    pass

        def open_help_file():
            os.system(f"start {help_file_path}")

        def print_help():
            print(f"""{Fore.LIGHTCYAN_EX}
{Fore.LIGHTMAGENTA_EX}- {Fore.LIGHTBLACK_EX}Commands:{Fore.RESET} {Fore.GREEN}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Help command{Fore.RESET} {Fore.LIGHTBLUE_EX}(terminal --help){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Clear terminal{Fore.RESET} {Fore.LIGHTBLUE_EX}(clear,clean){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Shows up all files{Fore.RESET} {Fore.LIGHTBLUE_EX}(ls){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Shows your ip{Fore.RESET} {Fore.LIGHTBLUE_EX}(ip --look){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Ping website{Fore.RESET} {Fore.LIGHTBLUE_EX}(webcall (link)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Install python lib{Fore.RESET} {Fore.LIGHTBLUE_EX}(pyinstall (lib-name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Uninstall python lib{Fore.RESET} {Fore.LIGHTBLUE_EX}(pyuninstall (lib-name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Shows the the terminal version{Fore.RESET} {Fore.LIGHTBLUE_EX}(terminal --ver){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Change title{Fore.RESET} {Fore.LIGHTBLUE_EX}(set-title-console-(your_title)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Open folder that you in{Fore.RESET} {Fore.LIGHTBLUE_EX}(open -/ folder){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Full screen{Fore.RESET} {Fore.LIGHTBLUE_EX}(full-screen-console){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Turn off full screen{Fore.RESET} {Fore.LIGHTBLUE_EX}(un-full-screen-console){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Read file{Fore.RESET} {Fore.LIGHTBLUE_EX}(read -/ (patch-to-file)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Create file{Fore.RESET} {Fore.LIGHTBLUE_EX}(touch -/ (file-name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Delete file{Fore.RESET} {Fore.LIGHTBLUE_EX}(del -/ (file-name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Write in file{Fore.RESET} {Fore.LIGHTBLUE_EX}(write /.(file-name) -/ (text)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Install recommended lib python{Fore.RESET} {Fore.LIGHTBLUE_EX}(pyinstall.rec -/ recommended{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Set wallpaper{Fore.RESET} {Fore.LIGHTBLUE_EX}(user32-change-wallpaper-(image-patch)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Start app{Fore.RESET} {Fore.LIGHTBLUE_EX}(run -/ (file_name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Start python script{Fore.RESET} {Fore.LIGHTBLUE_EX}(pyrun -/ (file_name)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Shows where are you{Fore.RESET} {Fore.LIGHTBLUE_EX}(terminal --patch){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Restart OS{Fore.RESET} {Fore.LIGHTBLUE_EX}(user32-restart){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Shutdown OS{Fore.RESET} {Fore.LIGHTBLUE_EX}(user32-shutdown){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}neofetch{Fore.RESET} {Fore.LIGHTBLUE_EX}(neofetch){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Open tree folder{Fore.RESET} {Fore.LIGHTBLUE_EX}(open -/ tf){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Show up your text{Fore.RESET} {Fore.LIGHTBLUE_EX}(terminal --console.out:(your-text)){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}About{Fore.RESET} {Fore.LIGHTBLUE_EX}(terminal --about){Fore.RESET}
                    {Fore.RESET}""")

        if __name__ == "__main__":
            main()

    elif cmd.lower() == "neofetch":
        print("MADE BY: M4cs")
        os.system("C:\\terminal-tree\\winfetch.exe")

    elif cmd.lower() == "ls":
        os.system("dir /b")
        
    elif cmd.lower() == "terminal --patch":
        print(directory)
        
    elif cmd.lower() == "terminal --ver":
        print(version)
        
    elif cmd.lower().startswith("terminal --console.out:"):
        text_to_print = cmd[23:]
        print(text_to_print)
        
    elif cmd.lower() == ("terminal --version"):
        print("Did you meant: terminal --ver")
        
    elif cmd.lower() == "terminal --about":
        print(f"""
{Fore.LIGHTMAGENTA_EX}- {Fore.LIGHTBLACK_EX}About:{Fore.RESET} {Fore.LIGHTGREEN_EX}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}VERSION{Fore.RESET} {Fore.LIGHTGREEN_EX}(1.0.0){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Programming language{Fore.RESET} {Fore.LIGHTGREEN_EX}(python){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}GITHUB{Fore.RESET} {Fore.LIGHTGREEN_EX}(https://github.com/LouSkull){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Developer discord{Fore.RESET} {Fore.LIGHTGREEN_EX}(@ggrolton123){Fore.RESET}
""")
        
    elif cmd.lower().startswith("cd "):
        new_directory = cmd[3:]
        
        try:
            os.chdir(new_directory)
            directory = os.getcwd()
        except FileNotFoundError:
            print(f"Error: Directory not found - {new_directory}")
    
    elif cmd.lower() == "@echo off":
        print(command_not_supporting)
        time.sleep(1)
        
    elif cmd.lower() == "ip --look":
        os.system("ipconfig | find \"IPv4\"")
        os.system("ipconfig | find \"IPv6\"")
        
    elif cmd.lower().startswith("webcall "):
        web_call_link = cmd[8:]
        os.system(f"ping {web_call_link}")
        
    elif cmd.lower().startswith("pyinstall "):
        python_lib_to_install = cmd[10:]
        os.system(f"pip install {python_lib_to_install}")
        
    elif cmd.lower().startswith("pyuninstall "):
        python_lib_to_uninstall = cmd[12:]
        os.system(f"pip uninstall {python_lib_to_uninstall}")
        
    elif cmd.lower().startswith("set-title-console-"):
        new_console_title = cmd[18:]
        os.system(f"title {new_console_title}")
        
    elif cmd.lower() == "open -/ folder":
        os.startfile(directory)
        
    elif cmd.lower() == "full-screen-console":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
        
    elif cmd.lower() == "un-full-screen-console":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        os.system(f"mode 200,55")

    elif cmd.lower().startswith("read -/ "):
        file_path = cmd[8:]
            
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            print("\033[90m" + content)
            
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

    elif cmd.lower().startswith("touch -/ "):
        name_file_to_create = cmd[9:]
        open(name_file_to_create, 'w').close()
        
    elif cmd.lower().startswith("del -/ "):
        name_file_to_delete = cmd[7:]
        os.remove(name_file_to_delete)
        
    elif cmd.lower().startswith("write /."):
        parts = cmd[8:].split(" -/ ")
        if len(parts) == 2:
            name_file_to_write_in = parts[0].strip()
            text_to_file = parts[1].strip()

            with open(name_file_to_write_in, 'w') as file:
                file.write(text_to_file)
    
    elif cmd.lower() == "pyinstall.rec -/ recommended":
        print("This can take up to 10M...")
        time.sleep(1.5)
        os.system("pip install requests customtkinter tk")
        
    elif cmd.lower().startswith("run -/ "):
        app_to_run = cmd[7:]
        os.system(f"start {app_to_run}")
        
    elif cmd.lower().startswith("pyrun -/ "):
        app_to_run = cmd[9:]
        os.system(f"python {app_to_run}")
        
    elif cmd.lower() == "?":
        print("Error: unknown command did you meant: terminal --help \n")
    
    elif cmd.lower().startswith("title "):
        print("Error: Did you meant \"set-title-console-(your_title)\"")
        
    elif cmd.lower().startswith("user32-change-wallpaper-"):
        wallpaper_patch = cmd[24:]
        
        import ctypes
        import os

        def set_wallpaper(image_path):
            if not os.path.isfile(image_path):
                raise FileNotFoundError(f"The file {image_path} does not exist.")

            image_path = os.path.abspath(image_path)

            SPI_SETDESKWALLPAPER = 20
            result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

            if not result:
                raise ctypes.WinError()

        if __name__ == "__main__":
            image_path = wallpaper_patch
            set_wallpaper(image_path)

    elif cmd.lower() == "user32-restart":
        os.system("shutdown /r /f /t 0")

    elif cmd.lower() == "user32-shutdown":
        os.system("shutdown /s /f /t 0")
    
    elif cmd.lower() == "terminal --get-update":
        import webbrowser
        from colorama import init

        init()

        webbrowser.open("https://github.com/git-for-windows/git/releases/download/v2.45.2.windows.1/PortableGit-2.45.2-64-bit.7z.exe")

        def clone_repo(github_url, destination_folder):
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            os.chdir(destination_folder)
            
            result = subprocess.run(['git', 'clone', github_url], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Repository cloned successfully to {destination_folder}")
            else:
                print(f"Error cloning repository: {result.stderr}")

        if __name__ == "__main__":
            github_url = "https://github.com/statusvisualeffect/terminal-tree"
            destination_folder = "C:\\"

            clone_repo(github_url, destination_folder)

            os.system("pip install colorama")

            print(f"{Fore.GREEN}Successfully!")
            print(f"{Fore.GREEN}Successfully!")
            print(f"{Fore.GREEN}Successfully!")
            time.sleep(2)
            print(f"{Fore.GREEN}Restart terminal please...!")
            print(f"{Fore.GREEN}Restart terminal please...!")
            print(f"{Fore.GREEN}Restart terminal please...!")
        
    elif cmd.lower().startswith("terminal "):
        print("Error: type \"terminal --help\" for help")

    elif cmd.lower() == "open -/ tf":
        os.startfile(rf"C:\terminal-tree")

    else:
        try:
            os.system(cmd)
        except Exception as e:
            print("Error: ", e)
