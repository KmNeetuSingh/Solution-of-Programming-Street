def perfectNum(N):
    if N < 0 :
        return False
    for i in range (int(N ** 0.5 )+1):
        if i*i == N:
            return True
        
    return False
print (perfectNum(16))