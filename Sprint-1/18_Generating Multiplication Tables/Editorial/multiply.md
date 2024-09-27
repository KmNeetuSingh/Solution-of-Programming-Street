# Generating Multiplication Tables ✖️

## Difficulty: Easy  
**Topics**: Basic Programming, Mathematical Computations  

---

### Prerequisite: Understanding of Loops  

---

### Hint  

Write a program that takes a number as input and generates its multiplication table. The table should show the results from multiplying the number by 1 up to a specified limit.

---

### Short Observations  

- **Multiplication Table**: A table that lists the products of a number with integers in a sequential order.
- For example, for the number 4, the multiplication table will show how 4 interacts with the numbers 1 through 5.

---

### Detailed Observations  

1. **Input Number**: Start by taking a number as input for which the multiplication table will be generated.
2. **Loop**: Use a loop to multiply the input number by each integer from 1 to 5 (or any specified limit).
3. **Print the Result**: Format the output to display the multiplication in a readable manner.

---

### Pseudocode 🖥️  

```python
def generate_multiplication_table(number):
    for i in range(1, 6):  # Loop from 1 to 5
        result = number * i  # Calculate the product
        print(f"{number} x {i} = {result}")  # Print the multiplication statement
```

---

### Example  

**Input**:  
`number = 4`

**Output**:  
```
4 x 1 = 4  
4 x 2 = 8  
4 x 3 = 12  
4 x 4 = 16  
4 x 5 = 20  
```

**Explanation**: The multiplication table for 4 up to 5 is generated.

---

### Time Complexity  

- **O(n)** - Linear time complexity, where n is the number of multiplications (in this case, 5).

### Space Complexity  

- **O(1)** - Constant space since only a few variables are used.
