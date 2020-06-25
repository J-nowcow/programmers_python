#https://programmers.co.kr/learn/courses/30/lessons/60061
"""
2차원 격자점에 연결된 세로선이랑 가로선 채워넣기
가로줄이랑 세로줄 각각 2차원 리스트 만들어서 처리하기
그냥 구현 문제인데 두시간이 넘게 걸리네 ㅂㄷㅂㄷ
"""

# 설치 가능하면 True 리턴하는 함수
def ispossible(garo,sero,x,y,a):
    # 기둥 설치하는 경우
    if a == 0:
        # 1. 바닥 위에 있는 경우: y = 0
        # 2. 보의 한쪽 끝: garo[x-1][y] = 1 or garo[x][y] = 1
        # 3. 다른 기둥 위: sero[x][y-1] = 1    
        if (y == 0) or (x > 0 and garo[x-1][y]) or garo[x][y] or sero[x][y-1]:
            return True
    # 보 설치하는 경우
    else:
        # 1. 기둥 위: sero[x][y-1] = 1 or sero[x+1][y-1] = 1
        # 2. 양쪽 끝 동시 연결: x>0 and garo[x-1][y] = 1 and garo[x+1][y] = 1
        if (sero[x][y-1] or sero[x+1][y-1]) or (x > 0 and garo[x-1][y] and garo[x+1][y]):
            return True
        
def solution(n, build_frame):
    # 가로줄과 세로줄 각각 리스트를 만들어준다.
    garo = [[0]*(n+2) for i in range(n+2)] # garo[x][y]: (x,y) - (x+1,y)
    sero = [[0]*(n+2) for i in range(n+2)] # sero[x][y]: (x,y) - (x,y+1)

    for info in build_frame:
        x,y,a = info[0:3]
        # 추가하는 경우
        if info[3] == 1:
            if ispossible(garo,sero, x, y, a):
                if a == 0: sero[x][y] = 1
                else: garo[x][y] = 1
        
        # 삭제하는 경우: 일단 지우고 possible한지 확인하기
        else:
            # 기둥 삭제하는 경우
            if a == 0:
                # 위의 기둥, 양쪽 위의 보 3가지 확인
                sero[x][y] = 0
                if sero[x][y+1] and (not ispossible(garo,sero,x,y+1,0)): sero[x][y] = 1; continue
                if garo[x][y+1] and (not ispossible(garo,sero,x,y+1,1)): sero[x][y] = 1; continue
                if garo[x-1][y+1] and (not ispossible(garo,sero,x-1,y+1,1)): sero[x][y] = 1; continue
  
            # 보 삭제하는 경우
            else:
                # 양쪽 기둥, 양쪽 옆의 보 4가지 확인
                garo[x][y] = 0
                if sero[x][y] and (not ispossible(garo,sero,x,y,0)): garo[x][y] = 1; continue
                if sero[x+1][y] and (not ispossible(garo,sero,x+1,y,0)): garo[x][y] = 1; continue
                if garo[x-1][y] and (not ispossible(garo,sero,x-1,y,1)): garo[x][y] = 1; continue
                if garo[x+1][y] and (not ispossible(garo,sero,x+1,y,1)): garo[x][y] = 1; continue


    # return 값 만들기
    answer = []
    for i in range(n+2):
        for j in range(n+2):
            if sero[i][j] == 1:
                answer.append([i,j,0])
            if garo[i][j] == 1:
                answer.append([i,j,1])
                
    return answer

n = 5
build_frame =[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))

