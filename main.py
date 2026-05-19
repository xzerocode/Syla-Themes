from pathlib import Path
import json
import subprocess


SYLA_DIR = Path.home() / ".config/syla/Themes/colors"
QTILE_THEME_PATH = Path.home() / ".config/qtile/theme.py"

print(f"Temas disponibles: \n- cyan\n- aether\n- glitch\n")
palette = input("Que tema quieres usar?: ")

CURRENT_THEME = palette

def load_palette(name: str) -> dict:
    file_path = SYLA_DIR / f"{name}_palette.json"
    
    with open(file_path, 'r', encoding='utf-8') as fichero:
        colors = json.load(fichero)
        
        return colors
    
def generate_qtile_theme(colors: dict):
    content = f"""colors = {json.dumps(colors, indent=4)}"""

    QTILE_THEME_PATH.write_text(content)
    
def main():
    colors = load_palette(CURRENT_THEME)
    generate_qtile_theme(colors)
    subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "reload_config"])


if __name__ == "__main__":
    main()