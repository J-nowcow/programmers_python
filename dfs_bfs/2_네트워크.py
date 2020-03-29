#https://programmers.co.kr/learn/courses/30/lessons/43162
"""
입력이 좀 헷갈리게 되어 있는데
110
110
001 이면 0 1번 두개 연결되어있고 2번 혼자 따로 노는중
200 이하니까 대충 n^3까지도 잘 돌아감 (800만)

그래프 dfs로 탐색하면서 1인 칸 찾으면 2로 바꿔주는 식으로 하면 될듯
각 컴퓨터에 대해서는 최대 1번만 탐색하고 그 뒤로는 바로바로 리턴해주니까
시간복잡도는 O(n^2) 으로 커팅되는 것처럼 보이는데 확실하진 않음 확인해야됨
"""
def dfs(i, computers):
    if 1 not in computers[i]: # 이미 다 찾은 컴퓨터면
        return
    for j in range(len(computers)):
        if computers[i][j] == 1: # 아직 탐색 안한 칸이면
            computers[i][j] = 2 # 탐색 한걸로 바꿔주기
            computers[j][i] = 2 # 그 짝도 같이 바꿔주기
            if i != j: # 두개 다르면 = 서로 다른 컴퓨터가 연결된거면
                dfs(j, computers) # 그 컴퓨터로 넘어가서 또 찾아주기
    
def solution(n, computers):
    answer = 0
    found = []
    for i in range(n):
        if 1 in computers[i]: # 1이 있으면 = 탐색이 아직 안된 컴퓨터면
            answer += 1; dfs(i, computers)        
    return answer

n = 3
computers = [[1,1,0],[1,1,0],[0,0,1]]
print(solution(n, computers))
