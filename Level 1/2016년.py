#https://programmers.co.kr/learn/courses/30/lessons/12901

solution = lambda a,b: (["THU","FRI","SAT","SUN","MON","TUE","WED"][(sum([31,29,31,30,31,30,31,31,30,31,30,31][:a-1])+b)%7])

a=5
b=24
print(solution(a,b))
