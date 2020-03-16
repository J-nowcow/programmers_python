#https://programmers.co.kr/learn/courses/30/lessons/42747
"""
논문의 H-index 구하는 문제
H-Index: h번 이상 인용된 논문이 h편 이상일 때 h의 최댓값
논문 1000편 이하 인용 횟수 10000회 이하 --> O(mn)으로도 돌아갈 듯
정렬이 O(nlogn) 먹으니까 O(nlogn + n)으로 구현하기
"""

def solution(citations):
    citations.sort(reverse = True)
    n = len(citations)
    for i in range(n): # 큰것 부터 하나씩 체크하기
        #print(i, n-i, citations[i])
        if citations[i] <= i:# 논문의 인용 횟수가
            return i  #인덱스보다 작으면 그때의 인덱스가 최댓값
    return n # 만약 끝까지 더 크면 전체 값이 최댓값

citations = [0,0,1,2,2,5,6,7,7,7,8,8,8,8,8,10]
print(solution(citations))
