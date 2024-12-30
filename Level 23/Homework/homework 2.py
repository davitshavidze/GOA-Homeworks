

def simple_calculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        return num1 / num2
    else:
        return "შეცდომა: უცნობი ოპერაცია"

print(simple_calculator(10, 5, "დამატება"))  
print(simple_calculator(10, 5, "გამოკლება"))  
print(simple_calculator(10, 5, "გამრავლება"))  
print(simple_calculator(10, 5, "გაყოფა"))     
print(simple_calculator(10, 0, "გაყოფა"))     
print(simple_calculator(10, 5, "უცნობი"))     