#https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    d = [0]+[chr(65+i) for i in range(26)]
    i = 0
    answer = []
    while i < len(msg):
        t = 2
        # 사전에 더이상 안나올 때까지 글자 수 한글자씩 늘려가면서 탐색한다.
        while msg[i:i+t] in d:
            t+=1
            if i+t > len(msg): break
        # 사전에 추가하고 그 직전 글자까지의 인덱스 answer에 추가한다.
        answer.append(d.index(msg[i:i+t-1]))
        d.append(msg[i:i+t])
        i += t-1
    #print(d)

    return answer

msg = "ABABABABABABABAB"
print(solution(msg))
