i = [1, 500]
armStrong= []
for num in range(i[0], i[1] + 1):
    s = str(num)
    power = len(s)  
    total_sum = sum(int(digit) ** power for digit in s)  
    if total_sum == num:
        armStrong.append(num)  
print(armStrong)
