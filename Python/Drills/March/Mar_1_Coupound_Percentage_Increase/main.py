# 1% Better every day for a week

# Function will calculate % increase
# for every number in n.

# Today = 1 so a Week 7
def percent_better(n=7):
    initial_today = 100
    today=initial_today
    increase=.01
    day_n = 1
    init_inc = increase
    # init_n = day_n

    # def double_pur(init_today=initial_today, init_n=init_n):
    #     while init_n =! 0
    #         init_today = init_today+init_today*increase
    
    while n != 0:
        today=today+today*increase
        per_inc = (today-100)
        n = n - 1
        print(f"% increase for day {day_n} is {per_inc:,.3f}%.")
        day_n = day_n + 1

    day_n = day_n - 1

    print(f"\n\nStats:")
    print("--------")
    print(f"For {day_n} days, compounding {init_inc*100}% each day:")
    print(f"Percentage increase: {per_inc:,.3f}%")
    print(f"Percentage gain: {per_inc-(increase*day_n*100):,.3f}%\n")
    # print("If you were {}% better every day, you would be: {}% better right now.")
    # print("")
    
calc = percent_better(int(input("How many days: ")))
