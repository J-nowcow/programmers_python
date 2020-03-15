# https://programmers.co.kr/learn/courses/30/lessons/42576
"""
participant: 마라톤에 참여한 선수들 이름 담긴 배열
completion: 완주한 선수들 이름 담긴 배열
참여한 선수의 수 100000명 이하 --> nlogn 구현 문제
completion의 길이가 participant보다 1 작음
각각 정렬하고 하나씩 비교하면서 다른 값 찾기
"""

def solution(participant, completion):
    participant.sort(); completion.sort() #정렬하고
    for i in range(len(participant)):
        if i != len(completion) and participant[i] == completion[i]: pass
        else: return participant[i] #비교하면서 다르면 리턴

participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]
print(solution(participant, completion))
