def matrix(s):
    m= [[(i * s + j + 1) for j in range(s)] for i in range(s)]
    
    for row in m:
        print(" ".join(map(str, row)))

# Example usage
matrix(5)
