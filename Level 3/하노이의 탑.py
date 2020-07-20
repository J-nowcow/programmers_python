# https://programmers.co.kr/learn/courses/30/lessons/12946
"""
하노이탑: f(a,b,c,n) : a에서 b를 거쳐서 c로 이동시키기
f(a,b,c,n) = f(a,c,b,n-1) + (a -> c) + f(b,a,c,n-1)
"""
def solution(n):
    answer = []
    def f(a,b,c,n):
        if n == 1:
            answer.append([a,c])
        else:
            f(a,c,b,n-1)
            answer.append([a,c])
            f(b,a,c,n-1)
    f(1,2,3,n)
    return answer

print(solution(3))
