#temperature

temp = int(input("enter a temp in degrees fahrenheit: "))
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')