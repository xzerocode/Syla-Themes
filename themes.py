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
    
    def _generate_qtile_theme(self, colors: dict):
        template_path = Path("templates/qtile_theme.py.template")
        output_path = Path("generated/theme.py")

        template_content = template_path.read_text()
        
        rendered_template = template_content.format(colors=json.dumps(colors, indent=4))

        output_path.write_text(rendered_template)
    
    def _generate_kitty_theme(self, colors: dict):
        template_path = Path("templates/kitty.conf.template")
        output_path = Path("generated/kitty.conf")
        
        template_content = template_path.read_text()
        
        rendered_template = template_content.format(**colors)
        
        output_path.write_text(rendered_template)
        
    def _generate_fish_theme(self, colors: dict):
        template_path = Path("templates/theme.fish.template")
        output_path = Path("generated/theme.fish")
        
        template_content = template_path.read_text()
        
        rendered_template = template_content.format(**colors)
        
        output_path.write_text(rendered_template)
        
    def _generate_dunst_theme(self, colors: dict):
        template_path = Path("templates/dunst.template")
        output_path = Path("generated/dunstrc")
        
        template_content = template_path.read_text()
        
        rendered_template = template_content.format(**colors)
        
        output_path.write_text(rendered_template)
        
    def _generate_rofi_theme(self, colors: dict):
        template_path = Path("templates/launcher.rasi.template")
        output_path = Path("generated/launcher.rasi")
        
        template_content = template_path.read_text()
        
        rendered_template = template_content.format(**colors)
        
        output_path.write_text(rendered_template)
        
    def generate_files(self, colors: dict):
        self._generate_qtile_theme(colors)
        self._generate_kitty_theme(colors)
        self._generate_fish_theme(colors)
        self._generate_dunst_theme(colors)
        self._generate_rofi_theme(colors)