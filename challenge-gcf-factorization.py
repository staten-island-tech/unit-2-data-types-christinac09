# accepts two arguments
# finds the greatest common factor of the two numbers
# uses EUCLIDEAN ALGORITHM

a = int(input("enter a number: "))
b = int(input("enter another number: "))

a_factors = []
b_factors = []

for i in range(1,a):
    if a%i == 0:
        a_factors.append(i)

print(f"factors of a: {a_factors}")
      
for i in range(1,b):
    if b%i == 0:
        b_factors.append(i)
print(f"factors of b: {b_factors}")

