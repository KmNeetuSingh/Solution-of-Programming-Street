# Finding the Largest Palindrome in a String

## Difficulty: Easy

## Topics: Basic Programming, String Manipulation

### Problem Description

Write a program to find the largest palindrome in a given string. A palindrome is a string that reads the same backward as forward.

### Input

- A string `s` which may contain letters, digits, or special characters.

### Output

- The largest palindrome found within the input string.

### Example

**Input:**  
`"babad"`

**Output:**  
`"bab"` or `"aba"`  
Explanation: Both "bab" and "aba" are valid palindromes in the string.

### Approach

1. **Check for Palindrome**: Implement a function to check if a substring is a palindrome by comparing it to its reverse.
2. **Iterate Through Substrings**: Use nested loops to generate all possible substrings of the input string.
3. **Track the Largest Palindrome**: For each palindrome found, compare its length with the current maximum length and update accordingly.
4. **Print the Result**: Output the largest palindrome found.

### Sample Code

```python
def is_palindrome(s):
    return s == s[::-1]  

def find_largest_palindrome(s):
    max_length = 0
    largest_palindrome = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):  
            sub = s[i:j]
            if is_palindrome(sub):
                if len(sub) > max_length:
                    max_length = len(sub)
                    largest_palindrome = sub

    print(largest_palindrome)

# Example usage
find_largest_palindrome("babad")  
```

### Complexity

- **Time Complexity**: O(n^3) due to the nested loops and the palindrome check.
- **Space Complexity**: O(1) for the palindrome check itself, but the largest palindrome string will depend on the input size.

### Constraints

- The input string can contain letters, digits, or special characters.
- The function will return an empty string if no palindrome is found.
