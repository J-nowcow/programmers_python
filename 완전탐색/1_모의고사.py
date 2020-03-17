#https://programmers.co.kr/learn/courses/30/lessons/42840
"""
1번: "12345"[n%5]로 찍음
2번: "21232425"[n%8]로 찍음
3번: "31245"[n%10//2]로 찍음
"""

def solution(answers):
    answer = [0]*3
    for n, v in enumerate(answers):
        if str(v) == "12345"[n%5]: answer[0]+=1
        if str(v) == "21232425"[n%8]: answer[1]+=1
        if str(v) == "31245"[n%10//2]: answer[2]+=1
    return [i+1 for i in range(3) if answer[i] == max(answer)]

answers = [1,2,3,4,5]
print(solution(answers))
