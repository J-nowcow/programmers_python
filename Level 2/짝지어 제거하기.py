# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for i in s:
        if stack and stack[-1] == i: stack.pop()
        else: stack.append(i)
    return int(len(stack) == 0)
print(solution("baabaa"))
