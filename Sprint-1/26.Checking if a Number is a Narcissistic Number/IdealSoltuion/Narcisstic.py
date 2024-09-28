number = 15
r = str(number)
s= 0  
for digit in r:
    s += int(digit) ** len(r)
if  s == number:
    print("Narcissistic Number")
else:
    print("Not a Narcissistic Number")
