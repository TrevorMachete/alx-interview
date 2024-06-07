import math

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascal_triangle(n):
    if n <= 0:
        return []

    result = []
    for count in range(n):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)

    return result
for row in pascal_triangle(5):
    print(row)
