# **Finding the Median of an Array**
## **Difficulty**: Medium  
**Topics**: Arrays, Sorting
### **Description**  
This program calculates the median of an array of numbers. The median is the middle value in a sorted array of numbers. If the array has an odd number of elements, the median is the middle element. If the array has an even number of elements, the median is the average of the two middle elements.

### **Example**  
**Input**:  
```  
array = [3, 1, 2, 4, 5]
```  
**Output**:  
```  
3  
```  
**Explanation**:  
The sorted array is `[1, 2, 3, 4, 5]`. Since the number of elements is odd, the median is the middle value, which is `3`.

### **Steps to Run the Project**

1. **Clone the repository**:  
   Clone this repository to your local machine using the following command:  
   ```bash
   git clone https://github.com/yourusername/median-finder.git
   ```

2. **Install dependencies**:  
   If the project has any dependencies, install them using `npm`, `pip`, or the appropriate package manager.

3. **Run the script**:  
   After installation, run the program using the following command:
   ```bash
   python median_finder.py
   ```
   Ensure that you have Python installed on your machine.

4. **Test with Custom Inputs**:  
   To test with custom inputs, you can modify the `array` variable in the script or create a simple input mechanism to pass arrays dynamically.

### **Code Overview**

1. **Input**:  
   Accept an array of numbers as input.

2. **Process**:  
   - Sort the array in ascending order.
   - If the array length is odd, return the middle element as the median.
   - If the array length is even, return the average of the two middle elements as the median.

3. **Output**:  
   The program will output the median value of the array.

### **Pseudo Code**:
```python
function findMedian(array):
    sort(array)
    length = len(array)
    
    if length % 2 != 0:
        return array[length // 2]
    else:
        middle1 = array[length // 2]
        middle2 = array[(length // 2) - 1]
        return (middle1 + middle2) / 2
```

### **Example Execution**

**Input**:  
```python
array = [3, 1, 2, 4, 5]
```

**Output**:  
```python
Median: 3
```

### **Time Complexity**:  
- Sorting the array takes `O(n log n)` time, where `n` is the length of the array.  
- Finding the median after sorting takes `O(1)` time.  
- Therefore, the overall time complexity is `O(n log n)`.

### **Space Complexity**:  
- The space complexity is `O(1)` if the sorting is done in place, or `O(n)` if a new sorted array is created.

### **Further Enhancements**
- The current implementation uses sorting to find the median, which is efficient for small to medium-sized arrays. For larger datasets, other algorithms like the "Median of Medians" can be implemented to find the median in `O(n)` time without sorting the entire array.

