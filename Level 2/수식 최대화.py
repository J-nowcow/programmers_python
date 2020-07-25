# https://programmers.co.kr/learn/courses/30/lessons/67257

"""
정규표현식 -> +, -, * 기준으로 분할
6가지 방법 계산해서 최댓값 출력하기
"""

import re
def solution(expression):
    lst = re.split("([*+-])",expression)
    order = ("+-*","+*-","*-+","*+-","-+*","-*+")
    answer = 0
    for a in order:
        tmp = lst[::]
        for char in a:
            i = 1
            while i+1 < len(tmp):
                if tmp[i] == char:
                    tmp = tmp[:i-1]+[str(eval("".join(tmp[i-1:i+2])))]+tmp[i+2:]
                else:
                    i += 2
        answer = max(answer, abs(int(tmp[0])))
    return answer

print(solution("100-200*300-500+20"))
