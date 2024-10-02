def identifyPrime(n):
    a = "Prime"
    for i in range(2, n):
        if n != 2 and n % i == 0:
            a = "Not a Prime"
            break
    print(a)

# Example usage:
identifyPrime(4)  
