import subprocess

from themes import SylaThemes
from move import MoveGeneratedFile
from menu import user_menu


palette = user_menu()

theme = SylaThemes(palette)
colors = theme.load_palette()
theme.generate_files(colors)

move = MoveGeneratedFile()
move.move_files()

subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "reload_config"])
subprocess.run(["dunstctl", "reload"])