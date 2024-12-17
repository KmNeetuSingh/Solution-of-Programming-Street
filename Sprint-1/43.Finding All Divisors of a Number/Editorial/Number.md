# Finding All Divisors of a Number

## **Difficulty**: Easy  
## **Topics**: Basic Programming, Mathematical Computations

### **Description**:
This program finds all divisors of a given number. A divisor is a number that divides the given number evenly (without a remainder). For instance, the divisors of 12 are 1, 2, 3, 4, 6, and 12.

### **Example**:
- **Input**:  
  `number = 12`
  
- **Output**:  
  `1, 2, 3, 4, 6, 12`

- **Explanation**:  
  The divisors of 12 are 1, 2, 3, 4, 6, and 12, as they divide 12 without leaving a remainder.

### **Approach**:
To find the divisors of a number:
1. Loop through all numbers from 1 to the number itself.
2. Check if each number divides the given number without leaving a remainder.
3. If a number divides evenly, it's a divisor.

### **Code**:

```python
def find_divisors(number):
    divisors = []
    
    for i in range(1, number + 1):  # Loop through numbers from 1 to the number
        if number % i == 0:  # Check if i is a divisor
            divisors.append(i)
    
    return divisors

# Example usage
number = 12
print("Divisors:", find_divisors(number))  # Output: Divisors: [1, 2, 3, 4, 6, 12]
```

### **Time Complexity**:
- **O(n)** — The program loops through all numbers from 1 to `n`, where `n` is the input number.

### **Space Complexity**:
- **O(n)** — The space used is proportional to the number of divisors found, which can be as large as `n` in the worst case.
