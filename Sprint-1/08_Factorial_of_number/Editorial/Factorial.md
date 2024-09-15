# Factorial of a Number  
## Difficulty: Easy

### Prerequisite: Basic Understanding of Loops

---

### Hint

The factorial of \( n \) is the product of all numbers from 1 to \( n \). For \( n = 0 \), the result is 1.

### Short Observations

- **Formula:** \( n! = n \times (n-1) \times ... \times 1 \).
- **Base Case:** \( 0! = 1 \).

### Detailed Observations

1. **Product Rule:** Multiply each integer from 1 to \( n \).
2. **Iterative Approach:** Loop from 1 to \( n \) and accumulate the result.
3. **Recursive Approach:** Factorial can also be calculated recursively.

### Pseudo Code

#### Iterative Approach
```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

#### Recursive Approach
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Example

**Input:** `n = 5`

1. **Iterative Approach:**
   - Start with result = 1.
   - Multiply by 1: result = 1.
   - Multiply by 2: result = 2.
   - Multiply by 3: result = 6.
   - Multiply by 4: result = 24.
   - Multiply by 5: result = 120.

**Output:**  
```text
120
```

**Recursive Approach:**
1. **Base Case:** \( n = 0 \) → return 1.
2. **Recursive Calls:**
   - \( 5! = 5 \times 4! \)
   - \( 4! = 4 \times 3! \)
   - \( 3! = 3 \times 2! \)
   - \( 2! = 2 \times 1! \)
   - \( 1! = 1 \times 0! \)
   - \( 0! = 1 \)

**Output:**  
```text
120
```

### Time Complexity

- **O(n)** - Linear time complexity.

### Space Complexity

- **Iterative:** O(1) - Constant space.
- **Recursive:** O(n) - Space for recursion stack.

### Alternate Solution

- **Dynamic Programming/Memoization:** Store results of subproblems to avoid redundant calculations in the recursive approach. Explore this approach further as it can optimize the recursive solution.