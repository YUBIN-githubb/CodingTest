def solution(board, h, w):
    colors = []
    center = board[h][w]
    
    if (h-1) >= 0:
        up = board[h-1][w]
        colors.append(up)
    if h+1 < len(board):
        down = board[h+1][w]  
        colors.append(down)
    if w-1 >= 0:        
        left = board[h][w-1]
        colors.append(left)
    if w+1 < len(board[0]):
        right = board[h][w+1]
        colors.append(right)
    
    return colors.count(center)
