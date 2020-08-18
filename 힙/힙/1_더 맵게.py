# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2: return -1
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
        
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
