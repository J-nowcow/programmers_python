# https://programmers.co.kr/learn/courses/30/lessons/12978
"""
어차피 n^2으로 돌아갈거 굳이 다익스트라 안만들고 그냥 for문 road 크기만큼 반복
"""
def solution(N, road, K):
    dist = [0,0]+[50*500001]*(N-1)
    for _ in road:
        for r in road:
            dist[r[1]] = min(dist[r[0]]+r[2],dist[r[1]])
            dist[r[0]] = min(dist[r[1]]+r[2],dist[r[0]])
    answer = 0
    for i in dist[1:]:
        if i <= K: answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N,road,K))
