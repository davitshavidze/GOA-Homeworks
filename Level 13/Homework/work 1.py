

# Work 1. 

# შექმნით რიცხვის გამოცნობის თამაში while ციკლით, რომელიც მომხმარებელს შეეკითხება რიცხვს 1-დან 10-მდე, სანამ მომხმარებელი არ შეიყვანს თქვენთვის სასურველ რიცხვს

correct_number = 7

while True:

    guess = int(input("Enter number from 0 - 10: "))
    
    if guess == correct_number:
        print("Congrats, Answer is Correct!")
    else:
        print("Incorrect! Try Again. ")
