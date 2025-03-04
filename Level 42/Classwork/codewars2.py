
# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# solution 

def past(h, m, s):
    miliseconds = 0
    miliseconds += 3600000 * h
    miliseconds += 60000 * m
    miliseconds += 1000 * s
    return miliseconds
