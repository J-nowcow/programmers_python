"""
def solution(n,arr1,arr2):
    answer = []
    map1 = [] # 첫번째 지도
    for i in arr1:
        line = ""
        for _ in range(n):
            line += " #"[i%2] # 2로 나눈 값이 0이면 공백, 1이면 # 넣어줌
            i//=2
        map1.append(line[::-1]) # 뒤집어서 넣어줘야 이진법이 처리됨

    map2 = [] # 두번째 지도도 똑같이 반복
    for i in arr2:
        line = ""
        for _ in range(n):
            line += " #"[i%2]
            i//=2
        map2.append(line[::-1])
        
    for i in range(n): # 두 지도 탐색해서 answer 만들기
        line = ""
        for j in range(n):
            if map1[i][j] == "#" or map2[i][j] == "#": # 하나라도 벽이면 #
                line += "#"
            else: line += " " #아니면 공백
        answer.append(line)
    return answer
"""
def solution(n,arr1,arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        line = ""
        for _ in range(n):
            line += " #"[i%2+j%2 > 0] # 둘 중 하나라도 벽이면 #, 아니면 0
            i//=2; j//=2
        answer.append(line[::-1]) # 이진법 계산한거니까 거꾸로 넣어줘야 함
    return answer

n=5; arr1= [9, 20, 28, 18, 11]; arr2= [30,1,21,17,28]
print(solution(n,arr1,arr2))
