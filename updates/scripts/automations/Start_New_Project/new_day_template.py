from datetime import datetime
from pathlib import Path

def create_proj(dir_path, filename, content=""):

    # Create the directory if it doesn't exist
    dir_path.mkdir(parents=True, exist_ok=True)

    # Create full file path
    file_path = dir_path / filename

    # Create and write to the file
    file_path.write_text(content, encoding="utf-8")

    return file_path


ROOT_DIR = Path(__file__).resolve().parents[4]
TODAY = datetime.now().strftime("%b %d")

proj_name = input("What's the project's name: ")

filename = proj_name + ".py"

folder_name = TODAY + "_" + proj_name

while True:
    try:
        type_of_proj = int(input("Is the project TODAYS DRILL [1] or a DRILL IDEA? [2]: "))
        if type_of_proj in (1, 2): break
        else: print("Invalid Input")
    except ValueError:
        print("Please enter 1 or 2.")
    
if type_of_proj == 1:
    # Create proj pack under drills/
    dir_path = ROOT_DIR / "Python" / "Drills" / folder_name / proj_name

else:
    # Create proj pack under drill_ideas/
    dir_path = ROOT_DIR / "Python" / "Drill_Ideas" / proj_name

create_proj(dir_path, filename)