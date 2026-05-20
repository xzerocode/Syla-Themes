import subprocess

from themes import SylaThemes
from menu import user_menu


palette = user_menu()

theme = SylaThemes(palette)

colors = theme.load_palette()
theme.generate_qtile_theme(colors)


subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "reload_config"])