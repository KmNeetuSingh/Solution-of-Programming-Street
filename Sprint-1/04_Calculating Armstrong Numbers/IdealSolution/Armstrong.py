def checkArmstrong(N):
    S = str(N)
    D = len(S)
    Arms = 0
    for i in S :
        Arms += int(i) ** D
    if Arms == N:
        return "Armstrong Number"
    else :
        return"Not a Armstrong Number"
print(checkArmstrong(153))