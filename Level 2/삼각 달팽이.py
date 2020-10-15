# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    lst = [[0]*n for _ in range(n)]

    for i in range(n):
        lst[i][0] = i+1

    for i in range(n):
        lst[-1][i] = n + i

    pos = (n-1,n-1)
    dir = (-1,-1)

    for i in range(2*n,n*(n+1)//2 + 1):
        if lst[pos[0]+dir[0]][pos[1]+dir[1]] != 0:
            if dir == (-1,-1):
                dir = (1,0)
            elif dir == (1,0):
                dir = (0,1)
            else:
                dir = (-1,-1)
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        lst[pos[0]][pos[1]] = i

    answer = []
    for i,v in enumerate(lst):
        answer += v[:i+1]
    return answer

print(solution(5))
