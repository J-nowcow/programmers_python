# https://programmers.co.kr/learn/courses/30/lessons/70130
def solution(a):
    ans = 0
    dic = {}
    check = {}
    for i in range(len(a)):
        dic[i] = 0
        check[i] = -2 # (check[i], check[i+1]) 을 골라서 넣었다는 것 표시

    # i,i+1번 째 숫자가 서로 달라서 넣을 수 있다고 하자
    # 이때 n = a[i+1]을 넣을지 말지는 (a[i-1],a[i])를 골랐는지 여부에 따라 결정된다.
    # 만약 a[i-1] = n이고, (a[i-1],a[i])를 골라야 하는 상황이라면 i+1은 넣을 수 없음
    # 골라야 되는 상황: ① a[i-2] = a[i-1]인 경우
    # ② a[i-2]에서 고를 수 없는 상황이었던 경우

    # check = True: 넣을 수 있음 / check = False: 넣을 수 없음
    
    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            # 직전에 넣지 않은 경우에만 숫자 넣기
            if check[a[i]] != i-1:
                dic[a[i]] += 1
                check[a[i]] = i
            if check[a[i+1]] != i-1:
                dic[a[i+1]] += 1
                check[a[i+1]] = i
                
    return max(dic.values()) * 2

a = [0]
print(solution(a))
