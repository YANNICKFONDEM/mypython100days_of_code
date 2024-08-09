# pizza order

print("wlcome to python pizza Deliveries!")
size = input("what size do you want? S, M, or L \n")
small_pizza = 1500
medium_pizza = 2000
large_pizza = 2500
extra_cheese = 500
pepperinoi = 500
add_pepperoni = small_pizza + pepperinoi
no_pepperinoi_and_cheese = small_pizza + extra_cheese
add_pepperoni_and_cheese = small_pizza + pepperinoi + extra_cheese

if size == 's':
    add_pepperoni = input("do you want pepperoni? Y or N \n")
    if add_pepperoni == 'y':
        cheese = input("do you need some extra chese? Y or N")
        if cheese == 'y':
            print(f"your pizza price is {add_pepperoni_and_cheese}cfa with pepperoni and some extra cheese. ")
        else:
            print(f"your pizza price is {add_pepperoni}cfa with pepperoni and no extra cheese. ")
    elif add_pepperoni =='n':
        cheese = input("do you need some extra chese? Y or N")
        if cheese == 'y':
            print(f"your pizza price is {no_pepperinoi_and_cheese}cfa without pepperoni and some extra cheese. ")
        
    else:
        print('your pizza is 1500cfa')
        
        
        
elif size == 'm':
    add_pepperoni = input("do you want to add pepperinio? Y or N \n")
    if add_pepperoni == 'y':
        add_pepperoni = medium_pizza + pepperinoi
        print(f"your pizza price is {add_pepperoni}cfa with pepperoni. ")
    else:
        print('your pizza is 2000cfa')
        
elif size == 'l':
    print(f"your pizza price is {large_pizza}cfa. ")