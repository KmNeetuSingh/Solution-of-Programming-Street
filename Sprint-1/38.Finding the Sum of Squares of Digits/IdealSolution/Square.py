def squarenum(n):
    n = abs (n)
    print (sum(int(digit) ** 2 for digit in str(n)))
squarenum(3)