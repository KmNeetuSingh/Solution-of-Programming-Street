### 🔢 Determining Even/Odd Numbers - Editorial

### **Difficulty**: Easy  
### **Prerequisite**: Basic Arithmetic (Division, Modulus)  

---

### 💡 Hint  
Check the remainder when dividing the number by 2.

### 📝 Short Explanation  
- A number is classified as **even** if it is divisible by 2 (i.e., the remainder when divided by 2 is `0`).  
- If the remainder is non-zero, the number is classified as **odd**.

### 📚 Detailed Explanation  
- Every integer is either **even** or **odd**.
- An **even** number gives a remainder of `0` when divided by 2.  
- An **odd** number gives a remainder of `1` when divided by 2.  
- We use this property to determine whether a given number is even or odd by checking the remainder.

### 💻 **Pseudo code**:

```python
number  # The input number

if ( number % 2 == 0 ):
  Print("Even")
else:
  Print("Odd")
```

### 🔍 **Example**:

```python
Input: number = 4
Since 4 % 2 == 0, the output is "Even".

Input: number = 7
Since 7 % 2 != 0, the output is "Odd".
```

### ⏳ Time Complexity:  
`O(1)` — Only a single calculation is needed to check divisibility by 2.

### 📦 Space Complexity:  
`O(1)` — No extra space is required other than the input number.

### 🔄 Alternate Solution:  
None — The modulus operation is the simplest way to determine if a number is even or odd.
