# https://programmers.co.kr/learn/courses/30/lessons/17679
"""
n,m<=30이니까 대충 아무렇게나 짜도 돌아가겠는데....?
900 * (900/4) 해도 돌아가니까 그냥 완전탐색 해도 될듯
"""

def solution(m, n, board):
    remain = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            remain[i][j] = board[i][j] # 문자열 처리하기 쉽게 이중 리스트로 변환

    answer = 0
    
    while 1:
        # 보드에서 2x2 찾아주기
        tmp = [] # 지워줄 칸들의 왼쪽 위 위치 저장
        for i in range(m-1):
            for j in range(n-1):
                if remain[i][j] != 0: # 빈칸이 아니고
                    if remain[i][j] == remain[i+1][j+1]\
                       and remain[i][j] == remain[i][j+1]\
                       and remain[i][j] == remain[i+1][j]: # 다 같으면                        tmp.append([i,j])
                        tmp.append([i,j])
                        
        if len(tmp) == 0: # 지워줄 게 하나도 없으면
            break # 끝난거니까 반복문 나가기
        
        # 찾은 칸들 지워주기
        for a, b in tmp:
            for i in range(a,a+2):
                for j in range(b,b+2):
                    remain[i][j] = 0

        # 밑으로 내려주기
        for j in range(n): # 한 줄씩 찾아주자
            point = -1 # 0인 가장 아랫칸의 위치
            for i in range(m-1,-1,-1):
                if remain[i][j] == 0:
                    point = i; break
            if point == -1:
                continue # 0인 칸이 없으면 넘어가기
            
            for i in range(m-1,-1,-1): # 내려주니까 밑에부터 탐색하면서 올라가기
                if remain[i][j] != 0 and point > i: # point보다 위고 0이 아닌 칸이면
                    remain[i][j], remain[point][j] = remain[point][j], remain[i][j]
                    point -= 1 # 위치 서로 바꿔주고 다음 0인 칸으로 올려주기
            
    # 0인 칸의 개수가 지워진 칸의 개수
    for i in range(m):
        for j in range(n):
            if remain[i][j] == 0: answer += 1

    return answer

m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))
