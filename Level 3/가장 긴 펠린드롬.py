# https://programmers.co.kr/learn/courses/30/lessons/12904
"""
길이 2500밖에 안되니까 처음부터 끝까지 브루트포스
두가지 탐색: i == i+1인 경우, i 혼자인 경우
"""

def solution(s):
    answer = 0
    for i in range(len(s)):
        # 홀수 개짜리 펠린드롬
        j = 1
        while 0 <= i-j and i+j < len(s) and s[i-j]==s[i+j]: j += 1
        answer = max(answer, j*2-1)
        if i+1<len(s) and s[i] == s[i+1]: # 짝수 개짜리 펠린드롬
              j = 1
              while 0 <= i-j and i+j+1 < len(s) and s[i-j]==s[i+j+1]: j += 1
              answer = max(answer, j*2)
    return answer

print(solution("addacde"))
