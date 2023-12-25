import os
import getpass
import sys
import time
import socket

directory = os.getcwd()
username = getpass.getuser()
    
os.system(f"title")
print("HELP COMMAND \"?\"")
print()
while True:
    cmd = input(f"{username}~~{directory}:~$ \033[93m\033[93m")
    print("\033[97m\033[97m")
    
    if cmd == "clear":
        os.system("cls")
        
    elif cmd == "exit":
        sys.exit(1)
        
    elif cmd == "?":
        print("You can read it in \"about.csv\" file : )")
        
    elif cmd == "clean":
        os.system("cls")
        
    elif cmd == "ls":
        os.system("dir")
        
    elif cmd.startswith("cd "):
        new_directory = cmd[3:]
        
        try:
            os.chdir(new_directory)
            directory = os.getcwd()
        except FileNotFoundError:
            print(f"Error: Directory not found - {new_directory}")
    
    elif cmd == "@echo off":
        print("This command is not supporting yet...")
        time.sleep(1)
        
    elif cmd == "@ECHO OFF":
        print("This command is not supporting yet...")
        time.sleep(1)
        
    elif cmd == "@Echo off":
        print("This command is not supporting yet...")
        time.sleep(1)
        
    elif cmd == "ip":
        os.system("ipconfig")
        
        
    else:
        os.system(f"{cmd}")
