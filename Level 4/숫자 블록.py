# https://programmers.co.kr/learn/courses/30/lessons/12923
"""
가장 큰 약수 찾기
숫자 10000개니까 O(n^(3/2))면 다 탐색 가능
"""
def solution(begin, end):
    answer = []
    for n in range(begin,end+1):
        if n == 1: answer.append(0)
        else:
            a = 1
            for i in range(2,round(n**0.5)+1):
                if n % i == 0 and n // i <= 10000000:
                    a = n//i
                    break
            answer.append(a)
    return answer

print(solution(1,10))
