"""
Todays code shows how to update a readme file using a template
and variable content by using the read and write modes over files,
and by using the .replace() functions to select where the content
would be displayed on the template.
"""
## Import Section
from datetime import datetime
from pathlib import Path
import random

"""
This is path handling.
__file__ = path of current script
Path(__file__).resolve() = Gets the absolute path to the script.
.parent moves the dir one up
    from: Python_Drills/updates/scripts/generate_readme.py
    to: Python_Drills/updates/scripts/
and we repeat this identification of path for:
    1. This script
    2. Updates dir (where we have the template)
    3. Root dir (Where our real readme lives)
Then we are defining the path to the template and to the README output.
"""
## Grounding Directory
ROOT = Path(__file__).resolve().parent

## Assigning Paths
TEMPLATE_PATH = ROOT / "TEMPLATE.md"
OUTPUT_PATH = ROOT / "Test_me_README.md"


"""
Here we code our variable content
"""
## Variable Data on this Project
START_DATE = datetime(2026, 2, 11)
today = datetime.now()
day_number = (today - START_DATE).days + 1
today_str = today.strftime("%m/%d/%Y")

## Random Image Generator

random_number = random.randint(1,5)
random_image = f"Image_#{random_number}.jpg"

"""
The following section utilizes the variable `content`
to make it:
    1. Contain the information from the template
    2. Replace {{VARIABLE}} with our variable content.
"""
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("{{DAY}}", str(day_number))
content = content.replace("{{DATE}}", today_str)
content = content.replace("{{STREAK}}", "Active")
content = content.replace("{{RANDOM_IMG}}", random_image)

"""
The following section will open our 
`Test_me_README.md` file in the write `w` mode, 
and completely replace its contents with our
`content` variable.

"""
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(content)


"""Lastly, give feedback to signify success
"""
print(f"Test_me_README Updated to Day {day_number} successfuly.")