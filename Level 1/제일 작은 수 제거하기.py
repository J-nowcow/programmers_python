#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    m = min(arr)
    while m in arr:
        arr.remove(m)
    return arr or [-1]

arr = [1,1,1]
print(solution(arr))
