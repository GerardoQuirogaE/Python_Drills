from pathlib import Path

# -------- CONFIG --------
BASE_FILE = Path("Feb_19_News.md")
INSERT_FILE = Path("github_actions.md")
OUTPUT_DIR = Path("output")
PLACEHOLDER = "{{GITHUB ACTIONS}}"
# ------------------------

def read_file(path):
    if not path.exists():
        raise FileNotFoundError(f"{path} not found.")
    return path.read_text(encoding="utf-8")

def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def replace_placeholder(base_text, insert_text, placeholder):
    if placeholder not in base_text:
        print("⚠ Placeholder not found.")
    return base_text.replace(placeholder, insert_text)

def main():
    print("Reading base file...")
    base_content = read_file(BASE_FILE)

    print("Reading insert file...")
    insert_content = read_file(INSERT_FILE)

    print("Replacing placeholder...")
    updated_content = replace_placeholder(
        base_content,
        insert_content,
        PLACEHOLDER
    )

    output_path = OUTPUT_DIR / f"{BASE_FILE.stem}_updated.md"

    print("Writing updated file...")
    write_file(output_path, updated_content)

    print(f"✅ Done. Output saved to {output_path}")

if __name__ == "__main__":
    main()