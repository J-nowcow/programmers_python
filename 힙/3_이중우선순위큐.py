# https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq as hq

def solution(operations):
    minh = []
    for i in operations:
        if i[0] == "I":
            hq.heappush(minh, int(i[2:]))
            
        elif minh:
            if i[2] == "1":
                minh.remove(max(minh))
            else:
                hq.heappop(minh)
    if not minh: answer = [0,0]
    else: answer = [max(minh),min(minh)]
    return answer

operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))
