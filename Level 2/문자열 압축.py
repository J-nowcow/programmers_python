# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s)== 1: return 1
    answer = 1001
    for i in range(1,len(s)//2+1):
        string = s[:i]; r = 1
        j = i; tmp = i
        while j <= len(s):
            # 반복된 경우
            if s[j:j+i] == string:
                r += 1
            else:
                if r > 1: tmp += len(str(r))
                r = 1
                tmp += len(s[j:j+i])
                string = s[j:j+i]
            j += i
        answer = min(tmp, answer)
    return answer

print(solution("abcabcabcabcdededededede"))
