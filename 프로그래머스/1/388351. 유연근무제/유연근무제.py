def solution(schedules, timelogs, startday):
    member = [0]*len(schedules)
    answer = 0
    week = []
    schedule = []
    for i in range (0,7):
        week.append((startday + i -1) % 7 + 1)

    for i in range (0,len(schedules)):
        hour = (schedules[i]//100)*60
        minute = (schedules[i]%100)
        h = (hour + minute + 10)//60
        m = (hour + minute + 10)%60
        schedule.append((schedules[i], h*100 + m))
        
    for i in range (0,len(week)):
        if week[i] == 6 or week[i] == 7:
            continue
        else:
            for j in range(0,len(schedules)):
                if timelogs[j][i] > schedule[j][1]:
                    member[j] += 1
    return member.count(0)