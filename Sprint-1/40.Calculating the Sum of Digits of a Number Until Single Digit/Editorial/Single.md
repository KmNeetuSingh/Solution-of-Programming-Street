# **Calculating the Sum of Digits of a Number Until Single Digit**

## **Difficulty**: Medium  
## **Topics**: Mathematical Computations  

### **Description**:
This program takes a number as input and keeps summing its digits until a single digit is obtained.

### **Example**:
Input:  
`number = 9875`

Output:  
`2`

**Explanation**:  
1. The sum of the digits is `9 + 8 + 7 + 5 = 29`.
2. Sum the digits of `29`, which gives `2 + 9 = 11`.
3. Sum the digits of `11`, which gives `1 + 1 = 2`, a single digit.

### **Code Implementation (Easiest Approach)**:
The easiest approach is to repeatedly sum the digits of the number until it becomes a single digit.

```python
def sum_of_digits_until_single(number):
    while number >= 10:  # Keep summing digits until the number is a single digit
        number = sum(int(digit) for digit in str(number))  # Sum the digits of the number
    return number

# Example usage
number = 9875
print(sum_of_digits_until_single(number))  # Output: 2
```

### **How It Works**:
1. The program enters a `while` loop that continues until the number is less than 10 (a single digit).
2. Inside the loop, it calculates the sum of the digits of the current number by converting the number to a string and using a generator expression to sum each digit.
3. Once the number is reduced to a single digit, the loop ends, and the result is returned.

### **Time Complexity**:
- **O(d)**: The program repeatedly sums the digits, where `d` is the number of digits in the original number. In each iteration, the number of digits reduces until a single digit is obtained.

### **Space Complexity**:
- **O(1)**: The program only uses a few variables for the sum and digits, so the space complexity is constant.

---

