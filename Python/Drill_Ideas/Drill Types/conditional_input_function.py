import time
import os

options = ["one", "two", "three"]

def user_defined_output(user_input):
    for i in options:
        if user_input != i:
            print("This is not a correct input value")
        else: output = user_input


user_input = input("What outcome do you want [one] or [two]: ")
user_input = user_defined_output(user_input)