## Finding the Least Common Multiple (LCM)
### Difficulty: Easy

### Prerequisite: Basic Understanding of Multiples and GCD

---

### Hint

The LCM of two numbers is the smallest positive integer that is divisible by both numbers.

### Short Explanation

- Compute the LCM using the relationship between LCM and GCD.

### Detailed Explanation

- **Definition:** The LCM of two numbers `a` and `b` is the smallest number that is a multiple of both `a` and `b`.
- **Method:** Utilize the formula that relates LCM and GCD:
  
  \[
  \text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}
  \]

### Pseudo Code

**Iterative Approach:**
```python
def lcm(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)
```

### Example

**Input:** `a = 12, b = 15`

- **Calculate GCD:**
  - `gcd(12, 15)` yields `3`.

- **Compute LCM:**
  - Apply the formula: `LCM = (12 * 15) / 3 = 180 / 3 = 60`.

- **Output:** `60`

### Time Complexity

- **O(log(min(a, b)))** - Time complexity for calculating GCD using the iterative approach.

### Space Complexity

- **O(1)** - Constant space complexity.
