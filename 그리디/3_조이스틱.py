# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    # 위아래 횟수
    answer = sum([min(ord(i)-65,91-ord(i)) for i in name])
    # 양옆 횟수: 언제 턴하는지 싹다 해보기
    a = len(name)-1
    i = 0
    while i < len(name):
        if name[i] == "A":
            tmp = i
            while name[tmp] == "A":
                tmp += 1
                if tmp == len(name): break
            a = min(a, (i-1)*2+len(name)-tmp)
        i += 1
    return answer+a

print(solution("JEROEN"))
