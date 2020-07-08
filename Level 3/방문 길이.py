#https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    road = [[[0,0] for _ in range(11)] for _ in range(11)]
    idx = 0; idy = 0
    for dir in dirs:
        if dir == "U" and idx > -5: idx -= 1; road[idx+5][idy+5][0] = 1
        elif dir == "D" and idx < 5: idx += 1; road[idx+4][idy+5][0] = 1
        elif dir == "L" and idy > -5: idy -= 1; road[idx+5][idy+5][1] = 1
        elif dir == "R" and idy < 5: idy += 1; road[idx+5][idy+4][1] = 1

    answer = 0
    for i in road:
        for j in i:
            answer += j.count(1)
    return answer

dirs = "UUUUUUUU"
print(solution(dirs))
