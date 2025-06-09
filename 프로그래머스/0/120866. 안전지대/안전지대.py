def solution(board):
    directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),  (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
    for i in range (0,len(board)):
        for j in range (0,len(board)):
            if board[i][j] == 1:
                for dx, dy in directions:
                    if 0 <= dy+i and len(board) > dy+i and 0 <= dx+j and len(board) > dx+j:
                        if board[dy+i][dx+j] == 1:
                            continue
                        else:
                            board[dy+i][dx+j] = 2
    result = 0
    for i in board:
        result += i.count(0)
    return result

