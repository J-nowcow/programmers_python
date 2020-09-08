# https://programmers.co.kr/learn/courses/30/lessons/67260

"""
stack 하나 정의해서, 0부터 탐색한다.

check: 그 방을 탐색했는지 확인하는 리스트
after[a] = b: a를 방문해야 b를 방문할 수 있다.
before[a] = b: a를 방문하기 전에 b를 방문해야 한다. (after와 반대)

graph[a]: a에서 갈 수 있는 방


"""
def solution(n, path, order):
    graph = [[] for _ in range(n)]
    before = [0] * n 
    after = [0] * n

    check = [0] * n
    
    for a,b in path:
        graph[b].append(a)
        graph[a].append(b)

    for a,b in order:
        before[b] = a # b를 방문하기 전에 a를 방문해야 한다.
        
    if before[0]:
        return False

    stack = [0]
    check[0] = 1
    while stack:
        tmp = stack.pop()
        
        # 지금 방에 도달할 수는 있는데, 먼저 들러야 할 방이 있는 경우
        if not check[before[tmp]]:
            after[before[tmp]] = tmp
            continue

        # 지금 방과 연결된 방들 중에서 아직 방문 안한 방 스택에 추가
        for i in graph[tmp]:
            if not check[i]:
                stack.append(i)

        # 과거에 도달했었지만 지금 방을 먼저 들렀어야 했어서 탐색하지 못했던 방 스택에 추가
        if after[tmp]:
            stack.append(after[tmp])

        # 방 탐색 완료           
        check[tmp] = 1
        
    return False if 0 in check else True
    
n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print(solution(n,path,order))
