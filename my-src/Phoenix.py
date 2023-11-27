def phoenix_Count(coordinate):
    max_iterations = 115
    z = 0
    for i in range(max_iterations):
        z = z * z + coordinate
        if abs(z) > 2:
            return i
    return max_iterations