#https://programmers.co.kr/learn/courses/30/lessons/12913
"""
2차원 dp 연습문제
한줄씩 내려오면서 자기 윗칸 말고 나머지 최댓값 + 그 칸의 값
"""

def solution(land):
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
