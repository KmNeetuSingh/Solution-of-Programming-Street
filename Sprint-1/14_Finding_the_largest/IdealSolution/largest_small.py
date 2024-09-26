arr = [1,5,3,2,5,]
largest=arr[0]
smallest= arr[0]
for num in arr :
    if num > largest:
        largest=num
    if num < smallest:
        smallest= num
print("Largest in array is :",largest)
print("Smallest in array is :",smallest)