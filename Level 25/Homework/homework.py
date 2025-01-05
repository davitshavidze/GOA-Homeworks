
correct = 78
attempts = 3


while attempts > 0:
        number = int(input("Enter chosen Number from 1-100: "))
        if number == correct:
                print("Correct! You guess the number!")
                break
        elif number > correct:
            print("Too high! Try again!")
        else:
            print("Too low! Try again! ")

        attempts -= 1  

while attempts == 0:
      print("Game over! You have 0 Attempts!")
      attempts -= 3
      
