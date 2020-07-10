#https://programmers.co.kr/learn/courses/30/lessons/60063
"""
Queue 하나 설정해서 (x, y, 가로/세로, 몇번째 탐색인지) 튜플로 넣어주기
BFS 구현하기
"""
import queue
def solution(board):
    q = queue.Queue() # 넣기: put(), 빼기: get()
    a = len(board); b = len(board[0])
    # check[x][y][0]: x,y에 가로로 탐색한 적 있는지 체크
    # 99999이면 아직 탐색하지 않은 곳, 아니면 탐색한 곳
    check = [[[99999,99999] for i in range(b)] for j in range(a)]
    check[0][0][0] = 1
    q.put((0,0,0,check[0][0][0]))
    while q.qsize() > 0:
        x,y,state,num = q.get()
        print(x,y,state,num)

        # 가로인 경우
        if state == 0:
            if x and y < a-1 and check[x-1][y][0] > num and not (board[x-1][y] or board[x-1][y+1]):
                check[x-1][y][0] = num; q.put((x-1,y,0,num+1))
            if x < a-1 and y < b-1 and check[x+1][y][0] > num and not (board[x+1][y] or board[x+1][y+1]):
                check[x+1][y][0] = num; q.put((x+1,y,0,num+1))
            if y and check[x][y-1][0] > num and not board[x][y-1]:
                check[x][y-1][0] = num; q.put((x,y-1,0,num+1))
            if y < b-2 and check[x][y+1][0] > num and not board[x][y+2]:
                check[x][y+1][0] = num; q.put((x,y+1,0,num+1))
            if x and y < b-1 and not (board[x-1][y] or board[x-1][y+1]):
                # 왼쪽 위로 돌리는 경우: (x-1,y,1)
                if check[x-1][y][1] > num:
                    check[x-1][y][1] = num; q.put((x-1,y,1,num+1))
                # 오른쪽 위로 돌리는 경우: (x-1,y+1,1)
                if check[x-1][y+1][1] > num:
                    check[x-1][y+1][1] = num; q.put((x-1,y+1,1,num+1))
            if x < a-1 and y < b-1 and not (board[x+1][y] or board[x+1][y+1]):
                if check[x][y][1] > num:
                    check[x][y][1] = num; q.put((x,y,1,num+1))
                if check[x][y+1][1] > num:
                    check[x][y+1][1] = num; q.put((x,y+1,1,num+1))
        # 세로인 경우
        else:
            if x and check[x-1][y][1] > num and not board[x-1][y]:
                check[x-1][y][1] = num; q.put((x-1,y,1,num+1))
            if x < a-2 and check[x+1][y][1] > num and not board[x+2][y]:
                check[x+1][y][1] = num; q.put((x+1,y,1,num+1))
            if x < a-1 and y and check[x][y-1][1] > num and not (board[x][y-1] or board[x+1][y-1]):
                check[x][y-1][1] = num; q.put((x,y-1,1,num+1))
            if x < a-1 and y < b-1 and check[x][y+1][1] > num and not (board[x][y+1] or board[x+1][y+1]):
                check[x][y+1][1] = num; q.put((x,y+1,1,num+1))
            if y and x and not (board[x][y-1] or board[x+1][y-1]):
                if check[x][y-1][0] > num:
                    check[x][y-1][0] = num; q.put((x,y-1,0,num+1))
                if check[x+1][y-1][0] > num:
                    check[x+1][y-1][0] = num; q.put((x+1,y-1,0,num+1))
            if y < a-1 and x < a-1 and not (board[x][y+1] or board[x+1][y+1]):
                if check[x][y][0] > num:
                    check[x][y][0] = num; q.put((x,y,0,num+1))
                if check[x+1][y][0] > num:
                    check[x+1][y][0] = num; q.put((x+1,y,0,num+1))
    for i in check:
        for j in i:
            print(j[0], end=" ")
        print()
    for i in check:
        for j in i:
            print(j[1],end=" ")
        print()
    print(check[-1][-2][0])
    print(check[-2][-1][1])
    return min(check[-1][-2][0], check[-2][-1][1])
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))
