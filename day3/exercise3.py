# checking if a year is a leap year

year = int(input("Which year would you want to ckeck?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print('leap year')
else:
    print("Not leap year")