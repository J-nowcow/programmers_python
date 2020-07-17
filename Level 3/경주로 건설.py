# https://programmers.co.kr/learn/courses/30/lessons/67259
"""
bfs 문제 구현하기
직선, 곡선에 따라 값이 다르므로
탐색했는지 체크해주는 리스트
가로에서 왔는지, 세로에서 왔는지 두가지로 만들어서 각각 탐색해주기
"""
import queue
def solution(board):
    n = len(board)
    check = [[[10**5,10**5] for _ in board] for _ in board]
    check[0][0] = [0,0]
    q = queue.Queue()
    
    # x,y 좌표
    q.put((0,0))
    
    while q.qsize():
        # 위, 아래, 오른쪽, 왼쪽 각각에 대해서 각각 탐색
        x,y = q.get()
        # 1. 위로 가는 경우: 방향은 세로
        if x and not board[x-1][y]:
            if check[x-1][y][1] > min(check[x][y][0]+6, check[x][y][1]+1):
                check[x-1][y][1] = min(check[x][y][0]+6, check[x][y][1]+1)
                q.put((x-1,y))
        # 2. 아래로 가는 경우: 방향은 세로    
        if x < n-1 and not board[x+1][y]:
            if check[x+1][y][1] > min(check[x][y][0]+6, check[x][y][1]+1):
                check[x+1][y][1] = min(check[x][y][0]+6, check[x][y][1]+1)
                q.put((x+1,y))
        # 3. 왼쪽으로 가는 경우: 방향은 가로 
        if y and not board[x][y-1]:
            if check[x][y-1][0] > min(check[x][y][0]+1, check[x][y][1]+6):
                check[x][y-1][0] = min(check[x][y][0]+1, check[x][y][1]+6)
                q.put((x,y-1))
        # 4. 오른쪽으로 가는 경우: 방향은 가로
        if y < n-1 and not board[x][y+1]:
            if check[x][y+1][0] > min(check[x][y][0]+1, check[x][y][1]+6):
                check[x][y+1][0] = min(check[x][y][0]+1, check[x][y][1]+6)
                q.put((x,y+1))
    
    return min(check[-1][-1]) * 100


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],
         [0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
"""
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]"""
print(solution(board))
