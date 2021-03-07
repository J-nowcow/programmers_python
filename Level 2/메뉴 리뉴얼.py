#https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools
def solution(orders, course):
    answer = []
    orders = [sorted(i) for i in orders]
    for n in course:
        dic = {}
        for order in orders:
            for c in list(itertools.combinations(order, n)):
                tmp = "".join(c)
                if tmp in dic: dic[tmp] += 1
                else: dic[tmp] = 1
        if len(dic) == 0: continue
        max_c = max(dic.values())
        if max_c == 1: continue
        for i in dic.items():
            if i[1] == max_c:
                answer.append(i[0])
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
