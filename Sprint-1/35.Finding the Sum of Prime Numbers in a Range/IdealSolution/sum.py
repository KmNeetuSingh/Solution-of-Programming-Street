def sum_of_primes_in_range(r):
    prime_sum = 0

    for n in range(r[0], r[1] + 1):
        if n < 2:  
            continue
        is_prime = True 

        for i in range(2, n):
            if n != 2 and n % i == 0:  
                is_prime = False
                break

        if is_prime: 
            prime_sum += n

    print (prime_sum)

# Example usage
sum_of_primes_in_range([1,10])
