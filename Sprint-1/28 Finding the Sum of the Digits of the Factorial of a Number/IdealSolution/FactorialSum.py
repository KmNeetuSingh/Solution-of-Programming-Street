def solve(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    sum = 0
    while fact > 0:
        sum += fact % 10  
        fact //= 10  

    print(sum)
solve(4)