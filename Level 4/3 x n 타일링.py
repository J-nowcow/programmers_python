# https://programmers.co.kr/learn/courses/30/lessons/12902
"""
3xn 타일링: n에 짝수값만 들어옴
f(n) = 3*f(n-2) + 2*(f(n-4)+f(n-6)+...+f(2)+f(0))
f(0) = 1
n-2까지 제대로 채워진 타일에서 마지막 두칸 채우는 방법 3가지
n-2는 아닌데, n-4에서부터 채워지는 경우 2가지
n-6에서부터도 2가지, ..., 계속 반복: 아무것도 없는 상태까지 반복
"""
def solution(n):
    a = [3]
    for i in range(n//2-1):
        s=2*sum(a)+2+a[-1]
        a.append(s%1000000007)
    return a[-1]

print(solution(4))
