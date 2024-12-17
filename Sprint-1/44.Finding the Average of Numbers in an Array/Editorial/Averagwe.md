# **Finding the Average of Numbers in an Array**

**Difficulty**: Easy  
**Topics**: Arrays, Mathematical Computations

## **Description**  
This program calculates the average of numbers in an array. It takes an array of integers as input and returns the average of the numbers. If the array is empty, it returns `0`.

## **Example**

### Input:
```python
numbers = [1, 2, 3, 4, 5]
```

### Output:
```python
Average: 3
```

### Explanation:  
The sum of the numbers is 1 + 2 + 3 + 4 + 5 = 15, and the average is 15 / 5 = 3.

## **Code**:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Average:", calculate_average(numbers))  # Output: Average: 3
```

## **Time Complexity**:  
`O(n)` — where `n` is the number of elements in the array. The time complexity is due to the summation of the elements.

## **Space Complexity**:  
`O(1)` — The space complexity is constant as only a few variables are used.

