# Static Method
s = "hello"
print(s[::-1])  # Here we use its built-in method slicing

# Brute Force Approach
# Simple brute force approach to reverse a string
s = "Learner"
reversed_str = ''
for i in range(len(s) - 1, -1, -1):
    reversed_str += s[i]
print(reversed_str)

"""Dynamic Method:
Here’s the lowdown: we’re wrapping our logic in a function, which means we can call it anytime we need, like our personal coding assistant. 
This is the core of function mechanics: create it once and reuse it whenever it fits. 
How cool is that? Plus, it keeps our code super organized and totally reusable. Win-win!
"""
def reversed_str(s):
    return s[::-1]

print(reversed_str("hustler"))  
