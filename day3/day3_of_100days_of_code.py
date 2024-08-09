
# practice

print('welcome to the rollercoaster!')
height = int(input("what is your height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("pay 5000")
    elif age <= 18:
        print("pay 7000")
    else:
        print("pay 12000")
else:
    print("sorry, you have to grow taller before you can ride.")
    