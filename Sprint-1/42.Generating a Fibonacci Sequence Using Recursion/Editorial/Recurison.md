# **Generating a Fibonacci Sequence Using Recursion**

## **Difficulty**: Medium  
## **Topics**: Recursion, Sequences  

### **Description**:
This program generates the Fibonacci sequence up to a given number using recursion.

### **Fibonacci Sequence**:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1. The sequence goes:  
`0, 1, 1, 2, 3, 5, 8, 13, 21, ...`

### **Example**:
Input:  
`number = 6`

Output:  
`0 1 1 2 3 5`

**Explanation**:  
The Fibonacci sequence up to the 6th number is: `0, 1, 1, 2, 3, 5`.

### **Code Implementation**:
```python
def fibonacci(n):
    # Base case: return n for 0 and 1
    if n <= 1:
        return n
    # Recursive case: sum of previous two numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci_sequence(limit):
    # Generate Fibonacci sequence up to the given limit
    sequence = []
    for i in range(limit):
        sequence.append(fibonacci(i))
    return sequence

# Example usage
number = 6
print(generate_fibonacci_sequence(number))  # Output: [0, 1, 1, 2, 3, 5]
```

### **How It Works**:
1. The function `fibonacci(n)` computes the n-th Fibonacci number using recursion. The base case is when `n` is 0 or 1.
2. The `generate_fibonacci_sequence(limit)` function calls the `fibonacci()` function for each number from `0` to `limit-1` to generate the full sequence.
3. The final sequence is returned as a list.

### **Time Complexity**:
- **O(2^n)**: The time complexity of the recursive approach is exponential due to repeated calculations for the same Fibonacci numbers.

### **Space Complexity**:
- **O(n)**: The space complexity is O(n) because of the recursion stack used to store function calls.

---

### **Optimization**:
- This recursive approach is simple but inefficient for large values of `n`. You can optimize it using dynamic programming or memoization to avoid redundant calculations.
