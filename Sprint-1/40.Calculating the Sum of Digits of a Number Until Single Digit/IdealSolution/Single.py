def single(n):
    while n >= 10:  # Keep summing digits until the number is a single digit
        n = sum(int(digit) for digit in str(n))  # Sum the digits of the number
    print(n)

# Example usage
single(987569)
