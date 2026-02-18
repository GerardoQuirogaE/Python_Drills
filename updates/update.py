import subprocess

print("Generating README...")
subprocess.run(["python", "scripts/generate_readme.py"])
print("README updated.")
