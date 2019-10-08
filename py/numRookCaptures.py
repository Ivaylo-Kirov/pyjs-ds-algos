

def numRookCaptures(board):
    result = 0

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                startPosY = i
                startPosX = j
    
    # based off of the location now I go through each row and column and check if I can make a move
    # there will always be only 2 - board[startPosY][0-7] and board[0-7][starPosX]
    # if I see a pawn on my way, take it and increment result

    # row
    eCap = False
    wCap = False
    for k in range(0, 8):
        if board[startPosY][k] == 'p':
            if k < startPosX and wCap != True:
                invalidMove = False
                for b in range(k+1, startPosX):
                    if board[startPosY][b] == 'B':
                        invalidMove = True
                if not invalidMove:
                    result += 1
                    wCap = True
            if k > startPosX and eCap != True:
                invalidMove = False
                for b in range(startPosX+1, k):
                    if board[startPosY][b] == 'B':
                        invalidMove = True
                if not invalidMove:
                    result += 1
                    eCap = True
    
    # column
    nCap = False
    sCap = False
    for k in range(0, 8):
        if board[k][startPosX] == 'p':
            if k < startPosY and nCap != True:
                invalidMove = False
                for b in range(k+1, startPosY):
                    if board[b][startPosX] == 'B':
                        invalidMove = True
                if not invalidMove:
                    result += 1
                    nCap = True
            if k > startPosY and sCap != True:
                invalidMove = False
                # is there a B there?
                for b in range(startPosY+1, k):
                    if board[b][startPosX] == 'B':
                        invalidMove = True
                if not invalidMove:
                    result += 1
                    sCap = True

    return result

result = numRookCaptures([[".",".",".",".",".",".",".","."],
                          [".",".","B","B","B","B","B","."],
                          [".","p","B","p","p","p","B","p"],
                          [".","p","B","p","R","p","B","p"],
                          [".","p","B","p","p","p","B","p"],
                          [".",".","B","B","B","B","B","."],
                          [".",".",".","p","p","p",".","."],
                          [".",".",".",".",".",".",".","."]])
print('hi')