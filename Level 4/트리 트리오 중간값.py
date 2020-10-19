# https://programmers.co.kr/learn/courses/30/lessons/68937
"""
tree의 지름(가장 먼 두 노드 사이의 거리)를 찾자.
(a,b)의 거리가 지름 n이고,
다른 노드 c가 존재하여 (a,c) 혹은 (b,c)의 거리가 (a,b)와 같다면 중앙값의 최댓값은 n이다.
그런 경우가 없다면 a 하나 전의 노드, 혹은 b 하나 전의 노드와 이으면 되므로 n-1이다.

tree의 지름은 임의의 노드 t에서 가장 먼 노드 x를 찾고, x에서 가장 먼 노드 y를 찾으면 된다.

"""
def solution(n,edges):
    tree = {}
    for i in range(1,n+1):
        tree[i] = []
    for a,b in edges:
        tree[a] += [b]
        tree[b] += [a]

    x, tmp = findmax(1,n,tree,-1)
    y, tmp = findmax(x,n,tree,-1)
    tmp, a1 = findmax(x,n,tree,y)
    tmp, a2 = findmax(y,n,tree,x)
    
    return max(a1,a2)

def findmax(x,n,tree, cf = -1):
    dist = [-1]*(n+1)
    s = [(x,0)]; dist[x] = 0
    while s:
        tmp, d = s.pop()
        for i in tree[tmp]:
            if dist[i] == -1 and i != cf:
                s += [(i, d+1)]
                dist[i] = d+1
    a = max(dist)
    return dist.index(a),a
print(solution(4,[[1,2],[2,3],[3,4]]))
