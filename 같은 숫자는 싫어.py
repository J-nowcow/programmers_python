#https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]
    for i in arr[1:]:
        if answer[-1] != i: answer+=[i]
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
