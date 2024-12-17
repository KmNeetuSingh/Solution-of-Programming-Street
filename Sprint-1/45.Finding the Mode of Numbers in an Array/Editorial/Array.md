# **Finding the Mode of Numbers in an Array**

**Difficulty**: Medium  
**Topics**: Arrays, Statistical Analysis

## **Description**  
This program finds the mode (the most frequent number) in an array. If there are multiple modes, it returns the one that appears first. If the array is empty, it returns `None`.

## **Example**

### Input:
```python
array = [1, 2, 2, 3, 4, 4, 4]
```

### Output:
```python
4
```

### Explanation:  
The most frequent number in the array is `4`.

## **Code**:

```python
from collections import Counter

def find_mode(array):
    if not array:
        return None
    frequency = Counter(array)
    return frequency.most_common(1)[0][0]

# Example usage
array = [1, 2, 2, 3, 4, 4, 4]
print("Mode:", find_mode(array))  # Output: 4
```

## **Time Complexity**:  
`O(n)` — where `n` is the number of elements in the array. The time complexity is due to the use of `Counter` which processes the array in linear time.

## **Space Complexity**:  
`O(n)` — The space complexity is linear because `Counter` stores the frequency of each element.

---
