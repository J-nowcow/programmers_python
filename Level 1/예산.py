#https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d,budget):
    d.sort()
    a = 0
    for i in range(len(d)):
        a+=d[i]
        if a>budget: return i
    return len(d)

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))
