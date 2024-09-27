num = 28 
if num <= 0:
    print(f"{num} is not a Perfect Number")
else:
    sumD = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sumD+= i
    
    if sumD == num:
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")
