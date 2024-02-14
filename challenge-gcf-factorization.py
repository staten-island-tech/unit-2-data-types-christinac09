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

print(f"factors of a: {a_factors}")
print(f"factors of b: {b_factors}")

factors = []

def check_factors(x,y):
    if (i in x) and (i in y):
        print("yes common factor")
        factors.append(i)
    else: 
        print("not common factor")

for i in (a_factors):
    check_factors(a_factors,b_factors)

print(f"all common factors of {a} and {b} are {factors}")
print(f"Greatest common factor is {factors[-1]}")