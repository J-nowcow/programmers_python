# https://programmers.co.kr/learn/courses/30/lessons/12936
"""
(k-1) // (n-1)! = 0,1,2,...,(n-1)
남아있는 숫자 리스트에서 (k-1) // (n-1)! + 1 번째 수 ( (k-1)//(n-1)! 번째 인덱스 )
k -> k % (n-1)!, n-1 -> n-2
마지막 자리까지 반복
"""
def solution(n,k):
    a = list(range(1,n+1))
    answer = []
    f = 1
    for i in range(1,n): f *= i
    for i in range(n-1,0,-1):
        tmp = (k-1) // f
        answer.append(a[tmp])
        del a[tmp]
        k %= f
        f //= i
    return answer+a

print(solution(3,5))
