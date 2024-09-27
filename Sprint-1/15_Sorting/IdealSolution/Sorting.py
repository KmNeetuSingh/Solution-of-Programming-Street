a = [1,2,3,4,5,9]
for s in range(len(a)):
    for t in range(s+1,len(a)):
        if a[s] > a[t]:
            a[s], a[t] = a[t], a[s]
print(a)