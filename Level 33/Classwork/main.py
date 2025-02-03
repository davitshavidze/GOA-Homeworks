
# Work 1.

# მომხმარებელს შემოვატანინეთ სიტყვა, მნიშვნელობა. დავალებაში იყო მოცემული რომ მომხმარებელს ჰქონდა დაზიანებული კლავიატურა ანუ Keyboard-ი და სიტყვების ნაცვლად წერდა # ნიშანს. ამის გამოსასწორებლად გვთხოვეს რომ სტრინმგის ერთ-ერთი ფუნქციით შემოტანილი არასწორი მნიშვნელობა შეგვეცვალა space-ით რაც გავაკეთეთ ქვემოთ მოცემულ კოდში. 

msg = input("Enter word: ")

print(msg.replace("#", " "))



# Work 2.

user = input("Enter your name: ")

age = input("Enter your age: ")

text = "Hello, {fuser}! You are {fage} years old." .format(fuser = user, fage = age)

print(text)

print(f"Hello, {user}! You are {age} years old.")



# Work 3.

list =  ["Python", "is", "fun"]

sep_list = " " .join(list)

print(sep_list)


# Work 4.


sentence = input("Enter sentence: ")

word = sentence.split()

print(word)


# Work 5.

sentence2 = input("Enter a sentence: ")

wordreplace = input("Enter word to replace: ")

newword = input("Enter new word: ")

modified = sentence2.replace(wordreplace, newword)

print(modified)