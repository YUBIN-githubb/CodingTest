def solution(n):
    #우->하->좌->상
    dx = [0,1,0,-1] #행
    dy = [1,0,-1,0] #열
    
    # 0으로 초기화
    answer = [ [0]*n for _ in range(0,n)]
    
    
    r = 0 #행
    c = 0 #열
    direction = 0
    
    for i in range(1, n*n+1):
        answer[r][c] = i
        
        nr = r + dx[direction]
        nc = c + dy[direction]
        
        if nr<0 or nr>=n or nc<0 or nc>=n or answer[nr][nc] != 0:
            direction = (direction+1)%4
            nr = r + dx[direction]
            nc = c + dy[direction]
        r = nr
        c = nc
        
    return answer