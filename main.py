import subprocess

from themes import SylaThemes
from move import MoveGeneratedFile
from menu import user_menu
from wallpaper import change_background


palette = user_menu()

change_background(palette)

theme = SylaThemes(palette)
colors = theme.load_palette()
theme.generate_files(colors)

move = MoveGeneratedFile()
move.move_files()

subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "reload_config"])
subprocess.run(["dunstctl", "reload"])