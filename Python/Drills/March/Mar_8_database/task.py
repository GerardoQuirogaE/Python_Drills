import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/tasks.jsonl")


def generate_task_id():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"task_{timestamp}"


def ask_categories():
    raw = input("Categories (separate with ';'): ")
    return [c.strip() for c in raw.split(";") if c.strip()]


def create_task():

    print("\n--- Create New Task ---\n")

    title = input("What task do you have: ")

    due_date = input("Due date (YYYY-MM-DD): ")

    due_time = input("Due time (HH:MM): ")

    est_duration = int(input("Estimated duration (minutes): "))

    categories = ask_categories()

    priority = input("Priority (1-5 optional): ")

    task_id = generate_task_id()

    event = {
        "event": "task_created",
        "task_id": task_id,
        "title": title,
        "due_date": due_date,
        "due_time": due_time,
        "estimated_duration_min": est_duration,
        "categories": categories,
        "priority": priority,
        "created_at": datetime.now().isoformat()
    }

    with open(DATA_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    print("\nTask created successfully.")
    print("Task ID:", task_id)


if __name__ == "__main__":
    create_task()