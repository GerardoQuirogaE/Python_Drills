# 1% Better every day for a week

# Function will calculate % increase
# for every number in n.

# Today = 1 so a Week 7
def percent_better(n=7):
    today=100
    increase=.01
    day_n = 1
    
    while n != 0:
        today=today+today*increase
        per_inc = (today-100)
        n = n - 1
        print(f"% increase for day {day_n} is {per_inc}%.")
        day_n = day_n + 1
    print(f"\n\nStats:")
    print("--------")
    print(f"Amount of Days: {day_n}")
    # print("")
    
calc = percent_better(int(input("How many days")))