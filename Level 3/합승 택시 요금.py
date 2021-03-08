# https://programmers.co.kr/learn/courses/30/lessons/72413

# 모든 노드에 대해 A, B, S까지 가는 최단거리 각각 구하기 : 다익스트라
# 세 최단거리의 합이 최소인 경우가 최소
# 연결되지 않은 노드 체크

import queue
def dijkstra(n, start, fares):
    dic = dict([(i, []) for i in range(1,n+1)])    
    for a,b,cost in fares:
        dic[a].append((b, cost))
        dic[b].append((a, cost))

    dis = [-1] * (n+1)
    dis[start] = 0
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        tmp = q.get()
        for i in dic[tmp]:
            if dis[i[0]] == -1 or dis[i[0]] > dis[tmp] + i[1]:
                dis[i[0]] = dis[tmp] + i[1]
                q.put(i[0])
    return dis
        
def solution(n, s, a, b, fares):
    dis_a = dijkstra(n,a,fares)
    dis_b = dijkstra(n,b,fares)
    dis_s = dijkstra(n,s,fares)

    answer = 10**10
    for i in range(n+1):
        if -1 not in (dis_a[i], dis_b[i], dis_s[i]):
            answer = min(answer, dis_a[i] + dis_b[i] + dis_s[i])
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
