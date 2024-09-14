# Fibonacci Series ......
## Difficulty: Easy

### Prerequisite: Basic Understanding of Sequences

---

### Hint

The Fibonacci series starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The series looks like: 0, 1, 1, 2, 3, 5, 8, 13, ...

### Short Observations

- **Generation Rule:** Each number is the sum of the two previous numbers.
- **Starting Points:** Begin with 0 and 1.

### Detailed Observations

1. **Start:** The series starts with 0 and 1.
2. **Recursive Rule:** Each number \( F_n = F_{n-1} + F_{n-2} \).
3. **Growth:** The series grows exponentially and approaches \( \phi^n / \sqrt{5} \), where \( \phi \) (phi) is the golden ratio (approx. 1.618).
4. **Generation Methods:** Can be generated iteratively or recursively.

### Pseudo Code

#### Iterative Approach
```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

#### Recursive Approach
```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci(n-1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs
```

### Example

**Input:** `n = 6`

1. **Sequence:** 0, 1, 1, 2, 3, 5.
2. **Iterative Generation:** 
   - Start with 0 and 1.
   - Generate next numbers: 1, 2, 3, 5.

**Output:**
```text
0, 1, 1, 2, 3, 5
```

### Time Complexity

`O(n)` - Linear time complexity as each term is computed once.

### Space Complexity

- **Iterative Approach:** `O(n)` - Space for storing the sequence.
- **Recursive Approach:** `O(n)` - Space for recursion stack and sequence storage.

### Alternate Solution

For large \( n \), use matrix exponentiation or Binet's formula for efficient computation.You can explore by yourself......
