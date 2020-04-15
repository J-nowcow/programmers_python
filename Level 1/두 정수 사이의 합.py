#https://programmers.co.kr/learn/courses/30/lessons/12912
solution = lambda a,b:max(a,b)*(max(a,b)+1)//2 - min(a,b)*(min(a,b)-1)//2
print(solution(-3,5))
