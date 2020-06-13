#https://programmers.co.kr/learn/courses/30/lessons/12909
"""
스택에 하나씩 넣고 빼주기: 그냥 숫자로 해줘도 돌아감
"""
def solution(s):
    stack = 0
    for i in s:
        if i == "(": stack+=1
        elif stack == 0: return False
        else: stack -=1
    return stack == 0
s = "()()"
print(solution(s))
