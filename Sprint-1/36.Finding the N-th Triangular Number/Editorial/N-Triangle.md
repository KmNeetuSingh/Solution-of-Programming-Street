# 📐 Finding the N-th Triangular Number  

### **Difficulty**: Easy  
### **Topics**: Basic Programming, Mathematical Computations  

---

## **Problem Description**  
Write a program to find the N-th triangular number. A triangular number represents the sum of the first N natural numbers. It can be calculated using the formula:  

\[
T_N = \frac{N \times (N + 1)}{2}
\]

---

### **Input**  
- An integer `N` representing the position of the triangular number to calculate.  

### **Output**  
- The N-th triangular number.  

---

### **Example**  

#### Input:  
```plaintext
N = 4
```

#### Output:  
```plaintext
10
```

#### Explanation:  
The 4th triangular number is the sum of the first 4 natural numbers:  
1 + 2 + 3 + 4 = **10**

---

### **Solution Approach**  

1. **Understanding the Formula**  
   - The N-th triangular number is the sum of the first `N` natural numbers. Using the formula:  
     \[
     T_N = \frac{N \times (N + 1)}{2}
     \]
     We can calculate the triangular number in constant time.  

2. **Implementation**  
   - Use the formula directly in a program to compute the N-th triangular number.

---

### **Code Implementation**  

#### Python Code:  
```python
def find_triangular_number(N):
    # Calculate using the formula
    return (N * (N + 1)) // 2

# Example usage
N = 4
print(find_triangular_number(N))  # Output: 10
```

---

### **Complexity Analysis**  

- **Time Complexity**:  
  - **O(1)** — The formula calculates the result in constant time.  

- **Space Complexity**:  
  - **O(1)** — No additional space is used apart from basic variables.  

---

### 📚 **Key Takeaways**  
- The problem demonstrates the power of mathematical formulas in simplifying calculations.  
- Using the formula ensures both efficiency and accuracy. 