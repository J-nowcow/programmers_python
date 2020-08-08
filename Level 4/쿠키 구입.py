# https://programmers.co.kr/learn/courses/30/lessons/49995
"""
각각의 m에 대해서 왼쪽이 작으면 l 1 빼고, 오른쪽이 크면 r 1 더하기 반복
같다면 answer 업데이트 해주고 양쪽 다 한칸씩 늘리기
"""
def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        l = m; r = m+1
        a = cookie[m]; b = cookie[m+1]
        while True:
            # 양쪽 개수 같은 경우
            if a == b:
                answer = max(answer,a)
                if l == 0 or r == len(cookie)-1: break
                l -=1; r += 1
                a += cookie[l]; b += cookie[r]
            elif a < b:
                if l == 0: break
                l -= 1; a += cookie[l]
            else:
                if r == len(cookie)-1: break
                r += 1; b += cookie[r]
    return answer

print(solution([1,1,2,3]))
