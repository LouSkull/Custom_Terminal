import os, getpass, sys

def get_username():
    username = getpass.getuser()
    return username

if __name__ == "__main__":
    user = get_username()

    os.system("color 8")
    print(
        """
BEENDER TERMINAL
VERSION (0.13.21.1)
HELP COMMAND "?"
TELEGRAM CHANNEL "t.me/beendernewdox"
        """
    )
    os.system("title TERMINAL")
    while True:
        current_directory = os.getcwd()
        cmd = input(f"{current_directory} @ ~ @ {user}:~$ \033[96m\033[96m")
        os.system("color 8")

        if cmd == "clear":
            os.system("cls")
            
        elif cmd == "exit":
            sys.exit()
            
        elif cmd == "?":
            print(
                """
Commands:
Batch help command "help"
Terminal help command "?"
Clear terminal command "cls" "clear" "clean"

About:
Programming language "python, batch"
Developer discord "@statusvisualeffect"
                """
            )
            
        elif cmd == "clean":
            os.system("cls")
            
        else:
            if cmd.startswith("cd "):
                new_directory = cmd[3:]
                try:
                    os.chdir(new_directory)
                except FileNotFoundError:
                    print(f"Directory not found: {new_directory}")
            else:
                command = os.system(f"{cmd}")
                
