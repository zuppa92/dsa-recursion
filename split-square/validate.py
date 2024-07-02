def is_valid_square(square):
    """Validate if the given square/split square is valid."""
    if isinstance(square, int):
        return square in [0, 1]
    if isinstance(square, list) and len(square) == 4:
        return all(is_valid_square(sub_square) for sub_square in square)
    return False

# Example usage
if __name__ == "__main__":
    print(is_valid_square(0))  # True
    print(is_valid_square(1))  # True
    print(is_valid_square([1, 1, 1, 1]))  # True
    print(is_valid_square([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1]))  # True
    print(is_valid_square([1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]))  # True
    print(is_valid_square(2))  # False
    print(is_valid_square([1, 1, 1, 1, 1]))  # False
    print(is_valid_square([1, 0, [1, [0, 0, 0, 0, 1], 1, [1, 1, 1, 1]], 1]))  # False
    print(is_valid_square([1, [1, 0, 1, [0, [0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]))  # False
