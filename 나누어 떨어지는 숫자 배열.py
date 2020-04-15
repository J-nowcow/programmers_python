#https://programmers.co.kr/learn/courses/30/lessons/12910


solution = lambda arr,divisor:sorted([i for i in arr if i%divisor == 0]) or [-1]
arr = [2,36,1,3]
divisor = 1
print(solution(arr,divisor))
