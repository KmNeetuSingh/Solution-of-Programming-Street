def solve(n):
    for i in range(n):
        num = 1 
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)  
        print()  

# Example usage
solve(4)
