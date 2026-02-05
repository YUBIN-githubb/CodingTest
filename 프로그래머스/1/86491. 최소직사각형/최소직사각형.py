def solution(sizes):
    for i in range (0,len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            big = sizes[i][1]
            small = sizes[i][0]
            sizes[i][0] = big
            sizes[i][1] = small
    w = []
    h = []
    for i in range (0,len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    return max(w) * max(h)