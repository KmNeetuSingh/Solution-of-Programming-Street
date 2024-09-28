i = [10, 30]  
primes = [] 
for num in range(i[0], i[1] + 1):
    if num < 2:  
        continue  
    sam = "Yes" 
    for j in range(2, num):  
        if num != 2 and num % j == 0:  
            sam = "No" 
            break  
    if sam == "Yes":  
        primes.append(num) 
print(primes) 