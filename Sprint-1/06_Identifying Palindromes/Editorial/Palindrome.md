## Identifying Palindromes
### Difficulty: Easy

### Prerequisite: Basic Understanding of Strings and Numbers

---

### Hint

A value is a palindrome if it reads the same forwards and backwards.

### Short Observations

- **Definition:** A value is a palindrome if it matches its reverse.
- **Check:** Compare the value with its reverse.

### Detailed Observations

1. **Reversal Approach:** Convert the value to a string, reverse it, and compare it with the original.
2. **Normalization:** For strings, consider removing non-alphanumeric characters and ignoring case.

### Pseudo Code

```python
def is_palindrome(value):
    # Convert value to string for uniform handling
    s = str(value)
    # Reverse the string
    reversed_s = s[::-1]
    # Compare the original string with its reversed version
    return "Palindrome" if s == reversed_s else "Not Palindrome"
```

### Example

**Input:** `value = "radar"`

1. **Convert to String:** "radar"
2. **Reverse String:** "radar"
3. **Compare:** "radar" == "radar"

**Output:**
```text
Palindrome
```

**Input:** `value = 121`

1. **Convert to String:** "121"
2. **Reverse String:** "121"
3. **Compare:** "121" == "121"

**Output:**
```text
Palindrome
```

### Time Complexity

- **O(n)** - Linear time complexity, where `n` is the length of the value.

### Space Complexity

- **O(n)** - Space for storing the reversed string.