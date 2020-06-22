#https://programmers.co.kr/learn/courses/30/lessons/12949
"""
행렬의 곱셈:

c[i][j] = a[i][0]*b[0][j] + ... + a[i][k]*b[k][j]
"""

def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for i in arr1]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = sum([arr1[i][a]*arr2[a][j] for a in range(len(arr2))])
    return answer
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1,arr2))
