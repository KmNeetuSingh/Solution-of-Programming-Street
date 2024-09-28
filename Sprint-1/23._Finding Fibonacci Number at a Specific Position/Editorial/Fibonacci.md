# Finding the Fibonacci Number at a Specific Position

**Difficulty**: Easy  
**Topics**: Basic Programming, Sequences

## Problem Description

Write a program to find the Fibonacci number at a specific position in the Fibonacci sequence.

## Input

- An integer `position` representing the position in the Fibonacci sequence (1-indexed).

## Output

- An integer representing the Fibonacci number at the specified position.

## Example

**Input:**  
`position = 5`

**Output:**  
`5`

**Explanation:**  
The Fibonacci sequence starts with:  
`0, 1, 1, 2, 3, 5, 8, ...`  
At position 5 (1-indexed), the Fibonacci number is `5`.

## Constraints

- The position will be a positive integer (i.e., `position >= 1`).

## Approach

### Iterative Approach

1. Initialize the first two Fibonacci numbers.
2. Use a loop to calculate Fibonacci numbers until the specified position is reached.
3. Print the Fibonacci number at the given position.

### Sample Code (Iterative Approach)

```python
position = 5  # Specify the position in the Fibonacci sequence

# First two Fibonacci numbers
n1, n2 = 0, 1

# Handle the case for the first position
if position == 1:
    fibonacci_number = n1
else:
    # Calculate Fibonacci number at the specified position
    for _ in range(2, position + 1):
        nth = n1 + n2  # Next term is the sum of the previous two terms
        n1 = n2  # Update n1
        n2 = nth  # Update n2
    fibonacci_number = n2

print(f"The Fibonacci number at position {position} is: {fibonacci_number}")  # Output: 5
```

### Alternative Approach: Using Recursion

You can also solve the problem using recursion. However, note that this approach may be inefficient for large positions due to repeated calculations.

#### Recursive Sample Code

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

position = 5  # Specify the position in the Fibonacci sequence
fibonacci_number = fibonacci_recursive(position - 1)  # Adjust for 0-indexing

print(f"The Fibonacci number at position {position} is: {fibonacci_number}")  # Output: 5
```

## Time Complexity

- **Iterative Approach**: **O(n)**, where `n` is the specified position.
- **Recursive Approach**: **O(2^n)**, due to repeated calculations of Fibonacci numbers.

## Space Complexity

- **Iterative Approach**: **O(1)** since only a constant amount of space is used.
- **Recursive Approach**: **O(n)** due to the recursion stack.

