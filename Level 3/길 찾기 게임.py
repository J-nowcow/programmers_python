#https://programmers.co.kr/learn/courses/30/lessons/42892
"""
이진트리 전위순회, 후위순회 구현하기
같은 레벨에 있는 노드는 모두 같은 y값을 가져야 함
문제 조건을 만족하도록 구성할 수 있는 노드 배열만 주어지니까
y기준으로 정렬해놓고 x값만 하나씩 트리에 넣어주기
"""
import sys
sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree():
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        
    def insert_value(self, node, data):
        if node == None:
            node = Node(data)
        elif data <= node.data:
            node.left = self.insert_value(node.left, data)
        else:
            node.right = self.insert_value(node.right, data)
        return node
    
    def preorder(self):
        return self.pre(self.root, [])
    def pre(self, node, arr):
        if node == None: return arr
        arr.append(node.data[1])
        arr = self.pre(node.left, arr)
        arr = self.pre(node.right, arr)
        return arr
    
    def postorder(self):
        return self.post(self.root, [])
    def post(self, node, arr):
        if node == None: return arr
        arr = self.post(node.left, arr)
        arr = self.post(node.right, arr)
        arr.append(node.data[1])
        return arr
    
def solution(nodeinfo):
    # 몇번째 node인지 정보 추가해주기
    node = [[nodeinfo[i][0],nodeinfo[i][1],i+1] for i in range(len(nodeinfo))]
    # y 역순으로 정렬
    node.sort(key = lambda x: -x[1])
    tree = BTree()
    for i in node:
        tree.insert([i[0],i[2]])        
    return [tree.preorder(), tree.postorder()]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
