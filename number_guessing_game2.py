
minimum = 0
maximum = 1000
answer = ""

print("""
Think about a number
from 0 to 1000 and
let me guess it!
""")

while answer.lower() != "you won":
    print(f"Guessing: {(guess := (int((maximum - minimum) / 2) + minimum))}")
    answer = input("Your answer: ")
    if answer.lower() == "too high":
        maximum = guess
    elif answer.lower() == "too low":
        minimum = guess
    elif answer.lower() == "you won":
        print("I won!")
    else:
        print("Sorry, that's not a valid input")

