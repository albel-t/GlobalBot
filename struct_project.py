import os
from pathlib import Path

def create_project_tree(start_path: str = ".", max_depth: int = 6):
    """Создает дерево файлов проекта"""
    ignore_dirs = {'.git', '__pycache__', '.vscode', '.idea', 'venv', 'env'}
    ignore_files = {'.DS_Store', '.gitignore'}
    
    def build_tree(path: Path, prefix: str = "", depth: int = 0):
        if depth > max_depth:
            return []
            
        lines = []
        try:
            items = sorted([item for item in path.iterdir() 
                          if item.name not in ignore_dirs and item.name not in ignore_files])
            
            for index, item in enumerate(items):
                is_last = index == len(items) - 1
                connector = "└── " if is_last else "├── "
                
                if item.is_dir():
                    lines.append(f"{prefix}{connector}{item.name}/")
                    extension = "    " if is_last else "│   "
                    lines.extend(build_tree(item, prefix + extension, depth + 1))
                else:
                    lines.append(f"{prefix}{connector}{item.name}")
                    
        except PermissionError:
            lines.append(f"{prefix}└── [Permission Denied]")
            
        return lines
    
    root_path = Path(start_path)
    tree_lines = [f"{root_path.name}/"] + build_tree(root_path)
    return "\n".join(tree_lines)

if __name__ == "__main__":
    tree = create_project_tree()
    print("🌳 СТРУКТУРА ПРОЕКТА:")
    print("=" * 50)
    print(tree)