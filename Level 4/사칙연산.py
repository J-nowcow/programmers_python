# https://programmers.co.kr/learn/courses/30/lessons/1843
"""
+: (최댓값) + (최댓값) / (최솟값) + (최솟값)
-: (최댓값) - (최솟값) / (최솟값) - (최댓값)
숫자가 1개일 때부터 n개일 때까지 dp

i~j까지의 숫자의 최댓값은
i/i+1~j, i~i+1/i+2~j, ... , i~j-1/j로 자르는 방법 각각 계산해서 그중에 최댓값
"""

def solution(arr):
    # 문자 숫자로 바꿔주기
    arr = [int(arr[i]) if i % 2 == 0 else arr[i] for i in range(len(arr))]
    num = len(arr)//2 + 1
    # cmax[i][j]: i번 째 숫자부터 j번 째 숫자까지의 연산의 최댓값
    cmax = [[-10**6]*num for i in range(num)]
    cmin = [[10**6]*num for i in range(num)]

    for i in range(num):
        cmax[i][i] = arr[i*2]
        cmin[i][i] = arr[i*2]
    
    for c in range(1,num): # c번의 연산: c+1개의 숫자
        for i in range(num-c): # 0~i부터 num-i ~ num 까지
            j = c + i # 즉, i부터 j까지 숫자의 연산
            for k in range(i,j):
                print(i,j,k)
                if arr[k*2+1] == "+":
                    cmax[i][j] = max(cmax[i][k] + cmax[k+1][j], cmax[i][j])
                    cmin[i][j] = min(cmin[i][k] + cmin[k+1][j], cmin[i][j])
                else:
                    cmax[i][j] = max(cmax[i][k] - cmin[k+1][j], cmax[i][j])
                    cmin[i][j] = min(cmin[i][k] - cmax[k+1][j], cmin[i][j])

    for i in cmax:
        for j in i:
            print("%8d"%j,  end = " ")
        print()
    for i in cmin:
        for j in i:
            print("%8d"%j,  end = " ")
        print()
    return cmax[0][-1]

arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
print(solution(arr))
