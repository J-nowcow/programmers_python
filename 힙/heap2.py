"""
def search(list, i):
    min = 0; max = len(list) - 1; mid = 0
    while min <= max:
        mid = (min+max)//2
        if list[mid] < i:
            min = mid+1
        else: max = mid-1
    return min

def solution(stock, dates, supplies, k):
    answer = 0
    s = []
    for i in range(k):
        if i in dates:
            value = supplies[dates.index(i)]
            mid = search(s, value)
            s = s[:mid] + [value] + s[mid:]
        if stock == 0:
            stock += s[-1]
            s.pop()
            answer+=1
        stock -= 1
    return answer
"""

import heapq as hq
def solution(stock, dates, supplies, k):
    answer = 0; s = []
    for i in range(len(dates)):
        while stock+1 <= dates[i]: stock -= hq.heappop(s); answer += 1
        hq.heappush(s, -supplies[i])
        if stock >= k: return answer
    
    while stock < k: stock -= hq.heappop(s); answer+=1
    return answer
print(solution(4, [4, 10, 15], [20, 5, 10], 30))
