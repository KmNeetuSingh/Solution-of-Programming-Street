# Sum of Odd Numbers in a Range

**Difficulty**: Easy  
**Topics**: Basic Programming, Mathematical Computations

## Problem Description

Write a program to calculate the sum of all odd numbers within a given range.

## Input

- Two integers, representing the start and end of the range (inclusive).

## Output

- An integer representing the sum of all odd numbers within the given range.

## Example

**Input:**  
`start = 1`  
`end = 10`

**Output:**  
`25`

**Explanation:**  
The sum of odd numbers between 1 and 10 is:  
`1 + 3 + 5 + 7 + 9 = 25`

## Constraints

- The start and end values will be non-negative integers.
- `start <= end`.

## Approach

1. Iterate through all numbers in the given range `[start, end]`.
2. Check if each number is odd by using the modulus operator (`num % 2 != 0`).
3. Add each odd number to the total sum.
4. Print the total sum after the loop completes.

## Sample Code (Python)

```python
start = 1
end = 10
total_sum = 0  # Variable to store the sum of odd numbers

for num in range(start, end + 1):
    if num % 2 != 0:  # Check if the number is odd
        total_sum += num  # Add the odd number to the sum

print(total_sum)  # Output: 25
```

## Time Complexity

- The time complexity is **O(n)**, where `n` is the number of integers in the range `[start, end]`.

## Space Complexity

- The space complexity is **O(1)** since only a constant amount of space is used.