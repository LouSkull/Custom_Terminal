import os
import getpass
import customtkinter as ctk

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("visible: \nterminal_size: \n")

def update_config(file_path, key, new_value):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(key):
                line = f"{key}: {new_value}\n"
            file.write(line)

def on_update_visible():
    new_value = visible_entry.get()
    update_config(config_path, "visible", new_value)
    result_label.configure(text="Visible value updated successfully.")

def on_update_terminal_size():
    new_value = terminal_size_entry.get()
    update_config(config_path, "terminal_size", new_value)
    result_label.configure(text="Terminal size value updated successfully.")

username = getpass.getuser()
config_dir = os.path.join("C:\\Users", username, "AppData", "Roaming", "Terminal")
config_path = os.path.join(config_dir, "config.txt")

ensure_directory_exists(config_dir)
ensure_file_exists(config_path)

root = ctk.CTk()
root.title("Config Updater")

visible_label = ctk.CTkLabel(root, text="Enter new value for 'visible':")
visible_label.pack(pady=5)
visible_entry = ctk.CTkEntry(root)
visible_entry.pack(pady=5)
visible_button = ctk.CTkButton(root, text="Update Visible", command=on_update_visible)
visible_button.pack(pady=5)

terminal_size_label = ctk.CTkLabel(root, text="Enter new value for 'terminal_size':")
terminal_size_label.pack(pady=5)
terminal_size_entry = ctk.CTkEntry(root)
terminal_size_entry.pack(pady=5)
terminal_size_button = ctk.CTkButton(root, text="Update Terminal Size", command=on_update_terminal_size)
terminal_size_button.pack(pady=5)

result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=5)

root.mainloop()
