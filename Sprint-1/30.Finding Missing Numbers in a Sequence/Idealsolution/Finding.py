def find_missing_numbers(s):
    if not s:
        return []

    n = max(s)
    p = [0] * (n + 1)

    for num in s:
        if 1 <= num <= n:
            p[num] = 1  

    missing = []
    for i in range(1, n + 1):
        if p[i] == 0:
            missing.append(i)

    print (missing)

# Example usage
s = [1,2,23]
find_missing_numbers(s)