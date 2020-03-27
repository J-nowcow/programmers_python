import re

def solution(dartResult):
    s = dartResult
    score = re.findall("\d+",s) # 숫자만 뽑아서 리스트 저장
    bonus = re.findall("[SDT]",s) #배수 뽑아서 리스트 저장

    answer = [0,0,0]
    for i in range(3):
        
        answer[i] = int(score[i])
        
        if bonus[i] == "D": #보너스 처리
            answer[i]**= 2
        elif bonus[i] == "T":
            answer[i]**= 3
            
        s = s[len(score[0])+1:] # 다 쓴 문자열 잘라서 옵션 처리하기 쉽게 바꾸기
        if s: #옵션 처리
            if s[0] == "*": 
                answer[i] *= 2
                if i > 0: answer[i-1] *=2
                s = s[1:]
                
            elif s[0] == "#":
                answer[i] *= -1
                s = s[1:]
    return sum(answer)

while 1:
    print(solution(input()))
