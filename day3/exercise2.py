# BMI calculator exercise

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight/height** 2)

if BMI < 18.5:
    print("you are under weight")
elif BMI < 25:
    print('Normal weight')
    
elif BMI < 30:
    print('Overweight')
    
elif BMI < 35:
    print('Obese')
    
else:
    print("you are clinically obese")
    