#https://programmers.co.kr/learn/courses/30/lessons/12924
"""
(1+...+i) + t*i == n 일 때 가능
n - (i+1)*i//2 >= 0 and (n - (i+1)*i//2) % i == 0
"""
def solution(n):
    answer = 0
    for i in range(1,n+2):
        if n - (i+1)*i//2 < 0: return answer
        if (n - (i+1)*i//2) % i == 0: answer+=1

for i in range(1,16):
    print(solution(i))
