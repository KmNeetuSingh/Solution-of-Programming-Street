# **Finding the Count of Specific Digits in a Number**

## **Difficulty**: Easy  
## **Topics**: Basic Programming, String Manipulation  

### **Description**:
This program counts the occurrences of a specific digit in a given number.

### **Example**:
Input:  
`number = 122333`, `digit = 3`

Output:  
`3`

**Explanation**:  
The digit `3` appears `3` times in the number `122333`.

### **Code Implementation**:
```python
def count_digit_occurrences(number, digit):
    # Convert the number to a string and count the occurrences of the digit
    return str(number).count(str(digit))

# Example usage
number = 122333
digit = 3
print(count_digit_occurrences(number, digit))  # Output: 3
```

### **How It Works**:
1. The program converts the number to a string using `str(number)`.
2. It then counts how many times the specified digit (also converted to a string) appears in the number using the `.count()` method.
3. Finally, it returns the count of occurrences.

### **Time Complexity**:
- **O(n)**: The time complexity is linear in terms of the number of digits in the number, as the `.count()` method goes through each character in the string representation of the number.

### **Space Complexity**:
- **O(1)**: The space complexity is constant, as the program only uses a few variables to store the number and the count.

---