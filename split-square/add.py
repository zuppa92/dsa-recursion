def is_simple_square(square):
    """Check if the square is a simple square (0 or 1)."""
    return square in [0, 1]

def add(square1, square2):
    """Add two squares together according to the rules."""
    if is_simple_square(square1) and is_simple_square(square2):
        return max(square1, square2)
    
    if is_simple_square(square1):
        if square1 == 1:
            return 1
        else:
            return square2
    
    if is_simple_square(square2):
        if square2 == 1:
            return 1
        else:
            return square1
    
    return [
        add(square1[0], square2[0]),
        add(square1[1], square2[1]),
        add(square1[2], square2[2]),
        add(square1[3], square2[3])
    ]

# Example usage
if __name__ == "__main__":
    s1 = 0
    s2 = 1
    print(add(s1, s2))  # 1

    s1 = 0
    s2 = [1, 0, 1, 0]
    print(add(s1, s2))  # [1, 0, 1, 0]

    s1 = [0, 0, 0, 1]
    s2 = [0, 1, 0, 1]
    print(add(s1, s2))  # [0, 1, 0, 1]

    s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]
    print(add(s1, s2))  # [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    s1 = [0, [1, 1, 1, 0], [0, 0, 0, 0], 1]
    s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]
    print(add(s1, s2))  # [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    s1 = [0, [1, 1, 1, 1], [0, 0, 0, 0], 1]
    s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]
    print(add(s1, s2))  # [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
