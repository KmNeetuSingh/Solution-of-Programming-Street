def find_div(num):
    div= []
    
    for i in range(1, num + 1): 
        if num % i == 0:  
            div.append(i)
    
    print(div)
# Example usage
find_div(20)
 # Output: Divisors: [1, 2, 3, 4, 6, 12]
