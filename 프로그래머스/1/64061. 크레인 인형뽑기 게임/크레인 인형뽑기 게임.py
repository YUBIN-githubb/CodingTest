def solution(board, moves):
    
    basket = [0]
    answer = 0
    
    for i in range (0,len(moves)):
        index = moves[i]
        print(index)
        for j in range (0,len(board)):
            if board[j][index-1] != 0:
                if basket[-1] == board[j][index-1]:
                    
                    answer += 2
                    basket.pop()
                    board[j][index-1] = 0
                    break
                else:
                    basket.append(board[j][index-1])
                    board[j][index-1] = 0
                    break
                    
                    
    
    return answer