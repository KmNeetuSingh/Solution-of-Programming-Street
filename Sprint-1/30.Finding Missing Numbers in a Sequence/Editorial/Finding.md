# Finding Missing Numbers in a Sequence

## Difficulty: Easy

## Topics: Basic Programming, Arrays

### Problem Description

Write a program to find the missing numbers in a sequence from `1` to `n`, where `n` is the maximum number in the provided sequence.

### Input

- An array `sequence` containing integers. The sequence may contain numbers from `1` to `n`, but some numbers might be missing.

### Output

- A list of missing numbers from `1` to `n`.

### Example

**Input:**  
`sequence = [1, 2, 4, 6, 7, 9]`

**Output:**  
`[3, 5, 8]`  
**Explanation:** The numbers `3`, `5`, and `8` are missing from the sequence.

### Approach

1. **Determine the Range**: Identify the maximum number `n` in the sequence to establish the range for checking missing numbers.
2. **Create an Array to Track Numbers**: Initialize an array `present` of size `n + 1` to keep track of which numbers are present in the input sequence.
3. **Mark Present Numbers**: Iterate through the input sequence and use each value as an index to mark the corresponding position in the `present` array.
4. **Identify Missing Numbers**: Iterate through the `present` array and collect the indices that remain unmarked (indicating those numbers are missing from the sequence).
5. **Return the Result**: Output the list of missing numbers.

### Sample Code

```python
def findmissing(s):
    n = 0
    for num in s:
        if num > n:
            n = num
    
    # Step 2: Create an array to track present numbers
    present = [0] * (n + 1)  # Initialize with zeros
    
    # Step 3: Mark present numbers
    for num in s:
        if 1 <= num <= n:  # Ensure the number is within range
            present[num] = 1  # Marking the number as present

    # Step 4: Identify missing numbers
    missing_numbers = []
    for i in range(1, n + 1):
        if present[i] == 0:  # If the number is not present
            missing_numbers.append(i)

    return missing_numbers

# Example usage
seq = [1, 2, 4, 6, 7, 9]
missing = findmissing(seq)
print(missing)  
```

### Complexity

- **Time Complexity**: O(n), where `n` is the maximum number in the sequence, due to the iterations through the input and the tracking array.
- **Space Complexity**: O(n) for the `present` array used to track which numbers are present.

### Constraints

- The input array may contain duplicates or numbers outside the range `1` to `n`, but the program will only consider numbers from `1` to `n` when determining missing numbers.