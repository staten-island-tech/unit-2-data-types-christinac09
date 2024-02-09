#accepts a bill value
#offers a tip of 0%, 15%, 20% or 25% 
#based on whether service was "bad, okay, good, or great"

bill = float(input("enter bill value: "))
service = input("how was the service? bad, okay, good, or great: ")

if service == "bad":
    tip = 0
elif service == "okay":
    tip = 0.15
elif service == "good":
    tip = 0.20
elif service == "great":
    tip = 0.25



if input(f"tip {100 * tip}%? yes or no: ") == "yes":
    total = tip * bill + bill
else: 
    percent = int(input("enter tip percentage (exclude percent sign): ")) / 100
    total = percent * bill + bill


print(f"your total is ${total}")