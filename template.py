from pathlib import Path
import os


p_name = "Depth-detector"
files = [
    ".github/workflows/.gitkeep",
    f"src/{p_name}/__init__.py",
    f"src/{p_name}/components/__init__.py",
    f"src/{p_name}/utils/__init__.py",
    f"src/{p_name}/config/__init__.py",
    f"src/{p_name}/config/configuration.py",
    f"src/{p_name}/pipeline/__init__.py",
    f"src/{p_name}/entity/__init__.py",
    f"src/{p_name}/constants/__init__.py",
    "config/configuration.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py"
]

for file in files:
    path = Path(file)
    f_dir,f_name = os.path.split(path)
    if f_dir!="":
        os.makedirs(f_dir,exist_ok=True)

    with open(path,"w") as n:
        pass







