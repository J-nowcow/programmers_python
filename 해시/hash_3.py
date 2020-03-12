from functools import reduce
def solution(clothes):
    d = {}
    for a,b in clothes:
        if b in d: d[b]+=1
        else: d[b] = 2
    return reduce(lambda x,y: x*y, list(d.values())) - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
