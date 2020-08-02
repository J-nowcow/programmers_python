#https://programmers.co.kr/learn/courses/30/lessons/17685
"""
트라이에 하나씩 넣어주고 노드가 없으면 그 지점까지 찾아서 출력하면 됨
"""

class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.child = {}
        self.end = False # 끝났는지 확인해주는 친구
        
class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string): # 삽입
        node = self.head

        for char in string:
            if char not in node.child: # 자식중에 지금 해당하는 문자가 없으면
                node.child[char]= Node(char) # 추가
            node = node.child[char]
        node.end = True # 단어 마지막에 True 달아주기
    
    def depth(self, string): # 깊이 찾아주기
        answer = 1 # 밑에 탐색에서 아무것도 안걸리면 첫 글자로 충분한거라 1 리턴
        node = self.head
        tmp = 0
        for char in string:
            node = node.child[char]
            tmp += 1
            #print(node.key, node.child, node.end)
            if node.end == True: # 지금 길이까지의 단어가 있는 경우
                if len(node.child) != 0:
                    # abc와 abcde 있으면 abcd까지는 탐색해줘야 함
                    answer = tmp + 1
                    # 그런데 지금 찾고 있는게 abc면 abc를 리턴해줘야 함
                    if len(string) == tmp:
                        return tmp
            if len(node.child) > 1: #child가 여러 개 = 이 분기점보다는 더 찾아야됨
                answer = tmp+1
            
        return answer
    
def solution(words):
    answer = 0
    trie = Trie()
    for i in words:
        trie.insert(i) # 단어 삽입
    for i in words:
        answer += trie.depth(i) # 깊이 찾아주기
        
    return answer


words = ["abc", "def", "ghi", "jklm"]
print(solution(words))
