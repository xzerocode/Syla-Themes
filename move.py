from pathlib import Path
import shutil


class MoveGeneratedFile():
    def __init__(self):
        self.qtile_file_path = Path.home() / ".config/qtile/theme.py"
        self.kitty_file_path = Path.home() / ".config/kitty/kitty.conf"
        self.fish_file_path = Path.home() / ".config/fish/themes/theme.fish"
        self.dunst_file_path = Path.home() / ".config/dunst/dunstrc"
        self.rofi_file_path = Path.home() / ".config/rofi/themes/launcher.rasi"
        
    def _move_qtile(self):
        generated_file = Path("generated/theme.py")
        
        shutil.copy(generated_file, self.qtile_file_path)
    
    def _move_kitty(self):
        generated_file = Path("generated/kitty.conf")
        
        shutil.copy(generated_file, self.kitty_file_path)
        
    def _move_fish(self):
        generated_file = Path("generated/theme.fish")
        
        shutil.copy(generated_file, self.fish_file_path)

    def _move_dunst(self):
        generated_file = Path("generated/dunstrc")
        
        shutil.copy(generated_file, self.dunst_file_path)

    def _move_rofi(self):
        generated_file = Path("generated/launcher.rasi")
        
        shutil.copy(generated_file, self.rofi_file_path)

    def move_files(self):
        self._move_qtile()
        self._move_kitty()
        self._move_fish()
        self._move_dunst()
        self._move_rofi()