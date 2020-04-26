#https://programmers.co.kr/learn/courses/30/lessons/64065
"""
전체 숫자 개수가 100개 이하니까 그냥 대충 짜줘도 돌아감

튜플은 정렬이 되니까 그냥 정렬시켜서 출력하면 될 것 같은데
일단 정규표현식 써서 뽑아내는게 우선인듯

"""

import re

def solution(s):
    c = re.findall("[\d,]+", s) # ,랑 숫자 들어가는거 전부 추출
    # print(c) # ['2', ',', '2,1', ',', '2,1,3', ',', '2,1,3,4']
    numbers = []
    for i in c:
        n = re.findall("[\d]+", i)
        if len(n) > 0: # 숫자가 있는 경우 : ,만 있는 경우 제거하기
            tmp = [int(n[j]) for j in range(len(n))]
            # print(tmp) # [2, 1, 3, 4]
            numbers.append(sorted(tmp))
            
    numbers.sort(key = len) # 길이순대로 정렬
    # print(numbers) # [[2], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
    
    answer = [numbers[0][0]] # 맨 처음 값 넣어주기
    for n in numbers[1:]:
        tmp = sorted(answer)
        for i in range(len(tmp)):
            if tmp[i] != n[i]: # 정렬했으니까 두개 다르면 그 값이 새로운 값임
                answer.append(n[i])
                break
        else:
            answer.append(n[-1]) # 없으면 가장 마지막 값이 새로운 값이니까 넣어주기

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
