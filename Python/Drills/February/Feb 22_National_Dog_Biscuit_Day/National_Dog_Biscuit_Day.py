import random
import webbrowser

# List of gif URLs
buiscuit = [
    "https://giphy.com/embed/4j9yvl6PQYdHIOlhLO",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3RsN2JtbTg3Y3Z0M3p2Z21neGJxeGhveXJ0aDk5MHhmZ3hxa3NubyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J2ohcJKGI6eHQh6YIW/giphy.gif",
    "https://giphy.com/embed/1fhj2W53BjaVVib2A2",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmM0dDNxbjlhajBsMjh6bjFzZHptbzdhYmozc3Jxc3B6M3gyc3I2MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/DdFJCeDKpcYRa/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmM0dDNxbjlhajBsMjh6bjFzZHptbzdhYmozc3Jxc3B6M3gyc3I2MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9Sm4nl7cr10VFpbSD6/giphy.gif"
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmM0dDNxbjlhajBsMjh6bjFzZHptbzdhYmozc3Jxc3B6M3gyc3I2MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7UtUgAeIXFbCU/giphy.gif"
]

# Pick a random gif
buiscuit = random.choice(buiscuit)

# Open in browser
webbrowser.open(buiscuit)


print("Happy National Dog Biscuit Day...")
print("I am being serius, that is a thing for some reason...")