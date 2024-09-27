# Checking for Perfect Numbers

## Difficulty: Easy

### Topics: Basic Programming, Number Theory

### Problem Description
A **perfect number** is a positive integer equal to the sum of its proper divisors (excluding itself). This program checks if a given number is perfect.

### Example
- **Input**: `num = 28`
- **Output**: `28 is a Perfect Number`
- **Explanation**: The divisors of 28 are 1, 2, 4, 7, 14. Their sum is `28`, making it a perfect number.

### Steps to Solve
1. **Input Validation**: Ensure the number is positive.
2. **Finding Divisors**: Loop through `1` to `num // 2` to find divisors.
3. **Sum the Divisors**: Accumulate the divisors.
4. **Check for Perfection**: Compare the sum to the original number.

### Code Implementation

```python
num = 28  # Change this number to check other cases

if num <= 0:
    print(f"{num} is not a Perfect Number")
else:
    sumD = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sumD += i
    
    if sumD == num:
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")
```

### Time Complexity
- **O(n/2)**: Iterates through half of the number.

### Space Complexity
- **O(1)**: Uses a constant amount of space.

### Additional Notes
- Known perfect numbers include 6, 28, 496, and 8128.

### Key Concepts
- Proper divisors
- Sum of divisors
- Basic loops and conditionals
