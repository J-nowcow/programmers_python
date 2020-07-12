# https://programmers.co.kr/learn/courses/30/lessons/12927
"""
전체 배열 크기의 합 구해서 재분배하기
근데 그 숫자보다 작은것들은 늘릴 수가 없으니까 빼고 재분배하기
-> 리스트 정렬한 다음에 총 작업시간 계산해두고 하나씩 빼가다가
그 리스트의 값이 남은 값 // 남은 개수 이상이 되면 break
5개 남았고, 12시간 남았으면 2시간 3개, 3시간 2개
remain // (len(works) - i) = 12 // 5 = 2
remain % tmp = 12 % 5 = 2
-> (remain // tmp) ** 2 * (tmp - remain % tmp) + (remain // tmp + 1) ** 2 * (remain % tmp)
"""
def solution(n, works):
    if sum(works) <= n: return 0
    answer = 0
    works.sort()
    remain = sum(works) - n
    tmp = len(works)
    for i in range(len(works)):
        if works[i] <= remain // tmp:
            remain -= works[i]
            tmp -= 1
            continue
        for j in works[:i]: answer += j**2
        return answer + (remain // tmp) ** 2 * (tmp - remain % tmp) + (remain // tmp + 1) ** 2 * (remain % tmp)

print(solution(10,[7,8,9]))
