#https://programmers.co.kr/learn/courses/30/lessons/43165
"""
이상하다 분명히 풀었던 문젠데 어디서 봤지..?
아 스킬 체크 할때 봤었나보다
dfs bfs 파트지만 그냥 브루트 포스 하는게 답인 이상한 문제
아 이걸 깊이우선탐색이라고 부르는건가..?

근데 -1000~1000 리스트 만들어서 계산해주는게 빠를지도

2^20 = 1048576
2001 * 20 = 40020 -> 이게 압도적으로 빠름
"""

def solution(numbers, target):
    answer = [0]*2001 # -1000 ~ 1000 만들 수 있는지 확인하는 리스트
    answer[1000 + numbers[0]] = 1; answer[1000 - numbers[0]] = 1 # 첫 값
    for i in numbers[1:]:
        tmp = [0] * 2001
        for j in range(2001):
            if answer[j] != 0: # 0이 아니면 = 있으면
                tmp[j+i] += answer[j] # 다음 원소 추가해준거 저장
                tmp[j-i] += answer[j]
        answer = tmp
    return answer[target+1000]

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
