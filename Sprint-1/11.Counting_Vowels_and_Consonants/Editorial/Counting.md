# Counting Vowels and Consonants in a String  
## Difficulty: Easy

### Prerequisite: Basic Understanding of Strings

---

### Hint

Count the vowels and consonants in a string. Vowels are `a, e, i, o, u` (case-insensitive), and consonants are all other alphabetic characters.

---

### Short Observations

- **Vowels:** `a, e, i, o, u` (both uppercase and lowercase).
- **Consonants:** All other alphabetic characters.

---

### Detailed Observations

1. **Iterate:** Loop through each character of the string.
2. **Check:** Identify whether the character is a vowel or consonant.
3. **Count:** Track counts for each category.

---

### Pseudo Code

#### Basic Approach
```python
Input = "Hey BROO KeepGoing Happy Coding"  
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in Input:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
```

#### Alternative Approach  
Using `collections.Counter`:
```python
from collections import Counter

def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    counts = Counter(s)
    vowel_count = sum(counts[char] for char in vowels)
    consonant_count = sum(counts[char] for char in counts if char.isalpha() and char not in vowels)
    
    return vowel_count, consonant_count
```

---

### Example

**Input:**  
`string = "hello world"`

**Basic Approach:**  
1. Iterate through the string.
2. Count vowels (`e`, `o`, `o` → 3).
3. Count consonants (`h`, `l`, `l`, `w`, `r`, `l`, `d` → 7).

**Output:**
```text
Vowels: 3, Consonants: 7
```

---

### Time Complexity

- **O(n)** - Linear time complexity for both approaches.

### Space Complexity

- **Basic Approach:** O(1) - Constant space.
- **Alternative Approach:** O(k) - Space for character counts, where `k` is the number of unique characters.