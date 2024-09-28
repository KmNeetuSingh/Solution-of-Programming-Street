position = 7
n1, n2 = 0, 1  
count = 1  
if position <= 0:
    print("Enter a positive integer.")
elif position == 1:
    print(n1)
else:
    while count < position:
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1
    print(n2)  
