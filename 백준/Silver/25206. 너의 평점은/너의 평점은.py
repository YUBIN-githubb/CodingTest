import sys

sum = 0
gpa = 0

score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

for _ in range(20):
    line = sys.stdin.readline().split()

    if line[2] != "P":  
        sum += score[line[2]] * float(line[1])
        gpa += float(line[1])

print(sum/gpa)
