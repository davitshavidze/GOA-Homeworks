
# Work 1.

user = input("Enter your name: ")

age = input("Enter your age: ")

text = "Hello, {fuser}! You are {fage} years old." .format(fuser = user, fage = age)

print(text)

print(f"Hello, {user}! You are {age} years old.")



# Work 2.

list =  ["Python", "is", "fun"]

sep_list = " " .join(list)

print(sep_list)


# Work 3.


sentence = input("Enter sentence: ")

word = sentence.split()

print(word)


# Work 4.

sentence2 = input("Enter a sentence: ")

wordreplace = input("Enter word to replace: ")

newword = input("Enter new word: ")

modified = sentence2.replace(wordreplace, newword)

print(modified)


# Work 5.

array = "HeLLo WoRLd"

lower_array = array.lower()

print(lower_array)


# Work 6.

main = "hello world"

upper_main = main.upper()

print(upper_main)