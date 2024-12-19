import random

def roll_the_dice(dice):
    result = random.randint(1, int(dice[dice.index("D")+1:]))
    return result

def game_2001():
    user = 0
    computer = 0
    dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    separator = "-" * 40
    i = 1
    while user < 2001 and computer < 2001:
        print(f"Current score:\n"
              f"User: {user}\n"
              f"Computer {computer}")
        print(separator)

        if i == 1:
            try:
                users_choice1 = input(f"Choose the first dice from the list: {dices}")
                users_choice2 = input(f"Choose the second dice from the list: {dices}")
                first_roll = roll_the_dice(users_choice1)
                second_roll = roll_the_dice(users_choice2)
                user += first_roll + second_roll
                computer += roll_the_dice(random.choice(dices)) + roll_the_dice(random.choice(dices))
                i += 1
            except ValueError:
                print("Invalid input. Try again")
                print(separator)
                continue
        else:
            try:
                users_choice1 = input(f"Choose the first dice from the list: {dices}")
                users_choice2 = input(f"Choose the second dice from the list: {dices}")
                first_roll = roll_the_dice(users_choice1)
                second_roll = roll_the_dice(users_choice2)
                if first_roll + second_roll == 7:
                    user //= 7
                elif first_roll + second_roll == 11:
                    user *= 11
                else:
                    user += first_roll + second_roll
                first_roll = roll_the_dice(random.choice(dices))
                second_roll = roll_the_dice(random.choice(dices))
                if first_roll + second_roll == 7:
                    computer //= 7
                elif first_roll + second_roll == 11:
                    computer *= 11
                else:
                    computer += first_roll + second_roll
            except ValueError:
                print("Invalid input. Try again")
                print(separator)
                continue

    if user > 2001 and computer > 2001:
        return "It is a draw!"
    elif user > 2001:
        return "You win!"
    else:
        return "Computer wins!"

print(game_2001())