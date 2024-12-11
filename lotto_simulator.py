import random

separator = 40*"_"
guessing_numbers = random.sample(range(1, 50), 6)
print(guessing_numbers)

def user_input():
    guessed_numbers = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        print(separator)
        print(f"Your numbers: {guessed_numbers[:i]}")
        while not (guessed_numbers[i] in list(range(1, 50)) and guessed_numbers[i] not in guessed_numbers[:i]):
            try:
                guessed_numbers[i] = int(input("Enter a number: "))
            except ValueError:
                print("Invalid input")
                print(f"Your numbers: {guessed_numbers[:i]}")
                print(separator)
                continue
            if guessed_numbers[i] in guessed_numbers[:i]:
                print("You have already guessed that number.")
                print(f"Your numbers: {guessed_numbers[:i]}")
                print(separator)
                continue
            elif guessed_numbers[i] not in range(1, 50):
                print("Out of range.")
                print(f"Your numbers: {guessed_numbers[:i]}")
                print(separator)
                continue
    return guessed_numbers

def counter(list1, list2):
    counter = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            counter += 1
    return counter

guessed_numbers = user_input()
print(f"Your numbers are: {sorted(guessed_numbers)}")
print(f"Numbers to be guessed are: {guessing_numbers}")
print(f"You guessed {counter(guessed_numbers, guessing_numbers)} numbers correctly.")






