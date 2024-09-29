# **Checking for an Anagram**  
**Difficulty**: Easy  
**Topics**: String Manipulation  

### Problem Statement
Write a program to check if two strings are anagrams.  
- **Input**: `str1 = "listen"`, `str2 = "silent"`  
- **Output**: `True`  
- **Explanation**: "listen" and "silent" are anagrams of each other.

### Short Observations
- An anagram is formed by rearranging the letters of another word.
- Two strings are anagrams if they contain the same characters with the same frequencies.

### Detailed Observations
1. **Length Check**: If the lengths of the two strings are not equal, they cannot be anagrams.
2. **Character Count**: Use an array to count the frequency of each character in the first string.
3. **Decrement Counts**: For each character in the second string, decrement the corresponding count in the array.
4. **Final Check**: If all counts are zero, the strings are anagrams.

### Pseudocode
```python
def anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    count = [0] * 26  # Assuming only lowercase letters
    for char in str1:
        count[ord(char) - ord('a')] += 1
    for char in str2:
        count[ord(char) - ord('a')] -= 1
    for c in count:
        if c != 0:
            return False
    return True
```

### Example
For `str1 = "listen"` and `str2 = "silent"`:
- Lengths are equal.
- Count the characters in "listen": `l=1, i=1, s=1, t=1, e=1, n=1`.
- Decrement counts with characters from "silent": `l=0, i=0, s=0, t=0, e=0, n=0`.
- All counts are zero, hence the output is `True`.

### Time and Space Complexity
- **Time Complexity**: O(n) where `n` is the length of the strings.
- **Space Complexity**: O(1), since the size of the character count array is fixed (26 for lowercase letters).

### Alternate Solutions
- You could also use sorting to determine anagrams by sorting both strings and checking for equality, but this approach is less efficient than counting characters.