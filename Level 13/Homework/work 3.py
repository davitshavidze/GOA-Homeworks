



# Work 3.

# while ციკლისა და input-ის საშუალებით მომხარებელს შემოატანინეთ პაროლი სანამ არ იქნება ის "group55"-ის ტოლი.

correct_password = ("group55")

while True:

    guess = input("Enter Database Password: ")
    
    if guess == correct_password:
        print("In access Granted. Welcome!")
    else:
        print("In access Denied. Try again: ")