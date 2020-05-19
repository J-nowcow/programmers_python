#https://programmers.co.kr/learn/courses/30/lessons/17687

import itertools
def solution(n,t,m,p):
    # n진법에서 사용할 숫자들
    num = "0123456789ABCDEF"[:n]
    # 불러야 하는 숫자 문자열
    string = num # 한자리 숫자 미리 넣어주기

    k = 1
    check = False
    while len(string) < m*t:
        a = num[1:] # 첫자리는 0이 될 수 없음
        b = list(map("".join, (itertools.product(num, repeat = k)))) # 나머지 자리 조합
        for i in a:
            for j in b:
                string += i; string += j
                # 충분히 다 만들었다면 break해준다.
                if len(string) >= m*t: check = True; break
            if check: break
        k += 1
        #print(k, len(string), m*t, len(b))
    #print(string)
    return "".join([string[p-1+m*i] for i in range(t)])

n=16;t=1000;m=2;p=2
import random
while 1:
    n = random.randint(2,16)
    t = random.randint(1,1000)
    m = random.randint(2,100)
    p = random.randint(1,m)
    print(n,t,m,p)
    print(solution(n,t,m,p))
print(solution(n,t,m,p))
