# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    ans = [0,0]
    while s != "1":
        ans[0] += 1
        ans[1] += s.count("0")
        s = bin(s.count("1"))[2:]
    return ans

print(solution("110010101001"))
