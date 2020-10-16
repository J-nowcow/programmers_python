# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    a = ""
    while n:
        a += str(n%3)
        n//=3
    a = a[::-1]

    ans = 0
    for i in range(len(a)):
        ans += int(a[i]) * (3**i)
    return ans
print(solution(125))
