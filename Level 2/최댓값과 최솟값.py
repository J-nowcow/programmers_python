# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    a = [int(i) for i in s.split()]
    return str(min(a))+" "+str(max(a))

print(solution("-1 2 3 -4"))
