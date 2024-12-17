

number1 = int(input("Enter number #1: "))
number2 = int(input("Enter number #2 : "))
number3 = int(input("Enter number #3 : "))
number4 = int(input("Enter number #4 : "))
number5 = int(input("Enter number #5 : "))

list = []

list += [number1]
list += [number2]
list += [number3]
list += [number4]
list += [number5]

print("Yout entered numbers list is: " + str(list))

search_number = int(5)

if search_number in list:
    print(str(search_number) + " is in list")
else:
    print("There is no number in list you entered.")

