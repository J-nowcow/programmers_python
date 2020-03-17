#https://programmers.co.kr/learn/courses/30/lessons/42842
"""
빨간 카펫을 갈색 카펫이 둘러싸고 있는 형태
( 빨간 카펫의 가로길이 + 빨간 카펫의 세로 길이 ) * 2 + 4가 갈색 카펫의 수
소인수분해 해서 하나씩 계산해보면 될 듯

red가 2000000 이하이고 brown이 5000 이하이므로 brown으로 계산하는 게 더 작을듯

빨강 카펫의 수 = (갈색 카펫의 수 - 4) // 2 를 적당히 a, n-a로 나눈 것
계산 5000번 이내로 해결 가능
"""

def solution(brown, red):
    n = (brown - 4) // 2
    for i in range(1,n):
        if i * (n-i) == red:
            return [n-i+2, i+2]

brown = 8; red = 1
print(solution(brown, red))
