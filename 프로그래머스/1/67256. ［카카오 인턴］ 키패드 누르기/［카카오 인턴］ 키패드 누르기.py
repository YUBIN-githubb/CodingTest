def solution(numbers, hand):
    answer = ""
    
    keyboard = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    
    pos = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2),
        "*" : (3,0),
        0 : (3,1),
        "#" : (3,2)
    }
    
    left = pos["*"]
    right = pos["#"]
    
    
    for i in range (0,len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            if numbers[i] == 1:
                left = pos[1]
            if numbers[i] == 4:
                left = pos[4]
            if numbers[i] == 7:
                left = pos[7]
            answer += "L"
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            if numbers[i] == 3:
                right = pos[3]
            if numbers[i] == 6:
                right = pos[6]
            if numbers[i] == 9:
                right = pos[9]
            answer += "R"
        elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0:
            if numbers[i] == 2:
                goal = pos[2]
                left_dis = abs(goal[0] - left[0]) + abs(goal[1] - left[1])
                right_dis = abs(goal[0] - right[0]) + abs(goal[1] - right[1])
                
                print(left_dis)
                print(right_dis)
                if left_dis < right_dis:
                    answer += "L"
                    left = pos[2]
                elif left_dis > right_dis:
                    answer += "R"
                    right = pos[2]
                else:
                    if hand == "right":
                        answer += "R"
                        right = pos[2]
                    else:
                        answer += "L"
                        left = pos[2]
            
            if numbers[i] == 5:
                goal = pos[5]
                left_dis = abs(goal[0] - left[0]) + abs(goal[1] - left[1])
                right_dis = abs(goal[0] - right[0]) + abs(goal[1] - right[1])
                
                print(left_dis)
                print(right_dis)
                if left_dis < right_dis:
                    answer += "L"
                    left = pos[5]
                elif left_dis > right_dis:
                    answer += "R"
                    right = pos[5]
                else:
                    if hand == "right":
                        answer += "R"
                        right = pos[5]
                    else:
                        answer += "L"
                        left = pos[5]
                        
            if numbers[i] == 8:
                goal = pos[8]
                left_dis = abs(goal[0] - left[0]) + abs(goal[1] - left[1])
                right_dis = abs(goal[0] - right[0]) + abs(goal[1] - right[1])
                
                print(left_dis)
                print(right_dis)
                if left_dis < right_dis:
                    answer += "L"
                    left = pos[8]
                elif left_dis > right_dis:
                    answer += "R"
                    right = pos[8]
                else:
                    if hand == "right":
                        answer += "R"
                        right = pos[8]
                    else:
                        answer += "L"
                        left = pos[8]
                        
            if numbers[i] == 0:
                goal = pos[0]
                left_dis = abs(goal[0] - left[0]) + abs(goal[1] - left[1])
                right_dis = abs(goal[0] - right[0]) + abs(goal[1] - right[1])
                
                print(left_dis)
                print(right_dis)
                if left_dis < right_dis:
                    answer += "L"
                    left = pos[0]
                elif left_dis > right_dis:
                    answer += "R"
                    right = pos[0]
                else:
                    if hand == "right":
                        answer += "R"
                        right = pos[0]
                    else:
                        answer += "L"
                        left = pos[0]

    return answer