# Checking for Armstrong Numbers in a Range 🎯

## Difficulty: Easy  
**Topics**: Basic Programming, Number Theory  

---

### Prerequisite: Understanding of Armstrong Numbers  

---

### Hint  

An **Armstrong number** (also known as a **Narcissistic number**) is a number that is equal to the sum of its digits each raised to the power of the number of digits. Your task is to find all Armstrong numbers within a given range.

---

### Short Observations  

- **Armstrong Number**: A number that equals the sum of its digits each raised to the power of the number of digits.  
- For example, `153` is an Armstrong number because \(1^3 + 5^3 + 3^3 = 153\).  

---

### Detailed Observations  

1. **Range Input**: We are given two numbers that define the lower and upper bounds of the range.  
2. **Check Armstrong**: For each number in the range, check if it is an Armstrong number by computing the sum of its digits raised to the power of the number of digits.  
3. **Return Armstrong Numbers**: Collect and return all Armstrong numbers found within the range.  

---

### Pseudocode 🖥️  

#### Basic Approach  
```python
def is_armstrong(num):
    digits = list(map(int, str(num)))  # Convert number to list of digits
    power = len(digits)  # Number of digits
    total_sum = sum([digit ** power for digit in digits])  # Sum of digits raised to the power
    return total_sum == num  # Check if it equals the original number

def find_armstrong_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            result.append(num)
    return result
```

---

### Example  

**Input**:  
`range = [1, 500]`

**Steps**:  
1. Iterate over each number from `1` to `500`.
2. For each number, check if it's an Armstrong number.
3. Collect and return Armstrong numbers.

**Output**:  
```text
[1, 153, 370, 371, 407]
```

---

### Time Complexity  

- **O(n * d)** where `n` is the size of the range and `d` is the number of digits in the largest number.  

### Space Complexity  

- **O(1)** for storing the results, assuming the number of Armstrong numbers is small compared to the range.
