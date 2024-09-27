## Summing Digits of a Number  
### Difficulty: Easy

### Prerequisite: Basic Understanding of Modulus and Division Operations

---

### Hint

To calculate the sum of digits of a number, repeatedly extract each digit by using modulus (`%`) and reduce the number by using division (`//`).

### Short Explanation

- The sum of the digits of a number can be found by continuously extracting each digit (using `% 10`) and reducing the number (using `// 10`) until the number becomes `0`.

### Detailed Explanation

- **Definition:** To sum the digits of a number, repeatedly extract the last digit and add it to the sum.
- **Method:**  
  - Use modulus (`% 10`) to get the last digit.
  - Use integer division (`// 10`) to remove the last digit from the number.
  - Continue this process until the number becomes `0`.

### Pseudo Code

**Iterative Approach:**

```python
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n = n // 10      
    return total
```

### Example

**Input:** `number = 1234`

- **Iterative Calculation:**
  - Initialize `total = 0`
  - First iteration: `total += 1234 % 10` → `total = 4`, `n = 1234 // 10` → `n = 123`
  - Second iteration: `total += 123 % 10` → `total = 7`, `n = 123 // 10` → `n = 12`
  - Third iteration: `total += 12 % 10` → `total = 9`, `n = 12 // 10` → `n = 1`
  - Fourth iteration: `total += 1 % 10` → `total = 10`, `n = 1 // 10` → `n = 0`
  - **Output:** `10`

### Time Complexity

- **O(d)** - Where `d` is the number of digits in `n`.

### Space Complexity

- **O(1)** - Constant space is used.

### Alternate Solution

- **Recursive Approach:**

```python
def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursive(n // 10)
```