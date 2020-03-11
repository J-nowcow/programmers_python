
def solution(heights):
    answer = []

    for i, v in enumerate(heights):
        t = 0
        for j in range(i-1,-1,-1):
            if heights[j] > v:
                answer += [j+1]; t=1; break
        if t==0 : answer += [0]
    return answer
    
print(solution([6,9,5,7,4]))
