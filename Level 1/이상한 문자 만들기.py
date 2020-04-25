#https://programmers.co.kr/learn/courses/30/lessons/12930
# 쉽게 될것 같은데 귀찮아서 그냥 스플릿하고 빈칸 하나씩 넣어주기
def solution(s):
    a = s.split()
    answer = ""
    while s and s[0] == " ":
        answer += " "
        s = s[1:]
    for i in a:
        tmp = ""
        t = True
        for j in i:
            if t == 0: tmp += j.lower()
            else: tmp += j.upper()
            t = not t
        answer += tmp
        s = s[len(tmp):]
        while s and s[0] == " ":
            answer += " "
            s = s[1:]
            
    return answer

s = "  try hello world  "
print(solution(s))
