Here’s the updated `README.md` file with the alternative approach added:
# Finding the Largest and Smallest Numbers in an Array  
## Difficulty: Easy

### Prerequisite: Basic Understanding of Arrays

---

### Hint

Write a program to find both the largest and smallest numbers in a given array. You can achieve this by iterating through the array manually or by using built-in Python functions like `max()` and `min()`.

---

### Short Observations

- **Smallest Number:** The number with the lowest value in the array.
- **Largest Number:** The number with the highest value in the array.

---

### Detailed Observations

1. **Initialize:** Start by setting the smallest and largest values as the first element in the array.
2. **Iterate:** Loop through the array, updating the smallest and largest numbers whenever a smaller or larger number is found.
3. **Return the result.**

---

### Pseudo Code

#### Basic Approach  
```python
def find_largest_and_smallest(arr):
    if len(arr) == 0:
        return None, None
    
    smallest = arr[0]
    largest = arr[0]
    
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    return largest, smallest
```

#### Alternative Approach  
Using Python's built-in functions `max()` and `min()`:
```python
def find_largest_and_smallest(arr):
    if len(arr) == 0:
        return None, None
    
    return max(arr), min(arr)
```

#### Alternative Approach with Sorting  
You can also use sorting to find the smallest and largest numbers:
```python
def find_largest_and_smallest(arr):
    if len(arr) == 0:
        return None, None
    
    sorted_arr = sorted(arr)
    return sorted_arr[-1], sorted_arr[0]
```

---

### Example

**Input:**  
`array = [4, 7, 1, 8, 5]`

**Basic Approach:**  
1. Initialize smallest and largest as the first element (`4`).
2. Iterate through the array, updating the smallest and largest numbers:
   - Compare `7` (largest now `7`).
   - Compare `1` (smallest now `1`).
   - Compare `8` (largest now `8`).
   - Compare `5` (no change).

**Output:**  
```text
Largest: 8, Smallest: 1
```

---

### Time Complexity

- **O(n)** - Linear time complexity for both the basic and built-in functions approach.
- **O(n log n)** - For the sorting approach due to the sorting operation.

### Space Complexity

- **O(1)** - For the basic and built-in functions approach since only a few variables are used.
- **O(n)** - For the sorting approach since a new sorted array is created.
