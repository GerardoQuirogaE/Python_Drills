from datetime import datetime

START_DATE = datetime(2026, 2, 11)
today = datetime.now()

day_number = (today - START_DATE).days + 1
today_str = today.strftime("%m/%d/%Y")

with open("README.template.md", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("{{DAY}}", str(day_number))
content = content.replace("{{DATE}}", today_str)
content = content.replace("{{STREAK}}", "Active")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated to Day {day_number}")
