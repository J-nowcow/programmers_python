#https://programmers.co.kr/learn/courses/30/lessons/43164
"""
dfs로 돌면서 백트레킹 시키는 문제인 것 같음
끝까지 갔다가, 더 갈 곳 없으면 돌아와서 다른 곳 가보고
계속 반복하면서 끝까지 다 찾은 경로 생기면 리턴
근데 이거 ticket 총 개수 제한이 inf인데 정렬하면 원칙적으로는 터져야 함..
문제 제한사항이 부실하게 달려 있는듯

"""
"""
def dfs(pos, answer, tmp, tickets, visited): # pos: 현재 공항 이름, tmp: 지금 돈 순서
    print(pos, answer, tmp, tickets, visited)
    if 0 not in visited: # 전부 다 돌았으면
        if answer == []: # 아직 들어온게 없으면
            answer = tmp[::1]
            return tmp
        
        if tmp < answer: # 지금 찾은게 더 작으면
            answer = tmp
            return tmp
        
        return answer
    
    for i in range(len(tickets)):
        print(i,tickets[i][0], visited[i], pos)
        if tickets[i][0] == pos and visited[i] == 0: # 아직 안왔고 시작점이면
            visited[i] = 1; tmp.append(tickets[i][1]) #경로 추가, visited 바꾸기
            answer = dfs(tickets[i][1], answer, tmp, tickets, visited)
            visited[i] = 0; tmp.pop() # 다시 지우기

    print("answer", answer)
    return answer    
            
def solution(tickets):
    answer = [] # 정답 넣어둘 리스트
    visited = [0] * len(tickets) # 방문했는지 체크해주기
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            print("!@$#%")
            visited[i] = 1 # 왔다고 바꿔주기
            answer = dfs("ICN", answer, ["ICN"], tickets, visited)
            visited = [0] * len(tickets) # 다음 탐색 위해 초기화
    print(answer)
    return answer
"""
def solution(tickets):
    dic = {}
    for i in tickets:
        if i[0] in dic: # 있는 경우
            dic[i[0]].append(i[1])
        else: # 없는 경우
            dic[i[0]] = [i[1]]
    
    for i in dic: dic[i].sort(reverse = True) # 각 딕셔너리별로 알파벳 역순으로 정렬

    stack = ["ICN"] # 시작 공항 인천이니까 디폴트 설정해주기
    answer = []
    # a-b, a-c, c-a 있다고 하면 a-c를 가야 할텐데, 일단 a-b를 스택에 넣을 거임
    # 그럼 그다음 b에서 가는게 없으니까 얘를 뒤로 미뤄줘야 함
    # 그래서 경로에 넣어두고, 그 다음 값인 a-c를 돌고 c-a로 다시 돌아옴
    # 그러면 a-b 빠져있고, 그 앞에 c-a, a-c 순서대로 들어올거임
    # 이걸 역순으로 빼주면 답이 됨
    while len(stack):
        if stack[-1] not in dic or len(dic[stack[-1]]) == 0: #만약 없거나 이미 다 돌았으면
            answer.append(stack.pop()) # 스택에서 팝해서 딕셔너리에 다시 넣어주기
        else: #아니라면 = 있다면
            stack.append(dic[stack[-1]].pop()) # 딕셔너리의 마지막 값 = 알파벳 가장 작은 값 빼주기
        #print(answer)
        #print(stack)
        #print(dic)
    return answer[::-1]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(tickets))
