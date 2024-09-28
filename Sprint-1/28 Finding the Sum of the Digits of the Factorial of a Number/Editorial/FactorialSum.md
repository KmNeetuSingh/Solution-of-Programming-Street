# Finding the Sum of the Digits of the Factorial of a Number

**Difficulty**: Easy  
**Topics**: Basic Programming, Mathematical Computations

## Problem Description

Write a program to calculate the sum of the digits of the factorial of a given number.

## Input

- An integer `num` for which the factorial and its digit sum are to be computed.

## Output

- An integer representing the sum of the digits of the factorial of the specified number.

## Example

**Input:**  
`num = 4`

**Output:**  
`6`

**Explanation:**  
The factorial of `4` is `24`, and the sum of the digits is `2 + 4 = 6`.

## Approach

1. **Calculate the Factorial**:
   - Use a loop to compute the factorial of the input number `num`.
2. **Sum the Digits**:
   - Use a `while` loop to extract each digit from the factorial and sum them.

### Sample Code

```python
def solve(num):
    fact = 1  
    for i in range(1, num + 1):  
        fact *= i
    sum = 0  
    while fact > 0:  
        sum += fact % 10  
        fact //= 10  

    print(sum) 

# Example usage
solve(4)
```

## Complexity

- **Time Complexity**: O(n), where `n` is the input number, due to the factorial calculation and summing the digits.
- **Space Complexity**: O(1), as only a fixed amount of space is used regardless of input size.
 ## Alternative Approached
 # you can use the recursive method by you own if you find it easy the go for it.Keep coding