#https://programmers.co.kr/learn/courses/30/lessons/12985
"""
토너먼트 경기에서 두 참가자가 몇 번째 경기에 만나게 되는지 찾아주는 문제
i번째 경기:
1~2**i, 2**i+1~2*2**i, ...
--> 2**i로 나누었을 때 몫이 같다면 그 판에서 만나게 됨

그런데 참가자 번호를 1부터 줬으니까 1씩 빼서 계산해주기
"""

def solution(n,a,b):
    for i in range(1,21):
        if (a-1) // (2 ** i) == (b-1) // (2 ** i): return i

n = 8
a = 4; b = 7
print(solution(b,a,b))
