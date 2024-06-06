import os, requests, getpass, sys, time, socket

version = "V6.4.6"
command_not_supporting = "This command is not supporting yet..."
directory = os.getcwd()
username = getpass.getuser()
computer_name = socket.gethostname()

os.system(f"title {directory}")
os.system(f"mode 200,55")
print("\033[92m||\033[92m\033[97mFor cmd help, Type\033[97m \033[94mhelp\033[94m\033[92m||\033[92m")
print("\033[92m||\033[92m\033[97mFor help, Type\033[97m \033[94mterminal --help\033[94m\033[92m||\033[92m")
print(f"\033[92m||\033[92m\033[97mVersion: \033[97m \033[94m[{version}]\033[94m\033[92m||\033[92m")
print()
print(f"\033[92m||\033[92m\033[97mBY: \033[97m \033[94m@ggrolton123\033[94m\033[92m||\033[92m")
print()

while True:
    # This part with colors was so hard :/
    cmd = input(f"\033[97m╔══(\033[97m\033[92m{username}\033[92m\033[97m@\033[97m\033[95m{computer_name}\033[95m\033[97m)-[\033[97m\033[97m\033[91m{directory}\033[91m\033[97m]:~$\033[97m \033[93m\033[93m")
    
    sys.stdout.write("\033[97m\033[97m")
    sys.stdout.flush() 
    
    if cmd.lower() == "clear":
        os.system("cls")
        
    elif cmd.lower() == "clean":
        os.system("cls")
        
    elif cmd.lower() == "exit":
        sys.exit(1)
        
    elif cmd.lower() == "terminal --help":
        #\033[36m \033[0m
        print(f"""\033[36m  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     PC USER: {username}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    DIRECTORY: {directory}
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   VERSION: {version}
@@@@@@@@@@@@@@@@@@@@@@@&&#####&&@@@@@@@@@@@@@@@@@@@@@@@  COMPUTER NAME: {computer_name}
@@@@@@@@@@@@@@@@@@#BP55YYYYYYYYY55PB#@@@@@@@@@@@@@@@@@@ GITHUB: https://github.com/LouSkull
@@@@@@@@@@@@@@@#G5YYYYYYYYYYYYYYYYYYY5P#@@@@@@@@@@@@@@@
@@#BBGGPPP555Y?77??JYYYYYYYYYYYYYYYYYYYY5B@@@@@@@@@@@@@
@@@@@@@@@&&GJ???77!!~~!7JYYYYYYYYYYYYYYYYY5#@@@@@@@@@@@
@&#BGP55YY?!!!!7!!!!~^^:!5YYYYYYYYYYYYYYYYYYG@@@@@@@@@@
BBBB##&@@PJJ?7!!!!!!!!!?^7YYYYJJ?JYYYYYYYYYYYG@@@@@@@@@
@@@@@@&B5!!!77?JJYYYYYYJ^ :^^^~~~!!7JYYYYYYYYY#@@@@@@@@
@@@@BPPGJJJJJJJJJJJJYY~.!JYYYYJ?7~^:^7YYYYYYYYP@@@@@@@@
@@@@&@@@YJJJJJJJJJJJY7 7YYYYYYYYY5Y?^:~JYYYYYY5&@@@@@@@
@@@@@@@&YJJJJJJJJJJJY! !YYYYYYYYYYYY5Y7!JYYYYY5@@@@@@@@
@@@@@@@@5?JJJJJJJJJJJJ~ ~?JYYYYYYYYYYYYYYYYYYYP@@@@@@@@
@@@@@@@@#JJJJJJJJJJJJJY?~:^^~~~~~~!7?JYYYYYYYY#@@@@@@@@
@@@@@@@@@GJJJJJJJJJJJJJJYYJJJ????7!~::~!7JYYYB@@@@@@@@@
@@@@@@@@@@BJJJJJJJJJJJJJJJJJJJYYYYYYY?~~?!!YB@@@@@@@@@@
@@@@@@@@@@@#5JJJJJJJJJJJJJJJJJJJJJJYYYY!^YJJ@@@@@@@@@@@
@@@@@@@@@@@@@B5JJJJJJJJJJJJJJJJJJJJJJJJ57?@B@@@@@@@@@@@
@@@@@@@@@@@@@@@#G5JJJJJJJJJJJJJJJJJJY5G&@?@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&BGP5YYJJJJYYY5PG#&@@@@G&@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


\033[90mCommands:\033[0m \033[38;5;208m\033[38;5;208m
\033[90mHelp command\033[0m \033[94m(terminal --help)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mClear terminal\033[0m \033[94m(clear,clean)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mLook up for all files\033[0m \033[94m(ls)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mLook at your ip\033[0m \033[94m(ip --look)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mPing website\033[0m \033[94m(webcall (link))\033[94m \033[38;5;208m\033[38;5;208m
\033[90mInstall python lib\033[0m \033[94m(pyinstall (lib-name))\033[94m \033[38;5;208m\033[38;5;208m
\033[90mUninstall python lib\033[0m \033[94m(pyuninstall (lib-name))\033[94m \033[38;5;208m\033[38;5;208m
\033[90mLook at the terminal version\033[0m \033[94m(terminal --ver)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mChange title\033[0m \033[94m(set-title-console-(your_title))\033[94m \033[38;5;208m\033[38;5;208m


\033[90mAbout:\033[0m \033[38;5;208m\033[38;5;208m
\033[90mVERSION\033[0m \033[94m({version})\033[94m \033[38;5;208m\033[38;5;208m
\033[90mProgramming language\033[0m \033[94m(python)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mGITHUB\033[0m \033[94m(https://github.com/LouSkull)\033[94m \033[38;5;208m\033[38;5;208m
\033[90mDeveloper discord\033[0m (@ggrolton123)\033[38;5;208m\033[38;5;208m                     
\033[0m""")
        
    elif cmd.lower() == "ls":
        os.system("dir /b")
        
    elif cmd.lower() == "terminal --ver":
        print(version)
        
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
        os.system(f"pip install {python_lib_to_uninstall}")
        
    elif cmd.lower().startswith("set-title-console-"):
        new_console_title = cmd[18:]
        os.system(f"title {new_console_title}")
        
    else:
        try:
            os.system(f"{cmd}")
        except Exception as e:
            print("Command not recognized. Type 'help' or 'terminal --help' for assistance.")
