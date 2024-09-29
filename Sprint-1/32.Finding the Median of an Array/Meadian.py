def find_median(a):
    a.sort()
    if len((a)) % 2 == 1:  
        median = a[len ((a))// 2]
    else: 
        mid1 = len // 2
        mid2 = mid1 - 1
        median = (a[mid1] + a[mid2]) / 2
    print (median)
array = [3, 1, 2, 4, 5]
find_median(array)    