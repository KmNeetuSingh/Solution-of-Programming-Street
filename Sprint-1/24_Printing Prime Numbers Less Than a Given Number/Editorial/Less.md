# Printing Prime Numbers Less Than a Given Number

**Difficulty**: Easy  
**Topics**: Basic Programming, Number Theory

## Problem Description

Write a program to print all prime numbers less than a specified number.

## Input

- An integer `number`, which serves as the upper limit for finding prime numbers.

## Output

- A list of prime numbers less than the specified number.

## Example

**Input:**  
`number = 20`

**Output:**  
`2, 3, 5, 7, 11, 13, 17, 19`

**Explanation:**  
The prime numbers less than 20 are: `2, 3, 5, 7, 11, 13, 17, and 19`.

## Constraints

- The input number will be a positive integer (i.e., `number > 1`).

## Approach

### Basic Approach

1. Iterate through all numbers from `2` to `number - 1`.
2. For each number, check if it is prime by testing divisibility against all integers up to its square root.
3. If a number is prime, print or store it in a list.
4. Output the list of prime numbers.

### Sample Code (Basic Approach)

```python
number = 20  # Specify the upper limit

print(f"Prime numbers less than {number}:")
for num in range(2, number):
    is_prime = True  # Assume num is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  # num is not prime
            break
    if is_prime:
        print(num, end=", " if num < number - 1 else "\n")  # Print with commas
```

### Alternative Approach: Sieve of Eratosthenes

An efficient algorithm to find all prime numbers up to a specified limit is the Sieve of Eratosthenes. This method is particularly efficient for generating a list of primes.Explore by own.
## Time Complexity

- **Basic Approach**: Approximately **O(n√n)**, where `n` is the specified number.
- **Sieve of Eratosthenes**: **O(n log(log(n)))**, making it more efficient for larger values.

## Space Complexity

- **Basic Approach**: **O(1)**, as only a few variables are used regardless of input size.
- **Sieve of Eratosthenes**: **O(n)**, for storing the boolean array.
