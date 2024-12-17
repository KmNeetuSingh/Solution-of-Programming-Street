def idenitfy_prime_numbers(Num):
    a = "Prime number"
    for i in range (2, Num):
          if Num !=2 and Num % i == 0 :
               a = "Not a Prime Numbers"
               break
    print(a)

    #Example usage...
idenitfy_prime_numbers(2)
idenitfy_prime_numbers(6)