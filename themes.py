from pathlib import Path
import json


class SylaThemes():
    def __init__(self, palette):
        self.syla_dir = Path.home() / ".config/syla/Themes/colors"
        self.name = palette
        
    def load_palette(self) -> dict:
        file_path = self.syla_dir / f"{self.name}_palette.json"
    
        with open(file_path, 'r', encoding='utf-8') as fichero:
            colors = json.load(fichero)
        
            return colors
    
    def generate_qtile_theme(self, colors: dict):
        template_path = Path("templates/qtile_theme.py.template")
        output_path = Path("generated/theme.py")

        template_content = template_path.read_text()
        
        rendered_template = template_content.format(colors=json.dumps(colors, indent=4))

        output_path.write_text(rendered_template)