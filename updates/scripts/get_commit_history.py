import subprocess

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
    print(date, "-", message)