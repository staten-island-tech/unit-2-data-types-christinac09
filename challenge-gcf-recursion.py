#find gcf of two numbers

a = int(input("enter a number: "))
b = int(input("enter another number: "))

def gcf(a,b):
    if b == 0:
        return a
    else: 
        return gcf(b,a%b)
    
print("The greatest common factor is ", gcf(a,b))