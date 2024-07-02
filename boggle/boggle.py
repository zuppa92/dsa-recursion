def make_board(board_string):
    board = []
    rows = board_string.strip().split('\n')
    for row in rows:
        board.append(row.strip().split())
    return board

def is_valid_move(board, x, y, visited):
    return 0 <= x < 5 and 0 <= y < 5 and (x, y) not in visited

def search_word(board, word, index, x, y, visited):
    if index == len(word):
        return True

    if not is_valid_move(board, x, y, visited):
        return False

    if board[x][y] != word[index]:
        return False

    visited.add((x, y))

    # Move in NEWS directions
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if search_word(board, word, index + 1, x + dx, y + dy, visited):
            return True

    visited.remove((x, y))
    return False

def find(board, word):
    for x in range(5):
        for y in range(5):
            if search_word(board, word, 0, x, y, set()):
                return True
    return False

# Example usage
board_string = """
N C A N E
O U I O P
Z Q Z O N
F A D P L
E D E A Z
"""

board = make_board(board_string)

print(find(board, "NOON"))  # True
print(find(board, "NOPE"))  # True
print(find(board, "CANON"))  # False
print(find(board, "QUINE"))  # False
print(find(board, "FADED"))  # True
