import random

guessing_number = random.randint(1, 100)
guessed_number = 0
print(guessing_number)

while guessed_number != guessing_number:
    try:
        guessed_number = int(input("Guess the number: "))
    except ValueError:
        print("It is not a number!")
        continue
    if guessed_number < guessing_number:
        print("Too small!")
    elif guessed_number > guessing_number:
        print("Too big!")
    else:
        print("You win!")
