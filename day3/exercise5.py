# A love calculator

print("welcome to the love calculator!")

name1 = input("what is your name?\n")
name2 = input("what is their name? \n")

bothNames = name1 + name2
lowercase_ofBothnames = bothNames.lower()

t = lowercase_ofBothnames.count('t')
r = lowercase_ofBothnames.count('r')
u = lowercase_ofBothnames.count('u')
e = lowercase_ofBothnames.count('e')

true = t+r+u+e 


l = lowercase_ofBothnames.count('l')
o = lowercase_ofBothnames.count('o')
v = lowercase_ofBothnames.count('v')
e = lowercase_ofBothnames.count('e')

love = l+o+v+e

love_score = int(str(true)+ str(love)
)

if love_score < 10 or love_score > 15:
    print(f'your love score is {love_score} you go together like coke and mentor')
elif love_score >= 16 and love_score <=20:
    print(f'your love score is {love_score} you are alright together')
else:
    print(f'your score is {love_score}')

