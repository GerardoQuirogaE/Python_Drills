import subprocess

print("Make sure your working dir is updates/")

print("Generating README...")
subprocess.run(["python", "scripts/generate_readme.py"])
print("README updated.")
