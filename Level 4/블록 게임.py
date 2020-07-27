# https://programmers.co.kr/learn/courses/30/lessons/42894
"""
왼쪽 위부터 검은 블록 한칸씩 채워나가기 (검은 블록: -1)
방금 칠한 칸 기준으로 2x3 정사각형이 모두 0이 아닌 곳이 있다면 지워주기(모두 -1인 경우는 제외)
1 2 3 1 2
4 5 6 3 4
      5 6
에서 2 3 에 있는 경우/ 2 3 4에 있는 경우 총 5가지 분석해주면 됨 다른경우는 없음
지운 다음에는 지운 칸 채울지 말지 결정
"""

def solution(board):
    N = len(board)
    b = [[-1] * (N+4) for _ in range(2)]
    for i in board: b.append([0,0] + i + [0,0])
    for _ in range(2): b.append([0]*(N+4))

    board = b
    answer = 0
    for i in range(2,N+2):
        for j in range(2,N+2):
            if board[i][j] == 0 and (i == 0 or board[i-1][j] == -1):
                board[i][j] = -1
            # 1. 가로 3 세로 2짜리
            lst = board[i][j-2:j+1] + board[i+1][j-2:j+1]
            if 0 not in lst and lst.count(-1) == 2 and len(set(lst)) == 2:
                if board[i-1][j-2] == -1: board[i][j-2] = -1; board[i+1][j-2] = -1
                if board[i-1][j-1] == -1: board[i][j-1] = -1; board[i+1][j-1] = -1
                if board[i-1][j] == -1: board[i][j] = -1; board[i+1][j] = -1
                answer += 1
                
            lst = board[i][j-1:j+2] + board[i+1][j-1:j+2]
            if 0 not in lst and lst.count(-1) == 2 and len(set(lst)) == 2:
                if board[i-1][j-1] == -1: board[i][j-1] = -1; board[i+1][j-1] = -1
                if board[i-1][j] == -1: board[i][j] = -1; board[i+1][j] = -1
                if board[i-1][j+1] == -1: board[i][j+1] = -1; board[i+1][j+1] = -1
                answer += 1

            # 2. 가로 2 세로 3짜리
            lst = board[i][j-1:j+1] + board[i+1][j-1:j+1] + board[i+2][j-1:j+1]
            if 0 not in lst and lst.count(-1) == 2 and len(set(lst)) == 2:
                if board[i-1][j-1] == -1: board[i][j-1] = -1; board[i+1][j-1] = -1; board[i+2][j-1] = -1
                if board[i-1][j] == -1: board[i][j] = -1; board[i+1][j] = -1; board[i+2][j] = -1
                answer += 1

            lst = board[i-1][j:j+2] + board[i][j:j+2] + board[i+1][j:j+2]
            if 0 not in lst and lst.count(-1) == 2 and len(set(lst)) == 2:
                if board[i-2][j] == -1: board[i-1][j] = -1; board[i][j] = -1; board[i+1][j] = -1
                if board[i-2][j+1] == -1: board[i-1][j+1] = -1; board[i][j+1] = -1; board[i+1][j+1] = -1
                answer += 1

            lst = board[i-1][j-1:j+1] + board[i][j-1:j+1] + board[i+1][j-1:j+1]
            if 0 not in lst and lst.count(-1) == 2 and len(set(lst)) == 2:
                if board[i-2][j-1] == -1: board[i-1][j-1] = -1; board[i][j-1] = -1; board[i+1][j-1] = -1
                if board[i-2][j] == -1: board[i-1][j] = -1; board[i][j] = -1; board[i+1][j] = -1
                answer += 1
    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
#board = [[1,2],[3,4]]
print(solution(board))
