def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []
    
    # Initialize the result list with the first row [1]
    result = [[1]]
    
    # Generate the rest of the rows
    for i in range(1, n):
        # Each new row starts with 1
        new_row = [1]
        
        # Each element in the row (except the first and last) is the sum of the two elements above it
        for j in range(1, i):
            new_row.append(result[i-1][j-1] + result[i-1][j])
        
        # The last element of the row is also 1
        new_row.append(1)
        
        # Add the new row to the result
        result.append(new_row)
    
    return result
