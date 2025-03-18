
# 1) In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

# More examples in the test cases.

# Good luck!

# Solution:

def repeats(arr):
    one_sum = []
    for i in arr:
        if arr.count(i) == 1:
            one_sum.append(i)
    return sum(one_sum)


# Codewars 2) Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

# Solution: 

def litres(time):
    return time // 2


# Codewars 3) You will be given a string featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'. The string will start with the cat, and end with the mouse.

# You need to find out if the cat can catch the mouse from its current position. The cat can jump over at most three characters. So:

# "C.....m" returns "Escaped!" <-- more than three characters between

# "C...m" returns "Caught!" <-- as there are three characters between the two, the cat can jump.

# Solution: 

def cat_mouse(x):
    n = x.count(".")
    if n <= 3:
        return ("Caught!")
    if n > 3:
        return ("Escaped!")

