### **Generating Pascal's Triangle - Editorial**

**Difficulty**: Medium  
**Topics**: Arrays, Mathematical Computations

---

### **Explanation**

Pascal's Triangle builds each row where:
- The first and last elements are always `1`.
- Non-boundary elements are the sum of the two elements directly above them from the previous row.

### **Steps**:
1. Start with the first row of Pascal's Triangle as `1`.
2. For each row `i`, generate the elements based on the previous row.
3. Each row starts and ends with `1`, and for the intermediate values, use the formula:
   \[
   \text{{num}} = \text{{num}} \times \left(\frac{{i - j}}{{j + 1}}\right)
   \]
   to compute the next number in the row.

### **Code**:

```python
def solve(n):
    for i in range(n):
        num = 1  
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)  
        print()  

# Example usage
solve(4)
```

### **Example**:

Input: `n = 4`  
Output:
```
1
1 1
1 2 1
1 3 3 1
```

### **Time Complexity**:  
- The time complexity is `O(n^2)` where `n` is the number of rows. This is because we loop through all elements in the triangle, where each row has a length proportional to its index.

### **Space Complexity**:  
- The space complexity is `O(1)` (ignoring the output storage), as no additional data structures are used apart from variables.
