def palinDrome(input):
    s = str(input)
    rev = s[::-1]
    if s == rev:
        return "Is a Palindrome"
    else:
        return "Not a Palindrome"

# Example usage
print(palinDrome("radar"))
print(palinDrome(121))      
print(palinDrome("Shrity"))