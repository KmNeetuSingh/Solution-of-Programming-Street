# **🔢 Finding the Sum of Squares of Digits**

### **Difficulty**: Easy  
### **Topics**: Basic Programming, Mathematical Computations  

---

## **Problem Description**  
Write a program to compute the sum of the squares of the digits of a given number.  

For a number \( N \), the sum of squares of digits is calculated as:  
\[
\text{sum} = d_1^2 + d_2^2 + \ldots + d_k^2
\]  
where \( d_1, d_2, \ldots, d_k \) are the digits of \( N \).  

---

### **Input**  
- An integer `number`, which can be positive, negative, or zero.  

### **Output**  
- An integer representing the sum of the squares of the digits of the given number.  

---

### **Example**  

#### **Input**:  
```plaintext
number = 123
```

#### **Output**:  
```plaintext
14
```

#### **Explanation**:  
The digits of the number are \( 1, 2, \) and \( 3 \).  
Their squares are \( 1^2 = 1 \), \( 2^2 = 4 \), \( 3^2 = 9 \).  
The sum of the squares is \( 1 + 4 + 9 = 14 \).  

---

### **Edge Cases**  
1. **Single-Digit Numbers**:  
   - The sum is the square of the single digit.  
   - Example: \( N = 7 \rightarrow 7^2 = 49 \).  
2. **Negative Numbers**:  
   - Treat the number as its absolute value to compute the sum.  
   - Example: \( N = -123 \rightarrow 1^2 + 2^2 + 3^2 = 14 \).  
3. **Zero**:  
   - The sum of squares is \( 0 \).  
   - Example: \( N = 0 \rightarrow 0 \).  

---

## **Solution Approach**  

### **Algorithm**  
1. Take the absolute value of the input number to handle negative inputs.
2. Convert the number to a string so that we can extract each digit.
3. Use **list comprehension** to square each digit and sum them.
4. Return the computed sum.

---

### **Code Implementation**  

#### Python Code:  
```python
def sum_of_squares_of_digits(number):
    number = abs(number)  # Handle negative numbers
    # Use list comprehension to calculate squares of each digit and sum them up
    return sum(int(digit) ** 2 for digit in str(number))

# Example usage
number = 123
print(sum_of_squares_of_digits(number))  # Output: 14
```

---

### **Complexity Analysis**  

- **Time Complexity**:  
  - \( O(d) \): The program iterates through all the digits of the number, where \( d \) is the number of digits.  

- **Space Complexity**:  
  - \( O(1) \): Only a few variables are used, regardless of the input size.  

---

### **Code Examples**  

#### Example 1:  
```python
number = 123
print(sum_of_squares_of_digits(number))  # Output: 14
```

#### Example 2:  
```python
number = -456
print(sum_of_squares_of_digits(number))  # Output: 77
```

#### Example 3:  
```python
number = 0
print(sum_of_squares_of_digits(number))  # Output: 0
```

#### Example 4:  
```python
number = 7
print(sum_of_squares_of_digits(number))  # Output: 49
```

---

### **Key Takeaways**  
- The program handles both positive and negative numbers by using the absolute value.  
- It uses Python's **list comprehension** for a concise and efficient solution to compute the sum of squares.  
