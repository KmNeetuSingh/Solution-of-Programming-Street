## Finding the Greatest Common Divisor (GCD)
### Difficulty: Easy

### Prerequisite: Basic Understanding of Division

### Hint

The GCD of two numbers `a` and `b` is the largest number that divides both `a` and `b` without leaving a remainder.

### Short Explanation

- Use the **Euclidean algorithm** to compute the GCD, which repeatedly replaces the larger number with its remainder when divided by the smaller number until the remainder is zero.

### Detailed Explanation

- **Definition:** The GCD of two numbers `a` and `b` is the largest number that divides both without a remainder.
- **Method:**
  - **Iterative Approach (Euclidean Algorithm):** Continuously divide `a` by `b` and assign the remainder to `a` until the remainder becomes zero. The value of `b` at that point is the GCD.

### Pseudo Code

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

### Example

**Input:** `a = 48, b = 18`

- **Iterative Calculation:**
  - Step 1: `a = 48, b = 18`, remainder = `48 % 18 = 12`
  - Step 2: `a = 18, b = 12`, remainder = `18 % 12 = 6`
  - Step 3: `a = 12, b = 6`, remainder = `12 % 6 = 0`
  - **Output:** `GCD = 6`

### Time Complexity

- **O(log(min(a, b)))** - Efficient time complexity, where `a` and `b` are the input numbers.

### Space Complexity

- **O(1)** - Constant space complexity.
[]
### Alternate Solution

- **Recursive Approach (Euclidean Algorithm):**

```python
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
```

### Explore more by yourself......