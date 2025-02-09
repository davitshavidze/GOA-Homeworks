
# Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

def opposite(number):
    if number > 0:
        return -1 * number
    elif number < 0:
        return number - (number * 2)
    else:
        return 0