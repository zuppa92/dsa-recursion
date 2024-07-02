def is_simple_square(square):
    """Check if the square is a simple square (0 or 1)."""
    return square in [0, 1]

def simplify(square):
    """Simplify the square/split square."""
    if is_simple_square(square):
        return square
    
    simplified = [simplify(sub_square) for sub_square in square]
    
    if all(s == simplified[0] for s in simplified):
        return simplified[0]
    
    return simplified

# Example usage
if __name__ == "__main__":
    print(simplify(0))  # 0
    print(simplify(1))  # 1
    print(simplify([1, 1, 1, 1]))  # 1
    print(simplify([0, 0, 0, 0]))  # 0
    print(simplify([1, 0, 1, 0]))  # [1, 0, 1, 0]
    print(simplify([1, 0, 1, [1, 1, 1, 1]]))  # [1, 0, 1, 1]
    print(simplify([1, 1, 1, [1, 1, 1, 1]]))  # 1
    print(simplify([[1, 1, 1, 1], [1, 1, 1, 1], 1, 1]))  # 1
    print(simplify([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1]))  # [1, 0, [1, 0, 1, 1], 1]
