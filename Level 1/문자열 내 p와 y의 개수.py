#https://programmers.co.kr/learn/courses/30/lessons/12916

solution = lambda s: s.lower().count("p") == s.lower().count("y")

s = "pPoooyY"
print(solution(s))
