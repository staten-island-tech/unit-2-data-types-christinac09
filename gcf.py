a = int(input("enter a number"))

b = int(input("enter another number"))

remainder = b

if b == 0:
    print(a)
else:
    remainder = a%b
    a = b
    b = remainder