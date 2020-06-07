# https://programmers.co.kr/learn/courses/30/lessons/42886
"""
추의 무게 정렬하기
n-1번 째 추까지의 무게의 합 + 1보다 n번 째 추의 무게가 더 크다면
sum(1~n-1) + 1 이 만들지 못하는 무게의 최솟값임
"""
def solution(weight):
    if not 1 in weight: return 1
    weight.sort()
    s = weight[0]
    for i in weight[1:]:
        if i > s+1: return s+1
        s += i
    return s + 1
print(solution([3,1,6,2,7,30,1]))
    
