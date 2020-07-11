# https://programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    A.sort(); B.sort()
    a = 0; b = 0
    answer = 0
    while a<len(A) and b<len(B):
        if A[a] < B[b]: answer += 1; a += 1
        b += 1
    return answer
A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A,B))
