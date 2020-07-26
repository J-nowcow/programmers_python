# https://programmers.co.kr/learn/courses/30/lessons/42891
"""
food_times 정렬한 리스트 만들어놓고
가장 양 적은 음식부터 하나씩 빼가면서 얼마나 남았는지 확인하기
총 먹은 양이 K가 되는 시점에서 stop
"""

def solution(food_times, k):
    # k가 먹을 음식 양보다 크면 바로 return
    if sum(food_times) <= k: return -1

    a = sorted(food_times)
    # s: 총 먹은 양 = 시간
    s = len(a) * a[0]
    if s <= k:
        for i in range(1,len(a)):
            # 이번 사이클에 먹을 양: (len(a) - i)*(a[i] - a[i-1])
            s += (len(a)-i) * (a[i] - a[i-1])
            if s > k: break
        # a[i-1] 번째 음식과 a[i] 번째 음식 사이에서 연결이 끊김
        s -= (len(a)-i) * (a[i] - a[i-1]); t = i-1
    else:
        # 첫 음식도 다 못먹고 끊기는 경우 예외처리
        return k % len(a) + 1
    
    # 하나 전 사이클로 돌려주면 먹어야 할 남은 양: k-s, 남은 음식 개수 len(a) - t + 1 (이러면 중복 처리됨)
    # 새로운 리스트 만들어서 더 큰 값만 넣어준다.
    # 그 리스트에서 (k-s) % len(lst) 번 째 원소를 리턴한다.
    
    # print(k,s,len(a),t,(k-s)%(len(a)-t + 1))
    lst = []
    for i in range(len(a)):
        if food_times[i] > a[t]: lst += [i]
    return lst[(k-s) % len(lst)] + 1

"""
import random
for i in range(10):
    food_times = [random.randint(10,99) for i in range(10)]
    k = random.randint(10,500)
    print(solution(food_times,k))"""

print(solution([3,4,2,2,2,2],14))
