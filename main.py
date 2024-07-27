# -*- coding: utf-8 -*-

import os
import getpass
import sys
import time
import socket
import ctypes
import subprocess
import platform
import webbrowser

username = getpass.getuser()
folder_path_user_tree = rf"C:\Users\{username}\AppData\Roaming\Terminal"
version = "V6.6.5"
command_not_supporting = "This command is not supporting yet..."
directory = os.getcwd()
computer_name = socket.gethostname()
os_name = platform.system() if platform.system() else os.name

os.system(f"title {directory}")

from colorama import init, Fore
init(autoreset=True)

if not os.path.exists(folder_path_user_tree):
    import shutil

    def copy_folder(source_folder, destination_folder):
        try:
            shutil.copytree(source_folder, destination_folder)
            print(f"Folder '{source_folder}' successfully copied to '{destination_folder}'.")
        except shutil.Error as e:
            print(f"Error: {e}")
        except OSError as e:
            print(f"Error: {e}")

    source_folder = 'Terminal'
    destination_folder = rf'C:\Users\{username}\AppData\Roaming\Terminal'

    copy_folder(source_folder, destination_folder)

with open(rf'C:\Users\{username}\AppData\Roaming\Terminal\config.txt', 'r') as file:
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

user32 = ctypes.WinDLL('user32', use_last_error=True)

hwnd = ctypes.windll.kernel32.GetConsoleWindow()

with open(rf'C:\Users\{username}\AppData\Roaming\Terminal\config.txt', 'r') as file:
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

if not os.path.exists(folder_path_user_tree):
    print(f"{Fore.RED}TYPE COMMAND: terminal --get-update")
    print(f"{Fore.RED}TYPE COMMAND: terminal --get-update")
    print(f"{Fore.RED}TYPE COMMAND: terminal --get-update")
    print()

print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}For cmd help, Type{Fore.WHITE} {Fore.LIGHTCYAN_EX}help{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}For help, Type{Fore.WHITE} {Fore.LIGHTCYAN_EX}terminal --help{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}Version: {Fore.WHITE}{Fore.LIGHTCYAN_EX}[{version}]{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print()
print(f"{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}{Fore.WHITE}By: {Fore.WHITE}{Fore.LIGHTCYAN_EX}@ggrolton123{Fore.LIGHTCYAN_EX}{Fore.LIGHTGREEN_EX}||{Fore.LIGHTGREEN_EX}")
print()

while True:
    print(f"{Fore.LIGHTGREEN_EX}┌──{Fore.LIGHTBLUE_EX}({computer_name}@@@{username})-[~/{directory}]")
    cmd = input(f"{Fore.LIGHTGREEN_EX}└─$ {Fore.LIGHTYELLOW_EX}")
    
    sys.stdout.write("\033[97m\033[97m")
    sys.stdout.flush() 
    
    if cmd.lower() == "clear" or cmd.lower() == "clean" or cmd.lower() == "clera":
        os.system("cls")
        
    elif cmd.lower() == "exit":
        sys.exit(1)
        
    elif cmd.lower() == "terminal --help":
        os.system(rf"start C:\\Users\\{username}\\AppData\\Roaming\\Terminal\\commands.html")

    elif cmd.lower() == "ls":
        import os
        from colorama import Fore, Style, init

        init(autoreset=True)

        def list_directory_contents():
            current_directory = os.getcwd()
            folders = []
            file_categories = {
                "txt": [],
                "reg": [],
                "cs": [],
                "py": [],
                "cpp": [],
                "others": []
            }
            
            with os.scandir(current_directory) as entries:
                for entry in entries:
                    if entry.is_dir():
                        folders.append(entry.name)
                    else:
                        _, ext = os.path.splitext(entry.name)
                        ext = ext.lower()[1:]
                        if ext in file_categories:
                            file_categories[ext].append(entry.name)
                        else:
                            file_categories["others"].append(entry.name)
            
            print(Fore.RED + "~~ Folders ~~" + Style.RESET_ALL)
            for folder in folders:
                print(Fore.RED + folder + Style.RESET_ALL)
            
            print()
            
            category_colors = {
                "txt": Fore.CYAN,
                "reg": Fore.YELLOW,
                "cs": Fore.MAGENTA,
                "py": Fore.GREEN,
                "cpp": Fore.BLUE,
                "others": Fore.WHITE
            }

            categories = ["txt", "reg", "cs", "py", "cpp", "others"]

            for category in categories:
                if file_categories[category]:
                    print(category_colors[category] + f"~~ {category.upper()} Files ~~" + Style.RESET_ALL)
                    for file in file_categories[category]:
                        print(category_colors[category] + file + Style.RESET_ALL)
                    print()

        if __name__ == "__main__":
            list_directory_contents()
        
    elif cmd.lower() == "pwd":
        print(directory)
        
    elif cmd.lower() == "terminal --ver":
        print(version)
        
    elif cmd.lower() == "terminal --version":
        print("Did you mean: terminal --ver")
        
    elif cmd.lower() == "terminal --about":
        print(f"""
{Fore.LIGHTMAGENTA_EX}- {Fore.LIGHTBLACK_EX}About:{Fore.RESET} {Fore.LIGHTGREEN_EX}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}VERSION{Fore.RESET} {Fore.LIGHTGREEN_EX}(1.0.0){Fore.RESET}
{Fore.LIGHTMAGENTA_EX}---- {Fore.LIGHTBLACK_EX}Programming language{Fore.RESET} {Fore.LIGHTGREEN_EX}(python,golang){Fore.RESET}
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
    
    elif cmd.lower() == "terminal --settings":
        os.system(fr"C:\\Users\\{username}\\AppData\\Roaming\\Terminal\\settings.py")
    
    elif cmd.lower() == "@echo off":
        print(command_not_supporting)
        time.sleep(1)
        
    elif cmd.lower() == "ip a":
        os.system("ipconfig | find \"IPv4\"")
        os.system("ipconfig | find \"IPv6\"")
        
    elif cmd.lower().startswith("set-title-console-"):
        new_console_title = cmd[18:]
        os.system(f"title {new_console_title}")
        
    elif cmd.lower() == "nautilus .":
        os.startfile(directory)

    elif cmd.lower().startswith("cat "):
        file_path = cmd[4:]
            
        try:
            with open(file_path, 'r') as file:
                content = file.read()

            print("\033[90m" + content)
            
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

    elif cmd.lower().startswith("touch "):
        name_file_to_create = cmd[6:]
        open(name_file_to_create, 'w').close()
        
    elif cmd.lower().startswith("rm -rf "):
        name_file_to_delete = cmd[7:]
        os.remove(name_file_to_delete)
        
    elif cmd.lower() == "?":
        print("Error: unknown command did you mean: terminal --help \n")

    elif cmd.lower().startswith("terminal "):
        print("Error: type \"terminal --help\" for help")

    elif cmd.lower() == "open -/ tf":
        os.startfile(rf"C:\Users\{username}\AppData\Roaming\Terminal")

    else:
        try:
            os.system(cmd)
        except Exception as e:
            print("Error: ", e)
