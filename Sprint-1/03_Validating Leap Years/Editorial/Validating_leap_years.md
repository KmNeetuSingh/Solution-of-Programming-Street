### Validating Leap Years 

### Difficulty: Easy

### Prerequisite: Basic Understanding of Calendar Years

---

### Hint

A leap year is determined by specific rules related to divisibility by 4, 100, and 400.

### Short Observations

- To identify a leap year:
  - The year must be divisible by 4.
  - If divisible by 100, it must also be divisible by 400 to qualify as a leap year.

### Detailed Observations

- **Patterns for Leap Years:**
  1. **Observation 1:** Years divisible by 400 are always leap years. (e.g., 2000, 2400)
  2. **Observation 2:** Years divisible by 100 but not by 400 are not leap years. (e.g., 1800, 1900)
  3. **Observation 3:** Years divisible by 4 but not by 100 are leap years. (e.g., 2020, 2024)
  4. **Observation 4:** Years not divisible by 4 are not leap years. (e.g., 2019, 2021)

- These observations align with the Gregorian calendar’s rules, which adjust the average length of the year to account for an extra day every four years.

### Pseudo Code

```python
def isLeapYear(year):
    if year % 400 == 0:
        return "Leap"
    elif year % 100 == 0:
        return "Not Leap"
    elif year % 4 == 0:
        return "Leap"
    else:
        return "Not Leap"
```

### Example

**Input:** `2020`

1. **Observation:** 2020 is not divisible by 400.
2. **Observation:** 2020 is not divisible by 100.
3. **Observation:** 2020 is divisible by 4.

**Output:** 

```text
Leap
```

### Time Complexity

`O(1)` - The time complexity remains constant due to a fixed number of arithmetic operations.

### Space Complexity

`O(1)` - The space complexity is constant as no additional storage is needed beyond a few variables.

### Alternate Solution

Consider using built-in libraries for date and time operations available in various programming languages for a simpler and potentially more efficient solution.
