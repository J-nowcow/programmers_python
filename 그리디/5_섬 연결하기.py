class Disjointset:
    def __init__(self, num):
        self.parent = {} # 가장 위 노드
        self.rank = {} # 굳이 필요 없지만 효율성 증가를 위해 넣어준다.
        for i in range(num):
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

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    disjoint = Disjointset(n)
    answer = 0
    for a,b,c in costs:
        root1 = disjoint.find(a)
        root2 = disjoint.find(b)
        if root1 != root2:
            disjoint.union(root1, root2)
            answer += c
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))
