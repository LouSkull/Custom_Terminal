import os
import shutil
from colorama import Fore

def copy_and_rename_exe(source_path, destination_directory):
    if not os.path.isfile(source_path):
        print(f"Error: {source_path} does not exist.")
        return

    print(f"{Fore.RED}WARNING: DON'T USE NAME LIKE \"cmd.exe, explorer.exe, taskmgr.exe\"")
    print(f"{Fore.RED}WARNING: DON'T USE NAME LIKE \"cmd.exe, explorer.exe, taskmgr.exe\"")
    print(f"{Fore.RED}WARNING: DON'T USE NAME LIKE \"cmd.exe, explorer.exe, taskmgr.exe\"")
    print(f"{Fore.RED}WARNING: DON'T USE NAME LIKE \"cmd.exe, explorer.exe, taskmgr.exe\"\n")
    
    new_name = input(f"{Fore.YELLOW}Enter the new name for better cmd (without extension): ") + ".exe"

    destination_path = os.path.join(destination_directory, new_name)

    try:
        shutil.copy2(source_path, destination_path)
        print(f"Successfully installed, to open better cmd press win+r and type {new_name}")
        os.system("start readme.txt")
        input()
    except Exception as e:
        print(f"Error: {e}")

source_file = "build.exe"

destination_dir = "C:\Windows\System32"

copy_and_rename_exe(source_file, destination_dir)
