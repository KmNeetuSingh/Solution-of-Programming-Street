### 🔍 Detect if a Number is Prime - Editorial

### **Difficulty**: Easy  
### **Prerequisite**: Mathematics  

---

### 💡 Hint  
A prime number `N` is only divisible by 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are the first few prime numbers.

### 📝 Short Explanation  
- A number is prime if it has exactly two divisors: 1 and the number itself. To determine if a number `N` is prime, check all numbers between 2 and `N-1` for divisibility.

### 📚 Detailed Explanation  
- If a number `N` is prime, it is divisible only by 1 and `N`.
- The logic is straightforward:
  - Check each number `i` from 2 to `N-1`.
  - If any `i` divides `N` without a remainder (`N % i == 0`), then `N` is not prime.
  - If no number between 2 and `N-1` divides `N`, the number is prime.
  
This method works, although it can be slow for larger numbers due to the number of checks.

### 💻 Pseudo code:

```python
def identifyPrime(n):
    sam = "Yes"
    for i in range(2, n):
        if n != 2 and n % i == 0:
            sam = "No"
            break
    print(sam)
```

### 🔍 **Example**:

```python
Input: number = 5

- Loop through numbers from 2 to 4.
- Check divisibility:
  - 5 % 2 != 0
  - 5 % 3 != 0
  - 5 % 4 != 0
- Since no number divides 5, output "Yes" (Prime).
```

```python
Input: number = 6

- Loop through numbers from 2 to 5.
- Check divisibility:
  - 6 % 2 == 0
- Since 6 is divisible by 2, output "No" (Not Prime).
```

### ⏳ Time Complexity  
`O(N)`  
- The function checks divisibility for all integers between 2 and `N-1`.

### 📦 Space Complexity  
`O(1)`  
- No additional space is required other than the input number and a few variables.

### 🔄 Alternate Solution  
None — This method checks every number between 2 and `N-1` for divisibility.

