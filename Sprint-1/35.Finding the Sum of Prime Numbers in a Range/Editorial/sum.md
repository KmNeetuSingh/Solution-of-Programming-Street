### 🔢 Finding the Sum of Prime Numbers in a Range - Editorial

### **Difficulty**: Medium  
### **Topics**: Number Theory, Mathematical Computations  

---

### 💡 Hint  
A prime number is only divisible by 1 and itself. Check for divisibility with numbers less than it.

### 📝 Short Explanation  
- Calculate the sum of all prime numbers within a given range. A prime number is greater than 1 and has no divisors other than 1 and itself.

### 📚 Detailed Explanation  
- To find the sum of prime numbers within a specified range, iterate through each number in that range.
- For each number, check if it is prime by attempting to divide it with all integers less than itself.
- If the number is determined to be prime, add it to a cumulative sum.

### 💻 **Pseudo code**:

```python
def sum_of_primes_in_range(r):
    prime_sum = 0

    for n in range(r[0], r[1] + 1):
        if n < 2:  
            continue
        is_prime = True 

        for i in range(2, n):
            if n != 2 and n % i == 0:  
                is_prime = False
                break

        if is_prime: 
            prime_sum += n

    print(prime_sum)
```

### 🔍 **Example**:

```python
Input: r = [1, 10]
Output: 17
Explanation: The sum of prime numbers between 1 and 10 is calculated as follows: 2 + 3 + 5 + 7 = 17.
```

### ⏳ Time Complexity:  
`O(n²)` — Each number in the range is checked for primality, resulting in a nested loop.

### 📦 Space Complexity:  
`O(1)` — Only a few variables are used, regardless of the input size.

### 🔄 Alternate Approach:  
An optimized approach would involve using the Sieve of Eratosthenes algorithm to efficiently find prime numbers, especially for larger ranges.
