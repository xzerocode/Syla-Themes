import subprocess

def change_background(theme):
    
    if theme == "cyan":
        subprocess.run(["feh", "--bg-fill", "/home/xavier/.config/syla/Themes/wallpapers/gwen.jpg"])
    elif theme == "aether":
        subprocess.run(["feh", "--bg-fill", "/home/xavier/.config/syla/Themes/wallpapers/gardevoircomic.png"])
    elif theme == "glitch":
        subprocess.run(["feh", "--bg-fill", "/home/xavier/.config/syla/Themes/wallpapers/zerotwoxhiro.png"])
    else:
        None