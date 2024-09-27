# Finding the Sum of Elements in an Array ➕

## Difficulty: Easy  

### Prerequisite: Basic Understanding of Arrays  

---

### Hint  

Write a program to find the sum of all elements in a given array. This can be done either by iterating through the array manually or by utilizing Python's built-in `sum()` function for a more concise solution.  

---

### Short Observations  

- **Sum of Elements**: The total value when all elements of the array are added together.

---

### Detailed Observations  

1. **Initialize**: Start by setting the sum to zero.  
2. **Iterate**: Loop through the array and incrementally add each element to the sum.  
3. **Return the result**: Once the iteration is complete, return the total sum.  

---

### Pseudo Code  

#### Basic Approach  
```python
def sum_of_array(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum
```

#### Alternative Approach  
Using Python's built-in `sum()` function:  
```python
def sum_of_array(arr):
    return sum(arr)
```

#### Alternative Approach with List Comprehension  
For a more Pythonic one-liner approach:  
```python
def sum_of_array(arr):
    return sum([num for num in arr])
```

---

### Example  

**Input**:  
`array = [1, 2, 3, 4, 5]`

**Basic Approach**:  
1. Initialize the sum to `0`.  
2. Loop through the array and add each element:
   - Add `1` (sum now `1`).
   - Add `2` (sum now `3`).
   - Add `3` (sum now `6`).
   - Add `4` (sum now `10`).
   - Add `5` (sum now `15`).

**Output**:  
```text
Sum: 15
```

---

### Time Complexity  

- **O(n)** - Linear time complexity for all approaches, as each element needs to be visited once to compute the sum.  

### Space Complexity  

- **O(1)** - Constant space for both the basic approach and the `sum()` function since no extra space is required beyond the sum variable.  
