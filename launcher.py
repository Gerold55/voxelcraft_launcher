import tkinter as tk
from tkinter import filedialog
import subprocess

def launch_game(mods, texture_pack):
    # Replace 'game_executable_path' with the actual path to your voxel game executable
    game_executable_path = 'path/to/your/voxel/game/executable'
    command = [game_executable_path]
    
    if mods:
        command.extend(['--mods', mods])
    if texture_pack:
        command.extend(['--texture', texture_pack])

    subprocess.run(command)

def choose_mods():
    mods_file = filedialog.askopenfilename(title="Choose Mods", filetypes=[("Mod files", "*.mod")])
    return mods_file

def choose_texture_pack():
    texture_pack_file = filedialog.askopenfilename(title="Choose Texture Pack", filetypes=[("Texture Pack files", "*.zip")])
    return texture_pack_file

def main():
    root = tk.Tk()
    root.title("Voxel Game Launcher")

    mods_label = tk.Label(root, text="Selected Mods: None")
    texture_label = tk.Label(root, text="Selected Texture Pack: None")
    mods_label.pack()
    texture_label.pack()

    def choose_mods_button():
        mods_file = choose_mods()
        if mods_file:
            mods_label.config(text=f"Selected Mods: {mods_file}")

    def choose_texture_pack_button():
        texture_pack_file = choose_texture_pack()
        if texture_pack_file:
            texture_label.config(text=f"Selected Texture Pack: {texture_pack_file}")

    def launch_game_button():
        mods = mods_label.cget("text").split(": ")[1]
        texture_pack = texture_label.cget("text").split(": ")[1]
        launch_game(mods, texture_pack)

    mods_button = tk.Button(root, text="Choose Mods", command=choose_mods_button)
    texture_button = tk.Button(root, text="Choose Texture Pack", command=choose_texture_pack_button)
    launch_button = tk.Button(root, text="Launch Voxel Game", command=launch_game_button)
    exit_button = tk.Button(root, text="Exit", command=root.destroy)

    mods_button.pack()
    texture_button.pack()
    launch_button.pack()
    exit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
