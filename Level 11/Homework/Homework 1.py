
# Work 1.

point = int(input("Enter your exam points: "))

if point > 90:
    print("Your assessment is A.")
elif point > 80 < 89:
    print("Your assessment is B.")  
elif point > 70 < 79:
    print("Your assessment is C.")   
elif point > 60 < 69:
    print("Your assessment is D.")       
elif point < 60:
    print("Your assessment is F.")     


# Work 2. 

age = int(input("Enter your age: "))

if age < 13:
    print("You are Child")
elif 14 < age > 20:
    print("You are Teenager")    
else:
    print("You are Adult") 

# Work 3.


number = int(input("Enter Number: "))

if number == 0:
    print("Number is 0")
elif number > 0:
    print("Number is Positive")
else:
    print("Number is Negative")


# Work 4. 


price = int(input("Enter price: "))

if price > 50:
    discount1 = price - 10
    print(price - discount1)
elif 20 < price < 50:
    discount2 = price - 5
    print(price - discount2)
else:
    print(price)   # No discount  

    


       


