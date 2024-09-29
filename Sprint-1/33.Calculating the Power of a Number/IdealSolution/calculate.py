def calculatePower(b, e):
    res = 1
    
    
    if e> 0:
        for _ in range(e):
            res *= b

    elif e < 0:
        for _ in range(abs(e)):
            res *= b
        res = 1 / res  

    elif e == 0:
        res = 1

    print (res)

calculatePower(2,4)