#https://programmers.co.kr/learn/courses/30/lessons/42839
"""
숫자 7개 받아서 소수 되는지 판별하는 문제
에라토스테네스 체 만들어서 하는게 젤 편할듯 --> 그냥 각각 판별해줘도 돌아간다함
--> 에라토스테네스 하면 오히려 타임리밋 걸리는듯
import itertools itertools.permutation 하면 순열 구해줌
"""

import itertools

def solution(numbers):
    numbers = ",".join(numbers).split(",") #스플릿이랑 조인써서 리스트 변환
    print(numbers)
    num_list = []
    for i in range(len(numbers)):
        num_list += list(map(''.join, itertools.permutations(numbers, i+1)))
    # itertools.permutations(list, n): 리스트에서 n개의 아이템 조합
    # map으로 저렇게 싸주면 각 원소들 하나의 문자열로 바꿔주고 list 변환 가능
    
    num_list = list(map(int,num_list)) # 문자열에서 숫자로 바꿔주기
    num_list = list(set(num_list)) # set은 중복을 안받으므로 중복 날려줌

    #print(num_list)
    answer = 0
    for n in num_list:
        if n <= 1: continue # 0하고 1이 안걸러져서 예외처리
        
        for i in range(2, round(n ** 0.5) + 1): # 절반 + 1까지 확인
            if n%i == 0:break # 나눠지면 합성수
        else: answer += 1; # 이렇게 if랑 else 문 위치 달라도 쓸 수 있음
        # 마지막 for문에서 if를 체크해서 else를 인식해주는듯..?
        
    return answer
    """
    prime_list = [ i+1 for i in range(1,max(num_list)) ] #에라토스테네스 체
    for i in prime_list:
        for j in prime_list:
            if i != j and j%i == 0: #순환하면서 배수이면 삭제
                prime_list.remove(j)
    answer = 0    
    for i in num_list:
        if i in prime_list:
            answer += 1"""
    

numbers = "011"
print(solution(numbers))
