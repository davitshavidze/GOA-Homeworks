
# Write a function that will check if two given characters are the same case.

# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0

# Solution:

def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        
        if (a.istitle() and b.istitle()) or (a.islower() and b.islower()):           
            return 1
        else:
            return 0
    else:
        return -1