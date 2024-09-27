i = [1, 500]
arm = []
for num in range(i[0], i[1] + 1):
    s = str(num)
    power = len(s)  
    total_sum = sum(int(digit) ** power for digit in s)  # we are using hte built in function sum() ot add up all the value
    if total_sum == num:
        arm.append(num)  
print(arm)
