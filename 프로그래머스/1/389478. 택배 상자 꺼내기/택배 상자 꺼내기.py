def solution(n, w, num):
    answer = 0
    h = n//w +1
    x = 1
    storage = []
    
    for i in range (0,h):
        t = []
        for j in range (0,w):
            if x <= n:
                t.append(x)
                x+=1
            else:
                t.append(0)
        if i%2 == 0:
            storage.append(t)
        else:
            t.reverse()
            storage.append(t)
            
    for i in range (0,len(storage)):
        for j in range (0,len(storage[i])):
            if storage[i][j] == num:
                d = i
                while d < h and storage[d][j] != 0:
                    answer += 1
                    d += 1
    return answer