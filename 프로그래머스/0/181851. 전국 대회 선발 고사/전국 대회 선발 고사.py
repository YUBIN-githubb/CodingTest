def solution(rank, attendance):
    ranking = []
    for (index, rank), b in zip(enumerate(rank), attendance):
        if b == True:
            ranking.append({'rank' : rank, 'index' : index})
    ranking.sort(key=lambda x: x['rank'])
    return 10000*ranking[0]['index'] + 100*ranking[1]['index'] + ranking[2]['index']