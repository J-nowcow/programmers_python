#https://programmers.co.kr/learn/courses/30/lessons/12905
"""
왼쪽 위부터 그 칸 기준으로 오른쪽 아래로 탐색하면서 정사각형인지 탐색하기
그 칸이 1이라면
그 칸 기준 왼쪽/ 위쪽/ 대각선 3칸 값 찾아서
그 값중 가장 작은 값 + 1로 바꿔주기
(0이 있으면 1x1만 되니까 그대로 1이고
만약 셋다 2면 3x3짜리 싹 다 되는거니까 그자리 3들어감)

ex)
0 1 1 1      0 1 1 1
1 1 1 1  --> 1 1 2 2
1 1 1 1      1 2 2 3
0 0 1 0      0 0 1 0
"""
def solution(board):
    answer = 0
    if 1 in board[0]: answer = 1
    for i in board:
        if i[0] ==1 : answer = 1 # 첫줄에만 숫자 1이 있는 경우 답 1이니까 미리 처
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1: # 0이 아닐 때 = 정사각형이 있을 때
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(board[i][j],answer)
    #print(board)
    return answer**2
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
