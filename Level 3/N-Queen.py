# https://programmers.co.kr/learn/courses/30/lessons/12952
"""
N-Queen: 백트래킹 활용한 dfs 알고리즘
"""
# solution = lambda n: [0,1,0,0,2,10,4,40,92,352,724,2680,14200][n] 으로도 정답 가능

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
