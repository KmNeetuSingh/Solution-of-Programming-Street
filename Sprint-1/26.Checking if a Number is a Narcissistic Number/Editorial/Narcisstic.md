# Checking if a Number is a Narcissistic Number

**Difficulty**: Easy  
**Topics**: Basic Programming, Number Theory

## Problem Description

Write a program to check if a number is a narcissistic number. A narcissistic number is 
\
defined as a number where the sum of its digits raised to the power of the number of digits equals the number itself.

## Input

- An integer `number`, which is the number to check.

## Output

- A message indicating whether the number is a narcissistic number or not.

## Example

**Input:**  
`number = 153`

**Output:**  
`Narcissistic Number`

**Explanation:**  
153 is a narcissistic number because \(1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153\).

## Constraints

- The input number will be a positive integer.

## Approach

### Custom Logic Approach

1. Convert the number to a string to easily access each digit.
2. Count the number of digits in the number.
3. Initialize a variable to store the sum of the digits raised to the power of the number of digits.
4. Iterate through each digit, convert it back to an integer, raise it to the power of the number of digits, and add it to the sum.
5. Compare the calculated sum with the original number to determine if it is a narcissistic number.

### Sample Code
```python
number = 153 

# Convert the number to a string to access digits
digits_str = str(number)
num_digits = len(digits_str)  # Count the number of digits
sum_of_powers = 0  # Initialize the sum

# Calculate the sum of digits raised to the power of the number of digits
for digit in digits_str:
    sum_of_powers += int(digit) ** num_digits  # Raise to power and add to sum

# Check if the sum equals the original number
if sum_of_powers == number:
    print("Narcissistic Number")
else:
    print("Not a Narcissistic Number")
```

## Time Complexity

- **O(d)**, where `d` is the number of digits in the number, as we iterate through each digit once.

## Space Complexity

- **O(1)**, as we use a constant amount of space regardless of the input size.

## Alternative Approach
You can do it without converting it into the string ....Explore by own