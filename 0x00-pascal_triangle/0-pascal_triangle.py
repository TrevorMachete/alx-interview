def pascal_triangle(n):
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]]

    # Generate the rest of the triangle
    for i in range(1, n):
        row = [1]  # First element of a row is always 1
        last_row = triangle[i - 1]
        for j in range(1, i):  # Each element is the sum of the two elements above it
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)  # Last element of a row is always 1
        triangle.append(row)

    return triangle

# Test the function
print(pascal_triangle(5))
