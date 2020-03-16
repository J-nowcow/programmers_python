# https://programmers.co.kr/learn/courses/30/lessons/42746

"""
숫자들을 이어붙여서 만들 수 있는 가장 큰 수를 찾는 문제
정렬할 때 비교하는 방법을 잘 지정해줘야 함
"""
"""
def solution(numbers):
    return "0" if max(numbers) == 0 else "".join(sorted(list(map(str,numbers)),reverse=True,key=lambda x: x*3))
"""
#한줄짜리 코드: 그냥 숫자를 3번 반복시켜서 비교하도록 key에 바로 넣어줬음


"""
import random
def q_sort(list, start, end):
    n = len(list)
    print(list, start, end)
    if start < end:
        s = [] ; e = []
        pivot = random.randint(0,n-1)
        for i in range(n):
            if i == pivot: pass
            elif list[i][0]+list[pivot][0] < list[pivot][0]+list[i][0]:
                e.append(list[i])
            else: s.append(list[i])
        list = s + [list[pivot]] + e
        q_sort(list, start, pivot - 1)
        q_sort(list, pivot+1, end)
    return list
"""
# 퀵정렬로 짜려고 했는데 터진다 왜그렇지

def solution(numbers):
    if max(numbers) == 0: return "0" # 다 0인 경우 예외처리
    return "".join(m_sort(list(map(str,numbers)))) 

def m_sort(list): # 병합정렬 구현
    if len(list) <= 1: return list # 한칸이면 리턴하고 아니면 재귀
    mid = len(list)//2
    return merge(m_sort(list[:mid]), m_sort(list[mid:]))

def merge(left, right):
    result = []
    i=0; j=0
    l = len(left); r = len(right)
    while l > i and r > j:
        if left[i] + right[j] > right[j] + left[i]: #sort할 때 17이랑 23 있으면
            # 12랑 21중에 21이 더 크니까 23이 17보다 앞으로 가도록 정렬
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
    
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
