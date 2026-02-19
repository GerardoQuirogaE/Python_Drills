from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "Python" / "Drills" / "Feb 15 Participants Database Leaderboard"))

from leaderboard_manager import LeaderboardManager

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
SCRIPT_DIR = Path(__file__).resolve().parent # Python_Drills/updates/scripts/
UPDATES_DIR = SCRIPT_DIR.parent # Python_Drills/updates/
ROOT_DIR = UPDATES_DIR.parent # Python_Drills/

TEMPLATE_PATH = UPDATES_DIR / "README.template.md"
OUTPUT_PATH = ROOT_DIR / "README.md"


START_DATE = datetime(2026, 2, 11)
today = datetime.now()

day_number = (today - START_DATE).days + 1
today_str = today.strftime("%m/%d/%Y")

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("{{DAY}}", str(day_number))
content = content.replace("{{DATE}}", today_str)
content = content.replace("{{STREAK}}", "Active")

manager = LeaderboardManager(str(ROOT_DIR / "Data" / "Participants" / "participants.json"))
manager.load_data()
manager.sort_leaderboard()

top_10 = manager.get_top_n_leaderboard(10)
top_3 = top_10[:3]
top_10 = top_10[3:]

def generate_promotion_zone(top_3):     
    zone = "\n## 💎 Top 3 Players\n\n"
    zone += "| Rank | Name | Total Cash ($) | Good Calls | Missed Calls | Bad Calls |\n"
    zone += "|------|------|---------|-------|--------|------------|\n"

    for rank, p in enumerate(top_3, start=1):
        name = f"{p.first_name} {p.last_name}"+ "&nbsp;"*40
        zone += f"| #{rank} | {name} | ${p.cash_collected} | {p.good_calls} | {p.missed_calls} | {p.rejected_calls} |\n"

    zone += "\n"
    return zone

def generate_top_10_table(top_10):
    table = "\n## ⭐ Leaderboard\n\n"
    table += "| Rank | Name | Total Cash ($) | Missed Calls |\n"
    table += "|------|---------|-------|--------|\n"

    for rank, p in enumerate(top_10, start=4):
        name = f"{p.first_name} {p.last_name}"
        table += f"| #{rank} | {name} | {p.cash_collected} | {p.missed_calls} |\n"

    table += "\n"
    return table

promotion_md = generate_promotion_zone(top_3)
content = content.replace("{{PROMOTION_ZONE}}", promotion_md)

top_10_table_md = generate_top_10_table(top_10)
content = content.replace("{{TOP_10_LEADERBOARD}}", top_10_table_md)

update_file_name = f"update_{today.strftime('%b_%d')}.md"  # e.g., update_Feb_15.md
update_path = UPDATES_DIR / update_file_name

if update_path.exists():
    with open(update_path, "r", encoding="utf-8") as f:
        latest_update_md = f.read()
else:
    latest_update_md = "_No updates yet._"

content = content.replace("{{LATEST_UPDATE}}", latest_update_md)


with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated to Day {day_number}")
