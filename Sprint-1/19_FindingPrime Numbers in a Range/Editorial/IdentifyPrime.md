# **Finding Prime Numbers in a Range** 🔍

## Difficulty: Easy  
**Topics**: Basic Programming, Number Theory  

---

### Prerequisite: Understanding of Prime Numbers  

---

### Hint  

A **prime number** is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. Your task is to find all prime numbers within a given range.

---

### Short Observations  

- **Prime Number**: A prime number is only divisible by 1 and itself.  
- For example, `11` is a prime number because its only divisors are 1 and 11.  

---

### Detailed Observations  

1. **Range Input**: We are given two numbers that define the lower and upper bounds of the range.  
2. **Check Prime**: For each number in the range, check if it is a prime number by checking for factors from 2 to the number itself.  
3. **Return Prime Numbers**: Collect and return all prime numbers found within the range.  

---

### Pseudocode 🖥️  

#### Basic Approach  
```python
# Define the range
i = [10, 30]  
primes = []  

for num in range(i[0], i[1] + 1):
    if num < 2:  
        continue
    sam = "Yes" 
    for j in range(2, num):  
        if num != 2 and num % j == 0:  
            sam = "No" 
            break  
    if sam == "Yes":  
        primes.append(num)  

print(primes)  # Output the list of prime numbers
```

---

### Example  

**Input**:  
`range = [10, 30]`  

**Steps**:  
1. Iterate over each number from `10` to `30`.  
2. For each number, check if it's a prime number using the `identifyPrime` logic.  
3. Collect and return the prime numbers.

**Output**:  
```text
[11, 13, 17, 19, 23, 29]
```

---

### Time Complexity  

- **O(n²)** where `n` is the size of the range, since for each number we check divisibility with all smaller numbers.

### Space Complexity  

- **O(k)** where `k` is the number of prime numbers found and stored in the list.