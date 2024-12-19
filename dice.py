import random


def roll_the_dice(formula: str):
    """
    Rolling the dice in format xDy+z \n
    x...number of dices \n
    y...number of sides of dice \n
    +z...factor to add \n
    -z...factor to subtract
    :param formula:
    :return:
    """
    if "D" not in formula:
        return "Not a valid input."
    elif formula[0] == "D":
        number_of_dices = 1
    elif formula[0] != "D":
        i = 0
        while formula[i].isdigit():
            i += 1
        number_of_dices = int(formula[0:i])
    else:
        return "Not a valid input."

    i = formula.index("D")
    try:
        while True:
            if formula[i+1].isdigit():
                i += 1
            else:
                break
        sides = int(formula[formula.index("D") + 1:i + 1])
    except IndexError:
        sides = int(formula[formula.index("D") + 1:i + 1])

    if "+" in formula or "-" in formula:
        result = 0
        for i in range(1, number_of_dices + 1):
            result += random.randint(1, sides)
        if "+" in formula:
            result += int(formula[formula.index("+")+1:])
        else:
            result -= int(formula[formula.index("-")+1:])
        return result

    result = 0
    for i in range(1, number_of_dices + 1):
        result += random.randint(1, sides)
    return result

print(roll_the_dice("12D7+1"))


















