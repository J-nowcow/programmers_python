#https://programmers.co.kr/learn/courses/30/lessons/12932

solution = lambda n: [int(str(n)[i]) for i in range(len(str(n)))][::-1]

print(solution(12345))
