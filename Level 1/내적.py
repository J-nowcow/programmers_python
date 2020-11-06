# https://programmers.co.kr/learn/courses/30/lessons/70128

solution = lambda a,b: sum([x*y for x,y in zip(a,b)])

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))
