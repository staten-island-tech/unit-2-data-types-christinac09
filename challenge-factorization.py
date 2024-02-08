# accepts an input
# determines all factors of the number

n = int(input("enter a whole number: "))

# for range i = 0 to n
# n%i
# if n%i == 0, then save i
# else exclude i
# put all the i's in a list
# print the list

factors = []

for i in range(1,n):
    if n%(i) == 0:
        factors.append(i)

print(factors)