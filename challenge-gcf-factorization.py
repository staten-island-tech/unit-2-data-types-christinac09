#find gcf of two numbers

a = int(input("enter a number: "))
b = int(input("enter another number: "))

a_factors = []
b_factors = []

for i in range(1,a+1):
    if a%(i) == 0:
        a_factors.append(i)

for i in range(1,b+1):
    if b%(i) == 0:
        b_factors.append(i)

print(a_factors)
print(b_factors)

factors = []

def check_factors(x,y):
    if(x == i and y == i):
        print("yes")
    else: 
        print("only 1 or 0 are 4")

for i in (a_factors):
    check_factors(a_factors,b_factors)

print(factors)
