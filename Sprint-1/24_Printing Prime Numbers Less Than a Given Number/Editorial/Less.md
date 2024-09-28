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

### Custom Logic Approach

1. Define a range of numbers.
2. For each number in the range, check if it is prime by testing divisibility against all integers up to the number itself.
3. If a number is prime, store it in a list.
4. Output the list of prime numbers.

### Sample Code (Custom Logic Approach)

```python
# Define the range
i = [10, 30]  
primes = []  # List to store prime numbers

print(f"Prime numbers between {i[0]} and {i[1]}:")

for num in range(i[0], i[1] + 1):
    if num < 2:  
        continue  # Skip numbers less than 2
    sam = "Yes" 
    for j in range(2, num):  
        if num != 2 and num % j == 0:  
            sam = "No" 
            break  
    if sam == "Yes":  
        primes.append(num)  # Add prime number to the list

print(primes)  # Output the list of prime numbers
```

## Time Complexity

- Approximately **O(n²)** due to the nested loops.

## Space Complexity

- **O(n)** for storing the list of prime numbers.
