# https://programmers.co.kr/learn/courses/30/lessons/1844

import queue
def solution(maps):
    dp = [[-1]*len(maps[0]) for _ in range(len(maps))]
    q = queue.Queue()
    dp[0][0] = 1
    q.put((0,0))
    while q.qsize():
        x,y = q.get()
        if x > 0 and maps[x-1][y] == 1 and dp[x-1][y] == -1:
            dp[x-1][y] = dp[x][y] + 1
            q.put((x-1,y))
        if x + 1 < len(maps) and maps[x+1][y] == 1 and dp[x+1][y] == -1:
            dp[x+1][y] = dp[x][y] + 1
            q.put((x+1,y))
        if y > 0 and maps[x][y-1] == 1 and dp[x][y-1] == -1:
            dp[x][y-1] = dp[x][y] + 1
            q.put((x,y-1))
        if y + 1 < len(maps[0]) and maps[x][y+1] == 1 and dp[x][y+1] == -1:
            dp[x][y+1] = dp[x][y] + 1
            q.put((x,y+1))
    return dp[-1][-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
