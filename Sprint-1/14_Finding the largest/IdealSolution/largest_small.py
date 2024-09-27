arr = [1,2,4,5,7,8,9]
largest= arr[0]
smallest= arr[0]
for num in arr :
    if num > largest:
        largest = num 
    if num < smallest:
        smallest= num
print("largest:",largest)
print("smallest:",smallest)