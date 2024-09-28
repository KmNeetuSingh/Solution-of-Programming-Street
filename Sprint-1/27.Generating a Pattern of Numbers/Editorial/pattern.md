# Generating a Sequential Number Pattern

**Difficulty**: Easy  
**Topics**: Basic Programming, Patterns

## Problem Description

Write a program to generate a pattern of numbers where each row contains sequentially increasing numbers.

## Input

- An integer `n` that defines the number of rows in the pattern.

## Output

- A pattern of numbers where each row contains increasing numbers.

## Example

**Input:**  
`n = 3`

**Output:**
```
1 
2 3 
4 5 6 
```

**Explanation:**  
The program generates a pattern with 3 rows, where numbers are printed sequentially across the rows.

## Approach

1. **Initialize** a variable `count` to `1` to keep track of the current number to be printed.
2. **Loop through** each row from `1` to `n`:
   - For each row, use a nested loop that runs from `1` to the current row number `i`.
   - Print the current value of `count`, then increment `count`.
3. **Print** a newline after finishing each row.

### Sample Code

```python
def solve(n):
    count = 1  
    for i in range(1, n + 1):
        for j in range(1, i + 1): 
            print(count, end=" ")  
            count += 1 
        print()  

solve(3)
```

## Complexity

- **Time Complexity**: O(n²), where `n` is the number of rows, as the inner loop runs `i` times for each row.
- **Space Complexity**: O(1), as no additional data structures are used that grow with input size.