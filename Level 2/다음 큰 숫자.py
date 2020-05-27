#https://programmers.co.kr/learn/courses/30/lessons/12911
"""
2진수 변환한 다음 1의 자리부터 탐색하기
"01" 나올때까지 탐색하고 "10"으로 바꾸기
"10" 전에 나온 0의 개수 세서 001111으로 바꿔주기
1001110 -> 10"10"110 -> 1010"011"

01이 한번도 안나오면 1 + (0의 개수 + 1) + (1의 개수 -1)
11110 -> 100111
"""

def solution(n):
    t = bin(n)[2:]
    check = 0
    for i in range(len(t)-1,0,-1):
        if t[i-1:i+1] == "01":
            return int(t[:i-1] + "10" + "0"*check + "1"*(len(t)-i-check-1), 2)
        check += t[i] == "0" # 0의 개수 세주기
    return int("1"+"0"*(1+t.count("0"))+"1"*(t.count("1")-1), 2) 
print(solution(15))
