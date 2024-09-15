Here's an editorial-style solution for the star pattern problem, formatted according to your preferences:

---

**Crafting Star Patterns**  
**Difficulty**: Easy  
**Topics**: Basic Programming, Patterns  

### Problem Statement
Write a program to create different star patterns (e.g., pyramid, diamond).  
- Input: `patternType = "pyramid"`, `height = 5`  
- Output:
```
    *
   ***
  *****
 *******
*********
```

### Short Observations
- We need to generate a **pyramid pattern** based on the given height.
- Each row will contain an increasing number of stars (`*`), and they must be centered.

### Detailed Observations
- The number of stars in each row follows the pattern of odd numbers (1, 3, 5, 7, ...).
- The stars must be aligned in the center. This requires adjusting spaces on the left side of the stars.
- For a row `i` (where `i` starts from 1), the number of stars is `2*i - 1`.
- The number of leading spaces for row `i` is `height - i`.

### Pseudocode
1. Loop through `i` from 1 to `height`.
2. Calculate the number of spaces (`height - i`).
3. Calculate the number of stars (`2*i - 1`).
4. Print the spaces followed by stars.

### Example
For `patternType = "pyramid"` and `height = 5`, the pattern is generated as follows:
- Row 1: `4 spaces + 1 star`
- Row 2: `3 spaces + 3 stars`
- Row 3: `2 spaces + 5 stars`
- Row 4: `1 space  + 7 stars`
- Row 5: `0 spaces + 9 stars`

Output:
```
    *
   ***
  *****
 *******
*********
```

### Time and Space Complexity
- **Time Complexity**: O(n) where `n` is the number of rows (height of the pyramid).
- **Space Complexity**: O(1), since we are only using a few variables.

### Alternate Solutions
- You could also generate other patterns (e.g., diamond, inverted pyramid) by tweaking the conditions for spaces and stars accordingly.

