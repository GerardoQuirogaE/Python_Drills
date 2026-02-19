from datetime import datetime
from pathlib import Path
import subprocess
import sys

# SCRIPT_DIR = Path(__file__).resolve().parent # Python_Drills/updates/scripts/
# UPDATES_DIR = SCRIPT_DIR.parent # Python_Drills/updates/
# ROOT_DIR = UPDATES_DIR.parent # Python_Drills/

# TEMPLATE_PATH = UPDATES_DIR / "README.template.md"
# OUTPUT_PATH = ROOT_DIR / "README.md"

"""
Here I am getting the commit history by runing subprocess git log %H %ad %s
    %H = Full commit hash
    %ad = Author date
    %s = Commit message
    The output is separated by pipes so they look like this:
        b82a7d1910ac|2026-02-17|Fix CSV export bug
"""
def get_commit_history():
    result = subprocess.run( # subprocess is like runing terminal
        ["git", "log", "--pretty=format:%H|%ad|%s", "--date=short"], # command: git log %H %ad %s
        capture_output=True,
        text=True
    )
    return result.stdout.split("\n") # this groups all strings (individual commits) into a list.

history = get_commit_history()

for commit in history: 
    commit_hash, date, message = commit.split("|", 2)
    """this breaks the sections into individual components & assigns commit_hash 
        to commit hash (e.g. commit_hash = "a3f9c12b89d3" or date = "2026-02-18")"""

    def generate_commits_table(history):     
        zone = "\n## 💎 Top 3 Players\n\n"
        zone += "| Rank | Name | Total Cash ($) | Good Calls | Missed Calls | Bad Calls |\n"
        zone += "|------|------|---------|-------|--------|------------|\n"

        for rank, p in enumerate(history, start=1):
            name = f"{p.first_name} {p.last_name}"+ "&nbsp;"*40
            zone += f"| #{rank} | {name} | ${p.cash_collected} | {p.good_calls} | {p.missed_calls} | {p.rejected_calls} |\n"

        zone += "\n"
        return zone



"""
Goal:
Commit Script Generator.

I want to update a markdown table with my daily commit history.
To do this, I know there is a function that can get you your commit history, 
    and you can add parameters like to keep it within today.
Then I know that I can write that into a file, I wonder if I can just update 
    a table with that information
Then wether I use the information directly, or I have to write a file, then
    read it with another function, I know it is possible to get that info.
Now with that info, update a table in markdown.
Easy.

"""