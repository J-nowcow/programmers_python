# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    s = set(gems)
    d = {}
    for i in list(s):
        d[i] = 0
    
    check = 0
    answer = 1000000
    x = 0; y = 0
    a = [0,0]
    while y < len(gems):
        if check == len(s):
            if answer > y-x:
                answer = y-x
                a = [x+1,y]
            d[gems[x]] -= 1
            if d[gems[x]] == 0: check -= 1
            x += 1
        else:
            if d[gems[y]] == 0: check += 1
            d[gems[y]] += 1
            y += 1
    while check == len(s):
        if answer > y-x:
            answer = y-x
            a = [x+1,y]
        d[gems[x]] -= 1
        if d[gems[x]] == 0: break
    return a

gems = ["DIA","RUBY", "RUBY", "DIA", "DIA", "EMERALD","DIA", "SAPPHIRE", "DIA"]
print(solution(gems))
