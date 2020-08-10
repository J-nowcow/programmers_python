# https://programmers.co.kr/learn/courses/30/lessons/42584
"""
prices를 받아서 가장 먼저 자기보다 작아지는 가격이 언제 나오는지 찾는 문제
prices가 100000이므로 nlogn으로 구현해야 하지만, 잘 짜면 n^2로도 돌아간다 함
O(n) 풀이: 스택에 시간을 하나씩 넣어주기
그 값보다 더 크거나 같은 값이 들어오면 스택에 쌓기
더 작은 값이 들어오면 자기보다 작은 값까지 스택에서 빼주고
answer에 추가해주기

for문 안에 while문이 중첩이지만
stack에 최대 들어갈 수 있는 값의 개수의 합도 n개이고
빼내는 값의 개수의 합도 n개니까
O(n+n+n) = O(3n)으로 해결 가능
"""

def solution(prices):
    n = len(prices)
    answer = [0] * n
    s = []
    for i in range(n):
        while s and prices[s[-1]] > prices[i]: # 입력받은 값이 더 작은 경우
            t = s.pop() # 더 커질 때까지 스택의 마지막 값 빼서
            answer[t] = i - t # n번째 값의 답은 지금 들어온 시간 - 원래 시간
        s.append(i) # 스택에 현재 시간 저장

    while s: # 남아있는 스택 처리해주기
        t = s.pop() # t번째 값은 끝까지 더 작은게 안들어온거니까
        answer[t] = n - 1 - t # 시간 계산해서 저장해주기
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
