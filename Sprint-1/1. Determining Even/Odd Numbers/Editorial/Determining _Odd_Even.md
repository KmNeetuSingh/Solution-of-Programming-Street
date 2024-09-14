### Determining Even/Odd Numbers - Editorial

### Difficulty: Easy

### Prerequisite: Basic Arithmetic (Division, Modulus).
---

### Hint

Check the remainder when dividing the number by 2.

### Short Explanation

- A number is classified as **even** if it is divisible by 2, meaning the remainder when divided by 2 is zero. If the remainder is non-zero, the number is classified as **odd**.

### Detailed Explanation

- Every integer can either be even or odd. An even number is divisible by 2, i.e., the number gives a remainder of 0 when divided by 2.
  
- On the other hand, an odd number will give a remainder of 1 when divided by 2. This basic property is used to check whether a given number is even or odd.

- We iterate through the input number (or take a single input) and check the remainder after division by 2 to determine if it is even or odd.

- **Pseudo code**:

```python
number; // The input number

if ( number % 2 == 0 ):

  Print("Even");

else:

  Print("Odd");
```

- **Example**:

```python
    Input: number = 4
    
    Since 4 % 2 == 0, the output is "Even".
    
    Input: number = 7
    
    Since 7 % 2 != 0, the output is "Odd".
```

### Time Complexity:

`O(1)`. 

Only a single calculation is required to check the remainder for divisibility by 2.

### Space Complexity:

`O(1)`.

No extra space is required apart from the input number.

### Alternate Solution:

None.