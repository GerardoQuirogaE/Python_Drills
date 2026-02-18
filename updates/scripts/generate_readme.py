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
SCRIPT_DIR = Path(__file__).resolve().parent
UPDATES_DIR = SCRIPT_DIR.parent
ROOT_DIR = UPDATES_DIR.parent

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

top_10 = manager.get_top_n(10)
top_3 = top_10[:3]

def generate_promotion_zone(top_3):
    zone = "## 🚀 Promotion Zone\n\n"

    for i, p in enumerate(top_3, start=1):
        zone += (
            f"### 🥇 Rank {i}\n"
            f"- **Name:** {p.first_name[:3]} {p.last_name[:3]}\n"
            f"- 💰 Pot: ${p.pot}\n"
            f"- 📞 Calls: {p.calls}\n"
            f"- ❌ Missed: {p.missed}\n"
            f"- 🚫 Wrong Calls: {p.wrong_calls}\n\n"
        )

    return zone

promotion_md = generate_promotion_zone(top_3)
content = content.replace("{{PROMOTION_ZONE}}", promotion_md)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated to Day {day_number}")
