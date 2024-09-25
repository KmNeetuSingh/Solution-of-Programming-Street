# Reversing a String  
## Difficulty: Easy

### Prerequisite: Basic Programming, String Manipulation

---

### Hint

Write a program to reverse a given string. The key is to iterate over the string in reverse order or use Python's slicing technique.

---

### Short Observations

- **String Reversal:** You can either use a loop to reverse each character or utilize Python's built-in slicing feature.

---

### Detailed Observations

1. **Loop through:** Start from the last character of the string and append each character to a new string, or use string slicing for simplicity.
2. **Return the reversed string**.

---

### Pseudo Code

#### Basic Approach  
```python
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
```

#### Alternative Approach  
Using Python's slicing:
```python
def reverse_string(s):
    return s[::-1]
```

---

### Example

**Input:**  
`string = "programming"`

**Basic Approach:**  
1. Loop through the string from the last character to the first.
2. Construct a new string by appending each character in reverse order.

**Output:**  
```text
"gnimmargorp"
```

---

### Time Complexity

- **O(n)** - Linear time complexity for both approaches, where `n` is the length of the string.

### Space Complexity

- **O(n)** - For storing the reversed string.

