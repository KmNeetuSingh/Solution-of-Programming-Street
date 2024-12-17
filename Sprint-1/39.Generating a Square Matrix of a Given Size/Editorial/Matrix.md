# **Generating a Square Matrix of a Given Size**

## **Difficulty**: Medium  
## **Topics**: Arrays, Matrix Operations  

### **Description**:
This program generates a square matrix of a specified size and fills it with sequential numbers starting from 1.

### **Example**:
Input:  
`size = 3`

Output:  
```
1 2 3  
4 5 6  
7 8 9
```

### **Explanation**:
- The program takes a `size` as input and generates a matrix with dimensions `size x size`.
- It fills the matrix with sequential numbers, starting from 1, in a row-wise manner.
- The numbers in each row are separated by spaces.

### **Code Implementation**:
```python
def generate_square_matrix(size):
    matrix = [[(i * size + j + 1) for j in range(size)] for i in range(size)]
    
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
size = 3
generate_square_matrix(size)
```

### **How It Works**:
1. The program uses a **list comprehension** to generate the matrix. For each row, it computes the values in the sequence `(i * size + j + 1)` where `i` is the row index and `j` is the column index.
2. After creating the matrix, it iterates over the rows and prints the matrix with space-separated values for a cleaner output.

### **Time Complexity**:
- **O(n²)**: The program iterates over all elements of the `n x n` matrix, where `n` is the given size.

### **Space Complexity**:
- **O(n²)**: The program stores the matrix in memory, which requires space proportional to the number of elements (`n²`).
