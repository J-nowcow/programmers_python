# https://programmers.co.kr/learn/courses/30/lessons/60059
"""
자물쇠 회전시킨거 4방향에 대해서 각각 브루트포스 실행
(0,1) -> (1,N-1) -> (N-1,N-2) -> (N-2,0)
(x,y) -> (y,N-1-x) -> (N-1-x, N-1-y) -> (N-1-y,x)
"""

def solution(key,lock):
    n = len(lock); m = len(key)
    k = [[[0]*m for _ in range(m)] for _ in range(4)]
    for x in range(m):
        for y in range(m):
            k[0][x][y] = key[x][y]
            k[1][y][m-1-x] = key[x][y]
            k[2][m-1-x][m-1-y] = key[x][y]
            k[3][m-1-y][x] = key[x][y]
    for key in k:
        # x = 0, y = 0 -> 0<= x+a < m , 0 <= y+b < m -> 0<=a<m, 0<=y<m
        # x = n-1, y = n-1 -> 1-n<=a<m+1-n, 1-n<=b<m+1-n
        # 두개 합치면 1-n <= a < m
        for a in range(1-n,m):
            for b in range(1-n,m):
                check = True
                for x in range(n):
                    for y in range(n):
                        if lock[x][y] == 1:
                            if 0 <= x+a < m and 0 <= y+b < m and key[x+a][y+b] == 1:
                                check = False
                                break
                            else: continue
                        if 0 <= x+a < m and 0 <= y+b < m and key[x+a][y+b] == 1:
                            continue
                        check = False
                        break
                    if not check: break
                if check: return True
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))

