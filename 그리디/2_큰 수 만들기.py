#https://programmers.co.kr/learn/courses/30/lessons/42883
"""
주어진 숫자에서 k개의 수 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기
n이 100만이므로 nlogn 문제
그리디 파트니까... 1개 없앨 때마다 가장 큰 숫자 날려주면 해결될 거긴 한데
어떻게 그게 성립하는지 수학적으로 알 필요가 있음 근데 자명한가

+) 스택으로 구현해줘야 제대로 된 nlogn 풀이임
(문자열 스플라이싱은 O(n)이므로 튕겨야 하지만 시간 안에 들어옴)
"""

def solution(number, k):
    n = len(number)
    check = 0
    for i in range(k):
        print(number, check, n-i-1)
        for j in range(check, n - i - 1):
            if number[j] < number[j+1]: # 만약 뒷자리가 더 크다면
                number = number[:j] + number[j+1:] # 그 자리를 날려주는게 가장 큼
                check = max(0,j-1) # 다음번 체크에서는 이 자리부터 확인해주면 됨
                break
        else: # 더이상 없으면 = 숫자가 9861처럼 내림차순이면
            return number[:n-k] # 그냥 남은거 앞에서 잘라서 리턴
        
    return number


number = "1264978"
k = 6
print(solution(number, k))
