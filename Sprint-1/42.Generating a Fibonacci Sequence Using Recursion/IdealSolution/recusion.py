def fibonacci(n):
    # Base case: return n for 0 and 1
    if n <= 1:
        return n
    # Recursive case: sum of previous two numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

def sequence(limit):
    # Generate Fibonacci sequence up to the given limit
    seq = []
    for i in range(limit):
        seq.append(fibonacci(i))
    print(seq)

# Example usage
sequence(6) # Output: [0, 1, 1, 2, 3, 5]
