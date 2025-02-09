
# Python

# Create a variale:

# Python-ში ცვლადები გამოიყენება მონაცემების მნიშვნელობების შესანახად. თქვენ შეგიძლიათ წარმოიდგინოთ ისინი, როგორც კონტეინერები მონაცემების შესანახად. მნიშვნელობები შეიძლება შევინახოთ integer,string,boolean და float-ის სახით.

# If / else

# if/else განცხადება გამოიყენება პირობების შესამოწმებლად და ერთი კოდის ბლოკის შესრულებისთვის, თუ პირობა სწორია, და სხვა კოდის ბლოკის შესრულებისთვის, თუ პირობა მცდარია.


# mathematic operators:


result_add = 10 + 5
print("Addition:", result_add)  


result_subtract = 10 - 5
print("Subtraction:", result_subtract)  


result_multiply = 10 * 5
print("Multiplication:", result_multiply)  


result_divide = 10 / 5
print("Division:", result_divide) 


result_floor_divide = 10 // 3
print("Floor Division:", result_floor_divide)  


result_modulus = 10 % 3
print("Modulus:", result_modulus)  

result_exponent = 10 ** 2
print("Exponentiation:", result_exponent) 




temperature = 20

if temperature > 25:
    print("It's a warm day.")
elif temperature < 15:
    print("It's a cold day.")
else:
    print("It's a moderate day.")


# For Loop

# პითონში for ციკლი საშუალებას გვალევს გავიმეოროთ კოდი, რამდენჯერაც დაგვჭირდება ჩვენი ინტერესებიდან გამომდინარე. მაგალითად, თუ გვჭირდება გადავუაროთ ელემენტებს სიაში, შეგვიძლია გამოვიყენოთ for ციკლი თითოუელი ელემენტის ტერმინალში გამოტანისთვის.

# Example: 

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

# Or:

for i in range(5):
    print(i)



# While Loop:

# პითონში while ციკლი საშუალებას გვაძლევს განვახორციელოთ კოდი რამდენჯერაც გვჭირდება ჩვენივე ინტერესებიდან გამომდინარე, მანამ სანამ გარკვეული პირობა შესრულდება.

# Exaple:

count = 0

while count < 5:
    print(count)
    count += 1


# Lists

# პითონში სია (list) არის მონაცემთა სტრუქტურა, რომელიც შეიცავს ელემენტების თანმიმდევრობას. სიაში ელემენტები შეიძლება იყოს ნებისმიერი ტიპის მონაცემი, Strings,Integers,Booleans,Floats and ETC.

list = ["Hello",True,43,56.87]

# append(x) - სიას ემატება ახალი ელემენტი x.

# remove(x) - სიიდან იშლება ელემენტი x.

# pop([i]) - შლის და აბრუნებს ელემენტს ინდექსი i-დან. თუ i არ არის მითითებული, შლის და აბრუნებს ბოლო ელემენტს.

# reverse() - ალაგებს ელემენტებს უკუმიმართულებით.

# index(x) - აბრუნებს პირველი გამოჩენის ინდექსს ელემენტ x-სთვის.

# count(x) - ითვლის რამდენჯერ გამოჩნდა ელემენტი x სიაში.


# Functions 

# პითონში ფუნქციები არის კოდი, რომელიც შეიძლება გამოყენებული იქნეს მრავალჯერ, მის ფუნქციას შეასრულებს და შემდეგ დაბრუნდება. ის გამოიყენება პროგრამების გასამარტივებლად და კოდის გასაადვილებლად.

# Parameters (პარამეტრები) - ეს არის ცვლადები, რომლებიც განსაზღვრულნი არიან ფუნქციის სათაურში. ისინი ფუნქციას აძლევენ მათ მნიშვნელობებს.

# Arguments (არგუმენტები) - ეს არის რეალური მნიშვნელობები, რომლებიც გადაეცემა ფუნქციას გამოძახების დროს. ისინი ჩადგმულია პარამეტრებში.

def my_function():
    print("Hello from a function")

def multiply(x, y): # x და y არის პარამეტრები
    return x * y

result = multiply(3, 5) # 3 და 5 არის არგუმენტები
print(result)


# String Functions 

# len() - აბრუნებს სტრინგის სიგრძეს (სიმბოლოების რაოდენობას).

text = "Hello, world!"
length = len(text)
print(length)  # 13

# lower() - აბრუნებს სტრინგს პატარა ასოებით.

text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # "hello, world!"

# upper() - აბრუნებს სტრინგს დიდი ასოებით.

text = "Hello, World!"
upper_text = text.upper()
print(upper_text)  

# split() - ყოფს სტრინგს საზღვრებად და აბრუნებს სიას.

text = "Hello, World!"
split_text = text.split(", ")
print(split_text)  # ['Hello', 'World!']

# join() - აბრუნებს სტრინგს, რომელიც შედგენილია სიის ელემენტებისგან, გაერთიანებული არის გარკვეული სიმბოლოს ან სტრინგის მიხედვით.

words = ['Hello', 'World']
joined_text = " ".join(words)
print(joined_text)  # "Hello World"

# Capitalize() - გამოიყენება სტრინგის პირველი ასოს დიდი ასოდ გადაქცევისთვის, ხოლო დანარჩენი ასოები გადადის პატარა ასოებად.

text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # "Hello, world!"

# Replace() - სტრინგის ფუნქცია, რომელიც ცვლის სტრინგის ნაწილებს სხვა ნაწილებით

text = "I love apples"
new_text = text.replace("apples", "oranges")
print(new_text)  


# Format() - გამოიყენება სტრინგში ტექსტისა და მონაცემების ჩასაწერად. ის ქმნის სტრინგებს, რომელიც მოიცავს ცვლადების მნიშვნელობებს, რაც მეტად აღქმულ საშუალებას აძლევს კოდის წაკითხულობისთვის.

text = "My name is {} and I am {} years old.".format("John", 25)
print(text)  

# Or:

name = "Davit"

age = 15

print(f'hello {name} your are {age} old!')
