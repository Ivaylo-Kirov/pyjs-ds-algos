
function numRookCaptures(board) {

    let result = 0
    let startPosY = 0;
    let startPosX = 0;
    let invalidMove = false;
    for (let i = 0; i < board[0].length; ++i) {
        for (let j = 0; j < board[0].length; ++j) {
            if (board[i][j] == 'R') {
                startPosY = i;
                startPosX = j;
            }
        }
    }
    
    // based off of the location now I go through each row and column and check if I can make a move
    // there will always be only 2 - board[startPosY][0-7] and board[0-7][starPosX]
    // if I see a pawn on my way, take it and increment result

    // row
    let eCap = false
    let wCap = false
    for (let k = 0; k < 8; ++k) {
        if (board[startPosY][k] == 'p') {
            if (k < startPosX && wCap != true) {
                invalidMove = false
                for (let b = k+1; b < startPosX; ++b) {
                    if (board[startPosY][b] == 'B') {
                        invalidMove = true
                    }
                }
                if (!invalidMove) {
                    result++;
                    wCap = true
                }
            }
        
            if (k > startPosX && eCap != true) {
                invalidMove = false
                for (let b = startPosX+1; b < k; ++b) {
                    if (board[startPosY][b] == 'B') {
                        invalidMove = true
                    }
                }
                if (!invalidMove) {
                    result++;
                    eCap = true
                }
            }
        }
    }
    // column
    let nCap = false
    let sCap = false
    for (let k = 0; k < 8; ++k) {
        if (board[k][startPosX] == 'p') {
            if (k < startPosY && nCap != true) {
                invalidMove = false
                for (let b = k+1; b < startPosY; ++b) {
                    if (board[b][startPosX] == 'B') {
                        invalidMove = true
                    }
                }
                if (!invalidMove) {
                    result++;
                    nCap = true
                }
            }

            if (k > startPosY && sCap != true) {
                invalidMove = false
                // is there a B there?
                for (let b = startPosY+1; b < k; ++b) {
                    if (board[b][startPosX] == 'B') {
                        invalidMove = true
                    }
                }
                if (!invalidMove) {
                    result++;
                    sCap = true
                }
            }

        }
    }

    return result

}

const result = numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]);