# Step 1: Represent the board
# A Sudoku board is a 9x9 list of lists, where each element is a character '1'-'9' or '.'
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            # Row check
            if board[i][j] != '.':
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

            # Column check
            if board[j][i] != '.':
                if board[j][i] in col:
                    return False
                col.add(board[j][i])

            # Box check
            r = 3 * (i // 3) + j // 3
            c = 3 * (i % 3) + j % 3
            if board[r][c] != '.':
                if board[r][c] in box:
                    return False
                box.add(board[r][c])
    return True

# Step 2: Validate row
def is_valid_row(board, row):
    seen = set()
    for num in board[row]:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

# Step 3: Validate column
def is_valid_col(board, col):
    seen = set()
    for i in range(9):
        num = board[i][col]
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True

# Step 4: Validate 3x3 box
def is_valid_box(board, start_row, start_col):
    seen = set()
    for i in range(3):
        for j in range(3):
            num = board[start_row + i][start_col + j]
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
    return True

# Step 5: Combine all checks
def is_valid_sudoku(board):
    for i in range(9):
        if not is_valid_row(board, i) or not is_valid_col(board, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_box(board, i, j):
                return False

    return True
if is_valid_sudoku(board):
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is NOT valid.")