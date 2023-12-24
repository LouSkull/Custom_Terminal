import os,getpass,sys,time,socket

current_directory = os.getcwd()

def get_pc_name():
    try:
        pc_name = socket.gethostname()
        return pc_name
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    pc_name = get_pc_name()


def get_username():
    username = getpass.getuser()
    return username

if __name__ == "__main__":
    user = get_username()

    print("HELP COMMAND \"?\"")
    os.system(f"title {current_directory}")
    os.system(f"color 8")
    while True:
        cmd = input(f"{user}~{pc_name}~{current_directory}:~$ \033[91m\033[91m")
        print("\033[90m\033[90m")

        if cmd == "clear":
            os.system("cls")
            
        elif cmd == "exit":
            sys.exit(1)
            
        elif cmd == "?":
            print(
                """\033[90m
Commands:
Batch help command "help"
Terminal help command "?"
Clear terminal command "cls" "clear" "clean"

About:
VERSION (5.8.3-PolarisBeta)
Programming language "python, batch"
GITHUB "https://github.com/LouSkull"
Developer discord "@statusvisualeffect"
 \n
                \033[90m"""
            )
            time.sleep(1)
            
        elif cmd == "clean":
            os.system("cls")
            
        elif cmd == "ls":
            os.system("dir")
        
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
            
        elif cmd == "myip":
            os.system("ipconfig")
            
        else:
            if cmd.startswith("cd"):
                new_directory = cmd[3:]
                try:
                    os.chdir(new_directory)
                except FileNotFoundError:
                    print(f"Directory not found: {new_directory}")
                    
                    
            else:
                command = os.system(f"{cmd}")
                
