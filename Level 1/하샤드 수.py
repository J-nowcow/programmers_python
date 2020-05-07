#https://programmers.co.kr/learn/courses/30/lessons/12947

solution = lambda x: x%sum([int(i) for i in str(x)]) == 0

print(solution(10))
