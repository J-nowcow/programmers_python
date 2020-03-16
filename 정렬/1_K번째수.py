#https://programmers.co.kr/learn/courses/30/lessons/42748
"""
주어진 배열의 i~j번째 인덱스만 뽑아서 정렬시킨 다음 k번째 원소 뽑아내는 문제
"""
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
