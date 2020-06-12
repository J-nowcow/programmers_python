#https://programmers.co.kr/learn/courses/30/lessons/42888
"""
유저 아이디 이름 딕셔너리 만들어서 업데이트 해주기
마지막에 업데이트 된 이름으로 다 바꿔서 출력해주기
"""

def solution(record):
    ID = {}
    for i in record:
        i = i.split()
        # 유저 입장이나 이름 변경시에만 딕셔너리 업데이트
        if i[0] != "Leave": ID[i[1]] = i[2]
        
    answer = []
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            answer.append(ID[i[1]]+"님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(ID[i[1]]+"님이 나갔습니다.")
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
