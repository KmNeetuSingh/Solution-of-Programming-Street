### Armstrong Number - Explanation

### Difficulty: Easy

### Prerequisite: Basic Understanding of Number Theory

---

### Hint

An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

### Short Explanation

To determine if a number is an Armstrong number:
- Convert the number to a string to iterate through its digits.
- Compute the number of digits.
- Sum each digit raised to the power of the total number of digits.
- If this sum equals the original number, it is an Armstrong number.

### Detailed Explanation

- **Rules to Determine an Armstrong Number:**
  1. **Step 1:** Convert the number to a string to get each digit.
   2. **Step 2:** Calculate the number of digits in the number.
  3. **Step 3:** Compute the sum of each digit raised to the power of the number of digits.
  4. **Step 4:** Compare this sum with the original number.

If the sum is equal to the original number, then it is an Armstrong number.

### Pseudo Code

```python
def isArmstrongNumber(number):
    # Convert the number to a string to easily iterate through digits
    num_str = str(number)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum of powers is equal to the original number
    return "Armstrong Number" if sum_of_powers == number else "Not Armstrong Number"
```

### Example

**Input:** `153`

1. **Convert 153 to string:** "153"
2. **Number of digits:** 3
3. **Sum of digits each raised to the power of 3:** \(1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153\)
4. **Compare sum with original number:** 153 equals 153

**Output:** 

```text
Armstrong Number
```

### Time Complexity

`O(d)` - The time complexity is linear with respect to the number of digits \(d\) because we process each digit.

### Space Complexity

`O(d)` - The space complexity is linear due to the space required to store the string representation of the number and to perform the calculations.

### Alternative Solution

You can also use the `math` library for a more straightforward implementation with the `pow` function. Explore this built-in method on your own.

### For a clearer understanding, try writing out the code and executing it yourself—it’s a helpful way to grasp the concepts! Consider also creating a flowchart for better visualization, as it can be very helpful.