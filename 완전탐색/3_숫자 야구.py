#https://programmers.co.kr/learn/courses/30/lessons/42841
"""
3자리수 숫자야구 문제
그냥 3자리수 싹다 만든다음에 하나씩 확인해주기
비교해가면서 짤 수 있을 것 같긴 한데 어려울듯
"""
import itertools

def solution(baseball):
    answer = 0
    numbers = [str(i) for i in range(1,10)]
    num_list = list(map("".join, itertools.permutations(numbers, 3)))
    # num_list: 123 ~ 987까지 3자리 자연수
    for check in num_list: # 체크할 숫자
        for n, s, b in baseball: # 숫자, 스트라이크, 볼
            ts, tb = 0, 0
            n = str(n)
            for i in range(3):
                if n[i] == check[i]: # 위치 같으면 스트라이크
                    ts += 1
                elif n[i] in check: # 다르지만 있으면 볼
                    tb += 1
            if ts != s or tb != b:
                break
        else: answer += 1
    return answer

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))
