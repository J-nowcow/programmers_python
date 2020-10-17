# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    ans = [0,0]
    check = [(0,0,len(arr))]
    while check:
        x,y,n = check.pop()
        tmp = [0,0]
        for i in arr[x:x+n]:
            if 1 in i[y:y+n]:
                tmp[1] = 1
            if 0 in i[y:y+n]:
                tmp[0] = 1
            if tmp == [1,1]: break
        if tmp == [1,1]:
            n //= 2
            check += [(x,y,n), (x+n,y,n), (x,y+n,n), (x+n,y+n,n)]
        elif tmp == [0,1]:
            ans[1] += 1
        else:
            ans[0] += 1
    return ans

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
