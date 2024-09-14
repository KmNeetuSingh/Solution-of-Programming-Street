import math
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(lcm(12, 15))
print(lcm(12, 24))