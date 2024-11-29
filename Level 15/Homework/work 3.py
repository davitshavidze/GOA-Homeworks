


year = int(input("Enter your year: "))

# ნაკიანობის შემოწმება
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is Nakiani")
else:
    print ("Year isnt Nakiani")