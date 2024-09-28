# Finding the Number of Digits in a Number
**Difficulty**: Easy  
**Topics**: Basic Programming, Mathematical Computations
## Problem Description

Write a program to count the number of digits in a given number.

## Input

- An integer `number`, for which you want to find the digit count.

## Output

- An integer representing the number of digits in the specified number.

## Example

**Input:**  
`number = 12345`

**Output:**  
`5`

**Explanation:**  
The number 12345 has 5 digits.

## Constraints

- The input number can be any integer (positive, negative, or zero).

## Approach
1. Initialize a counter variable to zero.
2. Convert the number to its absolute value to handle negative numbers.
3. Use a loop to divide the number by 10 until it becomes zero, incrementing the counter for each division.
4. Output the counter, which represents the number of digits.

### Sample Code 

```python
number = 12345  
count = 0  
number = abs(number)
while number > 0:
    number //= 10  
    count += 1  

print(count)
```

## Time Complexity

- **O(log(n))**, where `n` is the input number, due to the repeated division by 10.

## Space Complexity

- **O(1)**, as the space used does not grow with the size of the input.