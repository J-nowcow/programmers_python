# https://programmers.co.kr/learn/courses/30/lessons/68646
"""
각각의 풍선에 대해, 왼쪽 리스트의 최솟값과 오른쪽 리스트의 최솟값을 구해서 비교하자.
만약 두 최솟값보다 더 크다면 작은 숫자를 지우는 시행이 최소 두 번 필요하므로 불가능하다.
하나라도 더 작다면 나머지 숫자들을 지우고 최솟값만 남긴 다음 그 두개를 한 번 이내의 예외로 지울 수 있으므로 가능하다.
한편, 양 끝 값은 항상 가능하다는 것을 알 수 있다. 따라서 ans = 2에서 시작한다.

최솟값은 미리 계산해주고 사용하기!
총 O(n)*2 + O(n) = O(n) 시간에 해결 가능
"""

def solution(a):
    if len(a) == 1:
        return 1
    answer = 2
    left = [0] * len(a)
    right = [0] * len(a)
    rmin = lmin = 10**9
    for i in range(len(a)):
        lmin = min(lmin, a[i])
        left[i] = lmin
        rmin = min(rmin, a[-i-1])
        right[-i-1] = rmin
    
    for i in range(1,len(a)-1):
        if max(left[i-1], a[i], right[i+1]) != a[i]:
            answer += 1
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
