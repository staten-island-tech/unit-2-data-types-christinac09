#accepts a bill value
#offers a tip of 0%, 15%, 20% or 25% 
#based on whether service was "bad, okay, good, or great"

bill = float(input("enter bill value: "))
service = input("how was the service? bad, okay, good, or great")

if service == "bad":
    if input("tip 0%? yes or no") == "yes":
        tip = 0 * bill
    else: 
        percent = int(input("enter tip percentage: ")) / 100
        tip = percent * bill


if service == "okay":
    if input("tip 15%? yes or no") == "yes":
        tip = 0.15 * bill
    else: 
        percent = int(input("enter tip percentage: ")) / 100
        tip = percent * bill


if service == "good":
    if input("tip 20%? yes or no") == "yes":
        tip = 0.20 * bill
    else: 
        percent = int(input("enter tip percentage: ")) / 100
        tip = percent * bill


if service == "great":
    if input("tip 25%? yes or no") == "yes":
        tip = 0.25 * bill
    else: 
        percent = int(input("enter tip percentage: ")) / 100
        tip = percent * bill



total = bill + tip
print(f"your total is ${total}")