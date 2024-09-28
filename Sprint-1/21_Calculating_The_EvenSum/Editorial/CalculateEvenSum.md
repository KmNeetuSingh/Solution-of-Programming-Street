# Calculating the Sum of Even Numbers in a Range

**Difficulty**: Easy  
**Topics**: Basic Programming, Mathematical Computations

## Problem Description

Write a program to find the sum of all even numbers within a given range.

## Input

- A list of two integers representing the range, `range = [start, end]`.

## Output

- An integer representing the sum of all even numbers within the range (inclusive).

## Example

**Input:**  
`range = [1, 10]`

**Output:**  
`30`

**Explanation:**  
The sum of even numbers between 1 and 10 is:  
`2 + 4 + 6 + 8 + 10 = 30`

## Constraints

- The range will consist of two integers, where `start <= end`.
- Both integers will be non-negative.

## Approach

1. Iterate through all numbers in the given range.
2. Check if each number is even by using the modulus operator (`num % 2 == 0`).
3. Sum the even numbers and return the total.

## Sample Code (Python)

```python
def sum_of_even_numbers_in_range(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

# Example usage
range_start = 1
range_end = 10
result = sum_of_even_numbers_in_range(range_start, range_end)
print(result)  # Output: 30
```

## Time Complexity

- The time complexity of this solution is **O(n)** where `n` is the number of integers in the range `[start, end]`.

## Space Complexity

- The space complexity is **O(1)** since only a few variables are used regardless of the input size.