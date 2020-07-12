#https://programmers.co.kr/learn/courses/30/lessons/60062
"""
친구 수 8명 이하 -> 1명부터 순서대로 되는지 확인해보자
15개를 적당히 사람 수대로 잘라서 되는지 확인하기
-> 15C0 + 15C1 + ... + 15C8개 확인해주면 됨
"""
import itertools
def solution(n, weak, dist):
    dist.sort(reverse = True)
    split = [str(i) for i in range(len(weak))]

    # 1명으로 다 되는지 확인
    # 약한 칸 사이의 거리가 가장 큰 부분 찾아서 n - 사이 거리 < dist[0]인지 체크
    if (n - max([weak[i+1]-weak[i] for i in range(len(weak)-1)] + [n - weak[-1] + weak[0]])) <= dist[0]: return 1

    # 2명일 때부터 되는지 친구 한명씩 증가시키면서 확인
    for i in range(2,len(dist)+1):
        # s: weak 리스트를 잘라줄 위치
        s = list(map(" ".join, itertools.combinations(split, i)))
        #print(s)
        for j in s:
            # check: s에 따라 i조각난 weak 리스트
            check = []
            # itertools가 문자로 잘려있어서 다시 숫자로 변환해준다.
            j = [int(a) for a in j.split()]
            #print(j)
            for k in range(len(j)-1): check.append(weak[j[k]: j[k+1]])
            check.append(weak[:j[0]]+weak[j[-1]:])
            #print(check)

            # length: 각 check list의 가장 먼 두 점 사이 거리
            # 좀 더 빠르게 하는 로직을 만들 수는 있지만 몇개 안되니까 그냥 삼중 for문
            length = [0]*len(check)
            for idx, a in enumerate(check):
                for b in range(len(a)):
                    for c in range(b,len(a)):
                        length[idx] = max(length[idx], min(a[c] - a[b], n - a[c] + a[b]))
            
            length.sort(reverse = True)
            #print(length)
            # 모든 length에 대해 가장 멀리 가는 친구부터 하나씩 매칭시켜서 전부 통과하면 return
            for a in range(len(length)):
                if length[a] > dist[a]: break
            else: return i
    return -1

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
print(solution(n,weak,dist))

n = 50
weak = [1,5,10,16,22,25]
dist = [3,4,6]
print(solution(n,weak,dist))
"""
import random
for i in range(100):
    n = random.randint(46,200)
    weak = sorted(random.sample(range(n), random.randint(10,15)))
    dist = random.sample(range(30), random.randint(5,8))
    print(n,weak,dist)
    print(solution(n,weak,dist))
"""
