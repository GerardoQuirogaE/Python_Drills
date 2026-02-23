import random
import webbrowser
from pathlib import Path

buiscuit_list = [
    "https://giphy.com/embed/4j9yvl6PQYdHIOlhLO",
    "https://media.giphy.com/media/1fhj2W53BjaVVib2A2/giphy.gif",
    "https://media.giphy.com/media/DdFJCeDKpcYRa/giphy.gif",
    "https://media.giphy.com/media/9Sm4nl7cr10VFpbSD6/giphy.gif",
    "https://media.giphy.com/media/7UtUgAeIXFbCU/giphy.gif"
]

meme = random.choice(buiscuit_list)

html_content = f"""
<html>
<body>
<script>
window.open("{meme}", "_blank", "width=500,height=500");
window.close();
</script>
</body>
</html>
"""

file_path = Path("popup.html")
file_path.write_text(html_content, encoding="utf-8")

webbrowser.open(file_path.resolve().as_uri())

print("Happy National Dog Biscuit Day...")