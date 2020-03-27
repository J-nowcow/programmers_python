#https://programmers.co.kr/learn/courses/30/lessons/42897
"""
인접한 두 집을 털지 않게 하면서 최댓값 찾기
집 1 2 3 셋 중 하나는 무조건 털어야 최댓값이 나온다는 것을 관찰 가능
(셋다 안털면 2번을 터는 것보다 무조건 작은 값이 나오기 때문)
따라서 리스트 3개 만들어서 각각 판단해주고, 그거의 최댓값 구하기
첫 지점만 고정해주면 그냥 피보나치처럼 돌릴 수 있음

n번 째 지점 탐색해줄 때
max(n-1번 째 지점까지의 최댓값, n-2번 째 지점까지의 최댓값 + n번째 지점)

얘도 렙4는 아닌데... 저번에 풀었던것보다 훨씬 쉬운데....
"""

def solution(money):
    # dp 3개 만들고 각각 계산해주기
    k = len(money); a = [money[0]]*2 ; b = [money[1]]*2 ; c = [money[2]]*2
    for i in range(k-3):
        # 마지막칸이 최댓값이라면
        # 막칸은 어차피 못먹기 때문에 그 두칸 전에 같은 값 들어있음
        
        a.append(max(a[-1], a[-2]+ money[(i+2)%k]))
        b.append(max(b[-1], b[-2]+ money[(i+3)%k]))
        c.append(max(c[-1], c[-2]+ money[(i+4)%k]))
    return max(max(a),max(b),max(c))

money = [1,2,3,1]
print(solution(money))
