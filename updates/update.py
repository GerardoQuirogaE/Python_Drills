import subprocess

print(f"\n\nMake sure your working dir is updates/\n")

print(f"What type of command are you trying to run:\n\n"
      f"Update Main Readme \t\t[1]\n"
      f"Start Today's Project \t\t[2]\n"
      f"Work Ahead on a Buffer Project \t[3]\n"
      f"Promote a Buffer Project \t[4]\n"
      f"Make/Update Todays Newsletter \t[5]\n"
      f"Write Down a Drill Idea \t[6]\n")
command = input(": ")


print("Generating README...")
subprocess.run(["python", "scripts/generate_readme.py"])
print("README updated.")
