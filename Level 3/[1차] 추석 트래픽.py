# https://programmers.co.kr/learn/courses/30/lessons/17676
"""
lines [시작 시간, 종료 시간] 으로 전처리한 다음 딕셔너리에 {시간: 인덱스}로 넣기
s[i] : i번째 로그가 실행중이면 1, 아니면 0
딕셔너리 시간 순서대로 정렬해서 for문 돌리면서
그 인덱스 값이 처음 나오면 1로, 두번째면 0으로 바꿔주기 -> 그 시간동안 켜져 있음

시간 전처리: start에 0.999 빼주기(1초동안 몇개 켜져있나 검사하는 것이므로)
"""

def solution(lines):
    d = {}
    for i, line in enumerate(lines):
        a = line.split()
        h,m,s = a[1].split(":")
        end = round(int(h)*3600 + int(m)*60 + float(s) , 4)
        start = round(end - float(a[2][:-1]) + 0.001 - 0.999, 4)
        # 중복 제거해주기
        while end in d: end -= 0.000001
        while start in d: start -= 0.000001
        d[start] = i; d[end] = i
                
    answer = 0
    s = [0] * len(lines)
    
    tmp = 0
    lst = sorted(d.keys())
    print(lst)
    for t in lst:
        i = d[t]
        s[i]^=1
        tmp += (s[i]*2-1)
        print(s,tmp)
        answer = max(answer, tmp)
        
    return answer

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
