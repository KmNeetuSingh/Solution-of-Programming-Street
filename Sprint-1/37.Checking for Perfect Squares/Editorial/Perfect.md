# ✅ **Checking for Perfect Squares**

### **Difficulty**: Easy  
### **Topics**: Mathematical Computations  

---

## **Problem Description**  
Write a program to determine if a given number is a perfect square.  
A number is a perfect square if there exists an integer \( x \) such that:  
\[
x^2 = \text{number}
\]

---

### **Input**  
- An integer `number`, representing the value to be checked.  

### **Output**  
- `True` if the number is a perfect square.  
- `False` otherwise.  

---

### **Example**  

#### **Input**:  
```plaintext
number = 16
```

#### **Output**:  
```plaintext
True
```

#### **Explanation**:  
The number 16 is a perfect square because \( 4^2 = 16 \).  

#### **Input**:  
```plaintext
number = 20
```

#### **Output**:  
```plaintext
False
```

#### **Explanation**:  
The number 20 is not a perfect square as there is no integer \( x \) such that \( x^2 = 20 \).  

---

## **Solution Approach**  

### **Algorithm**  
1. Check if the input number is negative. Negative numbers cannot be perfect squares.  
2. Iterate through all integers from 0 to the square root of the number (inclusive).  
3. For each integer, check if its square equals the input number.  
4. If a match is found, return `True`.  
5. If no match is found after the loop, return `False`.  

---

### **Code Implementation**  

#### Python Code:  
```python
def is_perfect_square(number):
    if number < 0:
        return False  # Negative numbers cannot be perfect squares
    for i in range(int(number ** 0.5) + 1):  # Check up to the square root of the number
        if i * i == number:
            return True
    return False

# Example usage
number = 16
print(is_perfect_square(number))  # Output: True
```

---

### **Complexity Analysis**  

- **Time Complexity**:  
  - \( O(\sqrt{N}) \): The loop runs up to the square root of the number.  

- **Space Complexity**:  
  - \( O(1) \): No extra space is used.  

---

### **Edge Cases**  

1. **Negative Numbers**:  
   - Return `False` for negative numbers as they cannot be perfect squares.  
   - Example: \( -4 \rightarrow \text{False} \).  

2. **Zero**:  
   - \( 0^2 = 0 \), so the function should return `True` for \( 0 \).  
   - Example: \( 0 \rightarrow \text{True} \).  

3. **Large Numbers**:  
   - The loop runs efficiently up to the square root of the number, making it feasible for reasonably large inputs.  

---

### **Code Examples**  

#### Example 1:  
```python
is_perfect_square(16)  # Output: True
```

#### Example 2:  
```python
is_perfect_square(20)  # Output: False
```

#### Example 3:  
```python
is_perfect_square(-9)  # Output: False
```

#### Example 4:  
```python
is_perfect_square(0)  # Output: True
```

---

### 📚 **Key Takeaways**  
- This implementation avoids using external libraries like `math.sqrt` and uses simple iteration to determine if a number is a perfect square.  
- It effectively handles edge cases like negative numbers and zero.