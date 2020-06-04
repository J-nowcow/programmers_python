#https://programmers.co.kr/learn/courses/30/lessons/49189
"""
각 노드별로 인접한 노드 집합 만들어주기
*) 인접한 : adjacent
거리 list 만들어서 각 집합별로 더해주기?
"""
import queue
def solution(n, edge):
    adj = [set() for i in range(n+1)]
    for a,b in edge:
        adj[a].add(b)
        adj[b].add(a)
        
    dist = [-1] * (n+1)
    dist[1] = 0
    
    q = queue.Queue()
    for i in adj[1]: q.put([i,1])
    while q.qsize():
        a,b = q.get()

        if dist[a] == -1:
            dist[a] = b
            for i in adj[a]: q.put([i,b+1])
            
    return dist.count(max(dist))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))
