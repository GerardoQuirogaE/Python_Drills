import time
import os
import math

counter = 0

w_hours = 0
w_mins = 0
w_seconds = 0

speed = 1 #how many updates/second

## Start
print("Create a custom pomodoro timer!")

activation = input("Would you like to begin [y] or [n]: ").lower()
while activation not in ("y", "n"):
    print("That is not a correct value.")
    activation = input("Would you like to begin [y] or [n]: ").lower


while activation == "y":
    # if w_mins == 59: # Debugging
    #     speed = 0.25

    interval = input("What is the work interval: ")
    in_between_time = input("How long is the break in between: ")

    w_hours = int(math.floor(counter/(3600)))
    w_mins = int(math.floor((counter/60)-(60*w_hours)))
    w_seconds = int(math.floor((counter)-((60*w_mins)+((3600)*w_hours))))

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Active Pomodoro Timer:\n\n")
    print(f"Time worked so far: {w_hours}-h {w_mins}-m {w_seconds}-s:")

    counter += 1
    time.sleep(speed)



concern = 0
prompts = []

while activation == "n":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(concern)

    if concern == 7:
        print("\n\n\nTake a screenshot and send it to me to claim $1 cash bonus 📸 🎉 💸")
        print("Valid from Feb 26 - 27 @ 23:50")
        print("\nAchievement Unlocked: 'Honest Thinker: Give 7 pices of feedback to a project.'\n")
        time.sleep(1)
        print("3.")
        time.sleep(1)
        print("2.")
        time.sleep(1)
        print("1.")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    prompt = input("What are the problems?: ")

    while len(prompt.split()) < 3:
        prompt = input("The problem is more complex than 3 words: ")

    if prompt not in list(prompts):
        concern += 1
        prompts.append(prompt)
