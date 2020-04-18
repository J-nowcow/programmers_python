#https://programmers.co.kr/learn/courses/30/lessons/12918

solution = lambda s: (len(s)== 4 or len(s) == 6) and s.isdigit()

print(solution("1234"))
