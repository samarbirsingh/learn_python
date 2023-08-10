height = input("Enter your height:")
height=float(height)
weight = input("Enter your weight:")
weight=float(weight)
BMI= weight/height**2

if BMI >= 30:
    print("Obesity")
elif BMI > 25 and BMI < 29:
    print("Overweight")
elif BMI >18.5 and BMI <25:
    print("Normal")
elif BMI < 18.5:
    print("Underweight")
