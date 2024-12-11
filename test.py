guessed_numbers = [1, 2, 3, 8, 3, 5]

for i in range(6):
    print(i)
    print(not isinstance(guessed_numbers[i], int))
    print(guessed_numbers[i] not in list(range(1, 50)))
    print(guessed_numbers[i] in guessed_numbers)

