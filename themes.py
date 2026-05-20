from pathlib import Path
import json


class SylaThemes():
    def __init__(self, palette):
        self.syla_dir = Path.home() / ".config/syla/Themes/colors"
        self.qtile_theme = Path.home() / ".config/qtile/theme.py"
        self.name = palette
        
    def load_palette(self) -> dict:
        file_path = self.syla_dir / f"{self.name}_palette.json"
    
        with open(file_path, 'r', encoding='utf-8') as fichero:
            colors = json.load(fichero)
        
            return colors
    
    def generate_qtile_theme(self, colors: dict):
        content = f"""colors = {json.dumps(colors, indent=4)}"""

        self.qtile_theme.write_text(content)