# **Calculating the Power of a Number**

## **Overview**
This program calculates the power of a given base number raised to a specific exponent. It handles both positive and negative exponents.

## **Difficulty**
- Easy

## **Topics Covered**
- Basic Programming
- Mathematical Computations

## **How It Works**
The program takes two inputs:
- **base**: The number that will be multiplied.
- **exponent**: The number of times the base will be multiplied by itself.

### **Mathematical Formula**
For `base` raised to `exponent`, the formula is:
```
base^exponent = base * base * ... * base (exponent times)
```

If the exponent is negative, the result is the reciprocal of the base raised to the positive exponent.

## **Getting Started**

### **Prerequisites**
- Basic understanding of programming concepts.
- Familiarity with loops and conditions.

### **Installation**
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.

### **Usage**
To run the program, simply execute the Python script:

```bash
python power_calculator.py
```

### **Input**
- **base**: Enter the base number.
- **exponent**: Enter the exponent to which the base should be raised.

### **Example**

```bash
Input: base = 2, exponent = 3
Output: 8

Input: base = 2, exponent = -2
Output: 0.25
```

### **Pseudo Code**
1. Input base and exponent.
2. Initialize `result = 1`.
3. Loop:
    - If `exponent > 0`, multiply `result` by `base` `exponent` times.
    - If `exponent < 0`, multiply `result` by `base` with positive `exponent`, then set `result = 1 / result`.
4. Output the result.

### **Time Complexity**
- O(n), where `n` is the absolute value of the exponent.

### **Space Complexity**
- O(1), only using a few variables.

