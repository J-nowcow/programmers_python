# https://programmers.co.kr/learn/courses/30/lessons/62050
"""
① 사다리 없이 이동할 수 있는 영역 구분해주기
② 각 영역을 연결하기 위한 비용들 구해주기
③ 최소 신장 트리 구하기 (크루스칼 알고리즘 사용)
"""

import sys
sys.setrecursionlimit(10**6)

def solution(land, height):
    N = len(land)
    group = [[0]*N for _ in range(N)]

    # grouping: dfs 이용하기
    num = 1
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(N):
        for j in range(N):
            # 아직 그룹 생기지 않은 땅에 대해서 그룹 만들기
            if group[i][j] == 0:
                group[i][j] = num
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx, dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < N and group[nx][ny] == 0 and abs(land[nx][ny]-land[x][y]) <= height:
                            stack.append((nx,ny))
                            group[nx][ny] = num
                num += 1          
    # print(group)            

    # 노드와 간선 데이터 만들기
    cost = {}
    # cost[(a,b)] = c : a와 b를 잇는 사다리의 가격이 c ( a < b )
    for x in range(N):
        for y in range(N):
            # 그룹이 서로 다를 때, 딕셔너리에 없거나 더 비싸면 업데이트 하기
            if x < N-1 and group[x][y] != group[x+1][y]:
                tmp = (min(group[x][y], group[x+1][y]), max(group[x][y], group[x+1][y]))
                if tmp not in cost or cost[tmp] > abs(land[x][y] - land[x+1][y]):
                    cost[tmp] = abs(land[x][y] - land[x+1][y])
                
            if y < N-1 and group[x][y] != group[x][y+1]:
                tmp = (min(group[x][y], group[x][y+1]), max(group[x][y], group[x][y+1]))
                if tmp not in cost or cost[tmp] > abs(land[x][y] - land[x][y+1]):
                    cost[tmp] = abs(land[x][y] - land[x][y+1])
    # print(cost)

    # 크루스칼 알고리즘으로 최솟값 구하기
    cost = sorted(cost.items(), key = lambda x: x[1])
    disjoint = Disjointset(num)
    answer = 0
    for i in cost:
        a,b,c = i[0][0],i[0][1],i[1] # 각 간선, 비용
        root1 = disjoint.find(a)
        root2 = disjoint.find(b)
        if root1 != root2:
            disjoint.union(root1, root2)
            answer += c
    
    return answer

class Disjointset:
    def __init__(self, num):
        self.parent = {} # 가장 위 노드
        self.rank = {} # 굳이 필요 없지만 효율성 증가를 위해 넣어준다.
        for i in range(1,num):
            self.parent[i] = i
            self.rank[i] = 0
            
    # find: 가장 위 노드 (=부모가 자기 자신인 노드)를 찾아준다.
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    # union: 두 집합을 합쳐준다.
    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
                
land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3
print(solution(land,height))
