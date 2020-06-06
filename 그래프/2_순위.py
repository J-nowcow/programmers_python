# https://programmers.co.kr/learn/courses/30/lessons/49191
"""
각각의 원소에 대해 그 사람을 이긴 사람/ 진 사람 집합 설정해놓고
업데이트 해준 다음에 집합 사이즈 합이 n-1인 개수 세기
"""
def solution(n, results):
    win = {}; lose = {}
    for i in range(1,n+1):
        win[i] = set(); lose[i] = set()

    for i in range(n):
        for a,b in results:
            win[b].add(a)
            win[b].update(win[a])
            lose[a].add(b)
            lose[a].update(lose[b])

    answer = 0
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1: answer += 1
    return answer

n = 5
results = [[4,3],[4,2],[3,2],[1,2],[2,5]]
print(solution(n,results))
