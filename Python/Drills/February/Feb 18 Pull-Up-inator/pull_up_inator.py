import json
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
REGISTRY_PATH = BASE_DIR / "data" / "registry.json"

def load_registry():
    if not REGISTRY_PATH.exists():
        print("Registry file not found.")
        sys.exit(1)

    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def open_image(path):
    full_path = BASE_DIR / path

    if not full_path.exists():
        print("Image not found.")
        return

    os.startfile(full_path)  # Windows only


def open_text_file(path):
    full_path = BASE_DIR / path

    if not full_path.exists():
        print("Text file not found.")
        return

    with open(full_path, "r", encoding="utf-8") as f:
        print("\n--- FILE CONTENT ---\n")
        print(f.read())


def handle_request(key, registry):
    if key not in registry:
        print("Item not found.")
        return

    item = registry[key]
    item_type = item["type"]

    if item_type == "text_inline":
        print("\n--- MESSAGE ---\n")
        print(item["content"])

    elif item_type == "text_file":
        open_text_file(item["path"])

    elif item_type == "image":
        open_image(item["path"])

    else:
        print("Unknown type.")

def main():
    registry = load_registry()

    print("🔥 Pull-Up-Inator Activated 🔥")
    print("Available commands:")
    print(", ".join(registry.keys()))

    while True:
        user_input = input("\nWhat do you want to pull up? (or 'exit'): ").strip()

        if user_input.lower() == "exit":
            print("Shutting down Pull-Up-Inator...")
            break

        handle_request(user_input, registry)


if __name__ == "__main__":
    main()