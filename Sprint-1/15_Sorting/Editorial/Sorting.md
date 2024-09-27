# Sorting an Array 🧮

## Difficulty: Easy  
**Topics**: Basic Programming, Sorting Algorithms  

## Description 📝  
This is a classic problem where you need to write a program that takes in an array of numbers and sorts them in ascending order. Pretty straightforward, right? 😎

## Problem Statement 💡  
Given an array of numbers, sort them in **ascending order**.

### Example:  
- **Input**:  
  ```  
  array = [3, 1, 4, 1, 5, 9]  
  ```  

- **Output**:  
  ```  
  [1, 1, 3, 4, 5, 9]  
  ```  

- **Explanation**:  
  The sorted array in ascending order is `[1, 1, 3, 4, 5, 9]`.

## Python Pseudocode 🐍

Here’s the pseudocode using Python-like syntax for sorting an array:

```python
def sort_array(arr):
    # Step 1: Loop through the array
    for i in range(len(arr)):
        # Step 2: Find the minimum element in the unsorted part
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                # Step 3: Swap the found minimum element with the first element
                arr[i], arr[j] = arr[j], arr[i]
    return arr
```

- **Explanation**:
  - We are looping through the array to find the smallest element in the unsorted portion.
  - Once found, it swaps the smallest element with the current element at index `i`.
  - The process continues until the array is fully sorted.

## How to Solve 🚀  
1. Input the array.
2. Implement the sorting logic using the above pseudocode.
3. Return the sorted array.

## Constraints 🔐  
- The array can contain both positive and negative integers.
- Duplicate numbers are allowed.

## Example Walkthrough 🌟  
Given `array = [3, 1, 4, 1, 5, 9]`:

- Step 1: Start with `[3, 1, 4, 1, 5, 9]`.
- Step 2: After sorting, you get `[1, 1, 3, 4, 5, 9]`.  

Boom 💥, you're done!

## Built With ⚙️  
- Python, JavaScript, or any language of your choice! 🌍

## Fun Fact 🧠  
Sorting algorithms like **QuickSort** and **MergeSort** are some of the fastest algorithms out there. Sorting is used literally everywhere—from ranking your favorite songs to organizing files on your computer. 🔥