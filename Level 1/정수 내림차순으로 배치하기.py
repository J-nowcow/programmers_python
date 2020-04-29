#https://programmers.co.kr/learn/courses/30/lessons/12933

solution = lambda n: int("".join(sorted([i for i in str(n)],reverse = True)))

print(solution(118372))
