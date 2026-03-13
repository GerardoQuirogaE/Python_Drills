"""
Print numbers 1–100 but replace:
    Multiples of 3 → "Fuzz"
    Multiples of 5 → "Buzz"
    Multiples of both → "FuzzBuzz"
    Multiples of 7 → "Pop".
"""

numbers = list(range(1,101))

def Fuzz_Buzz_Replace(nums):
    for i in range(len(nums)):
        if nums[i] % 3 == 0:
            nums[i] = "Fizz"
        elif nums[i] % 5 == 0:
            nums[i] = "Buzz"
        elif nums[i] % 7 == 0:
            nums[i] = "pop"
    return nums

print(Fuzz_Buzz_Replace(numbers))


# nu = 4
# print(f"nu = {nu} ")
# print(f"numbers = {numbers[nu]}\n")

# print(numbers[nu]%2) # Prints 1

# print(type(numbers[nu]%2)) # <class 'int'> or 'float'.

