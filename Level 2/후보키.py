#https://programmers.co.kr/learn/courses/30/lessons/42890
"""
속성 최대 8종류, 인원 최대 20명
8! * 20 = 40320 * 20 = 806400이니까 브루트 포스로 구현 가능
"""

import itertools
def solution(relation):
    properties = [str(i) for i in range(len(relation[0]))]
    answer = []

    # 1가지 속성으로 되는 경우부터 하나씩 판단한다.
    for i in range(1, len(properties) + 1):
        choice = list(map("".join, itertools.combinations(properties,i)))
        
        # 각각의 속성 조합에 대해 확인
        for case in choice:
            # 확인 방법: 전체를 다 이어붙인 문자열들로 set 만들어서 중복 판단
            string = []
            for info in relation:
                string.append("".join([info[int(a)] for a in case]))
                
            # 중복 없는 경우
            if len(string) == len(set(string)):
                # 최소성 만족하는지 체크해준다.
                check = True
                # 지금 확인한 case의 부분집합 만들어주기
                for i in range(1, len(case) + 1):
                    tmpset = list(map("".join, itertools.combinations(case, i)))
                    for j in tmpset:
                        if j in answer:
                            # 부분집합이 이미 answer에 있으면 break
                            check = False; break
                    if check == False:break
                if check:
                    answer.append(case)
                
    return len(answer)

relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
