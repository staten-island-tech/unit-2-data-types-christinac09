# accepts two arguments
# finds the greatest common factor of the two numbers
# uses EUCLIDEAN ALGORITHM

a = int(input("enter a number: "))
first = a

b = int(input("enter another number: "))
second = b

while b != 0:
    remainder = a%b
    a = b
    b = remainder
print(f"The greatest common factor of {first} and {second} is {a}")
