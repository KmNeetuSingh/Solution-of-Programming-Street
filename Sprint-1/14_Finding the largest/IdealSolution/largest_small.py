a = [1,3,23,4,54]
largest = a[0]
smallest = a[0]
for num in a :
    if num >largest:
        largest=num 
    if num < smallest:
        smallest=num
print("largest",largest)
print("smallest",smallest)