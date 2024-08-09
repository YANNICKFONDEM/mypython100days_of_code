import math
print("(1)Addition: + \t",end="------------------------")
print("(2)Subtraction: -  \t",end="--------------------")
print("(3)Multiplication: * \t",end="----------------")
print("(4)Division: / \n")
print("(5)Modules: % \t",end="------------------------")
print("(6)Unit conversion: length, mass, temperature \n")
print("(7)Sin function:   \t",end="---------------")
print("(8)cos function:   \t",end="----------------")
print("(9)Tan function:   \t",end="---------------------")
print("(10)Exponential function:   \t")
print("(11)Square root:   \t",)
opp = int(input("Sellect an operator above:\n"))

if opp == 1:
    num1 = int(input("Enter first number below:\n"))
    num2 = int(input("Enter second number below:\n"))
    total = num1 + num2
    print("the sum of ",num1, "and", num2, "is:",total )
elif opp == 2:
    num1 = int(input("Enter first number below:\n"))
    num2 = int(input("Enter second number below:\n"))
    total = num1 - num2
    print("the subtraction of ",num1, "and", num2, "is:",total )
elif opp == 3:
    num1 = int(input("Enter first number below:\n"))
    num2 = int(input("Enter second number below:\n"))
    total = num1 * num2
    print("the Multiplication of ",num1, "and", num2, "is:",total )
elif opp == 4:
    num1 = int(input("Enter first number below:\n"))
    num2 = int(input("Enter second number below:\n"))
    total = num1 / num2
    print("the Division of ",num1, "and", num2, "is:",total )
    
    # Mathematical functions
    
elif opp == 7:
    num = int(input("Enter a number below to fine the sine:\n"))
    total = (math.sin(num))
    print("the sine of ",num, "is:",total )
elif opp == 8:
    num = int(input("Enter a number below to fine the cos:\n"))
    total = (math.cos(num))
    print("the cos of ",num, "is:",total )
elif opp == 9:
    num = int(input("Enter a number below to fine the tan:\n"))
    total = (math.tan(num))
    print("the tangent of ",num, "is:",total )
elif opp == 10:
    num = int(input("Enter a number below to fine the sine:\n"))
    total = (math.exp(num))
    print("the exponential of ",num, "is:",total )
elif opp == 11:
    num = int(input("Enter a number below to fine the sine:\n"))
    total = (math.sqrt(num))
    print("the square root of ",num, "is:",total )
    
elif opp == 5:
    num1 = int(input("Enter first number below:\n"))
    num2 = int(input("Enter second number below:\n"))
    total = num1 % num2
    print("the remainder of ",num1, "divided by", num2, "is:",total ,"***This is an additional module***" )
    
    
# Units conversion and percentage calculation
    
elif opp == 6:
    print("############ Unit conversion ###################")
    print("1: Length")
    print("2: Mass")
    print("3:Temperature")
    conversion = int(input("what do you want to convert from the list above: \n"))
    if conversion == 1:
        choice = input("(a)Length (m - cm)\n(b)Length (cm - m)")
        if choice == "a":
        
            num = int(input("Enter the number below in metter(m):\n"))
            conv = num * 100
            print("the number ",num, "converted from m - cm is:",conv, "cm" )
        elif choice == "b":
            num = int(input("Enter the number below in centimetter(cm):\n"))
            conv = num / 100
            print("the number ",num, "converted from cm - m is:",conv, "m" )
        else:
            print("Invalid operation")
    elif conversion == 2:
        choice = input("(a)Mass (G - Kg)\n(b)Length (Kg -G)")
        if choice == "a":
            num = int(input("Enter the number below in gram(G):\n"))
            conv = num * 1000
            print("the number ",num, "converted from G - kG is:",conv, "Kg" )
        elif choice == "b":
            num = int(input("Enter the number below in gram(Kg):\n"))
            conv = num / 1000
            print("the number ",num, "converted from Kg - G is:",conv, "G" )
        else:
            print("Invalid operation")
    elif conversion == 3:
        choice = input("(a)Temperature (K - degree)\n(b)Temperature (Degree - K)")
        if choice == "a":
        
            num = int(input("Enter the number below in kelvin(Kj):\n"))
            conv = num + 127
            print("the number ",num, "converted from K - degree is:",conv, "dg" )
        elif choice == "b":
            num = int(input("Enter the number below in Degee(dg):\n"))
            conv = num - 127
            print("the number ",num, "converted from degree - kelvin is:",conv, "Kj" )
        else:
            print("Invalid operation")
            
else:
    print("Invalid operation")
        
