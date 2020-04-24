#https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    if n==0: return 0
    a = {}
    i = 2
    while i<=n:
        if n%i == 0:
            n//=i
            if i in a: a[i]+=1;
            else: a[i] = 1
        else: i+=1
    answer= 1
    for i in a:
        answer *= (i**(a[i]+1)-1)//(i-1)
    return answer

print(solution(0))
