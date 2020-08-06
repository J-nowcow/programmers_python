# https://programmers.co.kr/learn/courses/30/lessons/12984
"""
모든 칸의 높이 동일하게 맞추기
정렬해놓고 Q : P 내분점에서 자른 다음 거기에 맞추기
"""
def solution(land, P, Q):
    lst = []
    for i in land:
        lst += i
    lst.sort()
    print(lst)
    s = Q * len(lst) // (P+Q)
    return P * (s * lst[s] - sum(lst[:s])) + Q * (sum(lst[s:]) - (len(lst) - s) * lst[s])

land = [[4,4,3],[3,2,2],[2,1,0]]
print(solution(land,5,3))
