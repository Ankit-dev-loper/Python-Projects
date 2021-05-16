print("|=======================================|")
print("| This calculator Is Made By Ankit singh|")
print("|=======================================|")

i = int(input("enter first number here=>>"))
print("For addition use + sing")
print("For multiplication use * sing")
print("For subtraction use - sing")
print("For Division use / sing")
n = input("setect operation=>>")
c = int(input("enter second number here=>>"))
r = "yes"
b = "no"
if n == ('*'):
    print(i,"X",c,"=",i*c,"[answer]")

if n == ('+'):
    print(i,"+",c,"=",i+c)

if n == ('-'):
    print(i,"-",c,"=",i-c)

if n == ('/'):
    print(i,"/",c,"=",i/c)

t = print("do you want use it again so type yes ")
g = input()
while g==("yes"):
    print("|=======================================|")
    print("| This calculator Is Made By Ankit singh|")
    print("|=======================================|")
    i = int(input("enter first number here=>>"))
    print("For addition use + sing")
    print("For multiplication use * sing")
    print("For subtraction use - sing")
    print("For Division use / sing")
    n = input("setect operation=>>")
    c = int(input("enter second number here=>>"))
    r = "yes"
    b = "no"
    if n == ('*'):
        print(i, "X", c, "=", i * c, "[answer]")

    if n == ('+'):
        print(i, "+", c, "=", i + c)

    if n == ('-'):
        print(i, "-", c, "=", i - c)

    if n == ('/'):
        print(i, "/", c, "=", i / c)

    t = print("do you want use it again so type yes ")
    g = input()
    i = i + 1
if g==("no"):
    print("Ok Thanks")