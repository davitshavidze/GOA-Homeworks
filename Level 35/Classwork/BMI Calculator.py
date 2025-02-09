
# BMI Calculator

def calculate_bmi(weight, height):
    bmi = (weight / (height ** 2))
    print(bmi)

    if bmi < 18.5:
        print("BMI Is Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("BMI Is Normal")
    elif bmi >= 25 and bmi <30:
        print("BMI Is overweight")
    else:
        print("obecity")


calculate_bmi(23,1.8)
calculate_bmi(25,2.1)
