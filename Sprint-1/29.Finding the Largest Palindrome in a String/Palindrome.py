def is_palindrome(s):
    return s == s[::-1]  

def find_largest_palindrome(s):
    max_length = 0
    largest_palindrome = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1): 
            sub = s[i:j]
            if is_palindrome(sub):
                if len(sub) > max_length:
                    max_length = len(sub)
                    largest_palindrome = sub

    print(largest_palindrome)

# Example usage
find_largest_palindrome("bbda")  
