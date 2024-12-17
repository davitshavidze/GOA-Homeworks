

# Work 1

# What is the output of this code:

# nums = [1,2,3,4,5,6] -- > [6,5, 4, 3,2,1]

# res = nums[::-1]

# print(res[2])

# ამ შემთხვევაში, თავდაპირველად მოცემული გვაქვს სიის შემდეგ შექმნილი ახალი ცვლადი, რომელშიც გამოყენებულია List slicing - ი, ამ კონკრეტულ შემთხვევაში კი მოცემული გვაქვს ქმედებები, რომლის შემდეგადაც სია შეიცვლის დაწყების თანმიმდევრობას და დაიწებს ათვლას ბოლოდან, ანუ იზამსე Revers - ს, შემდეგ კი ახალ სიაში იპოვის 2 ინდექსად მდგარ მნიშვნელობას და გამოიტანს მას.

# answer = 4

nums = [1,2,3,4,5,6]
res = nums[::-1]
print(res[2])



# work 2

# write a program that takes a string as input and outputs the last character of that string

word = input("Enter word: ")

print(word[::-100])

# გამოიტანს სტრინგში მოცემულ ბოლო ასოს "o"-ს



# work 3.

# How many elements will this slice return if the "names" list contains t items?


# (names[1:-1])

# ეს კოდი გამოიტანს მნიშვნელობებს ინდექსად 2,3,4, ჯერ სიასი შემოატრიალებს და შემდეგ მიუჰყვება მას 1 ინდექსამდე ანუ:

# მაგალითად:

names = ["David" , "Nikita" , "Gio" , "Vlado" , "Nika"]

print(names[1:-1])

# გამოიტანს ვლადოს,გიოს და ნიკიტას




# work 4

squares = [ "Dato" , "Mari" , 5 , 5.9 , True , "Nikolozi" , False , 6.79 , "Tamuna" , 6 ] 

print(squares[5:10:1])
