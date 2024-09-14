def limit_Iterative(n):
    a, b = 0, 1
    result = []
    while a<= n:
        result.append(a)
        a, b = b, a + b
    return result

# Example Usage
n = 10 #limit...
print(limit_Iterative(n))  

