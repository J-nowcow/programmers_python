# https://programmers.co.kr/learn/courses/30/lessons/42583
import queue
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = queue.Queue() # 트럭의 무게 저장해주는 Queue
    t = [0] * len(truck_weights) # 트럭이 들어오는 시간 저장해주는 리스트
    idx = 0; w = 0 # 몇 번째 트럭인지 인덱스, q에 있는 트럭의 무게 총합
    while True:
        while w+truck_weights[idx] <= weight:
            q.put(truck_weights[idx])
            t[idx] = time
            w += truck_weights[idx]
            time += 1
            idx += 1
            if time == bridge_length + t[idx - q.qsize()]:
                w -= q.get()
            if idx == len(truck_weights):
                return time + bridge_length
           
        time = t[idx - q.qsize()] + bridge_length 
        w -= q.get()
        

print(solution(11,10,[2,4,3,6,1,8,9,1,4,6]))
