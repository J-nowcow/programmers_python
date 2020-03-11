def solution(arrangement):
    stack = 0
    answer = 0
    for i in range(len(arrangement)):
        if arrangement[i] == "(": stack += 1
        else:
            stack -= 1
            if arrangement[i-1] == "(": answer += stack # 레이저면 자른만큼 추가
            else: answer +=1 # 아니면 막대기 하나 끝난거니까 1 추가
    return answer

print(solution("()(((()())(())()))(())"))
