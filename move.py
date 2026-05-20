from pathlib import Path
import shutil


class MoveGeneratedFile():
    def __init__(self):
        self.qtile_file_path = Path.home() / ".config/qtile/theme.py"
        
    def move_qtile(self):
        generated_file = Path("generated/theme.py")
        
        shutil.copy(generated_file, self.qtile_file_path)