def isValidSudoku(board):
    # Check rows
    for i in range(9):
        row = set()
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

    # Check columns
    for j in range(9):
        col = set()
        for i in range(9):
            if board[i][j] != ".":
                if board[i][j] in col:
                    return False
                col.add(board[i][j])

    # Check sub-boxes
    for box in range(9):
        sub_box = set()
        for i in range(box // 3 * 3, box // 3 * 3 + 3):
            for j in range(box % 3 * 3, box % 3 * 3 + 3):
                if board[i][j] != ".":
                    if board[i][j] in sub_box:
                        return False
                    sub_box.add(board[i][j])

    return True
