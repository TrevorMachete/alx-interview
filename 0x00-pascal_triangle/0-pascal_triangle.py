def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)
        triangle.append(row)
    return triangle

# Example usage
n = 5  # Change this value as needed
result = pascal_triangle(n)
print(result)
