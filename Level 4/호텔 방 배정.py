#카카오 코테 실전 4번
# m시 nn분 해결
"""
k를 10^12로 줘버리는 카카오....
room_number 사이즈가 20만이니까 각 탐색을 1000번 이내에 해내야함
빈 방 리스트를 만들 수는 없고
차있는 방 리스트를 만드는게 최선일듯
"""

def solution(k,room_number):
    room = {} # 각 사람이 가리키고 있는 방 번호를 저장해줄 것임
    answer = []
    for i in room_number: # 각 사람에 대해서
        tmp = i
        a_list = [tmp]
        while tmp in room: # 그 번호가 room 딕셔너리에 있다면
            tmp = room[tmp] # 그 방이 가리키는 딕셔너리 값으로 바꿔주기
            a_list.append(tmp) # 임시 리스트에 추가
            
        for j in a_list:
            room[j] = tmp + 1 # 지금 탐색한 것들 위치 값 다음 빈 방 번호로 바꾸기
        answer.append(tmp) # 정답 리스트에 추가
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k,room_number))
