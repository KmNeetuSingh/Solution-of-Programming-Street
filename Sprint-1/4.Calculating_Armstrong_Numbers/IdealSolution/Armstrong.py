def armStrong(number):
    num_str = str(number)
    num_digits = len(num_str)  
    sum = 0  
    for digit in num_str:
        sum += int(digit) ** num_digits
    if sum == number:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"

# Example Usage...
number = 123  # Static example
print(armStrong(number))
