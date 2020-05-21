# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ""
    while n:
        n-=1
        answer += "124"[n%3]
        n //= 3
    return answer[::-1]

for i in range(1,10):
    print(solution(i))
