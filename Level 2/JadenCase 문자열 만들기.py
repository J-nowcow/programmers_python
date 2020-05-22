# https://programmers.co.kr/learn/courses/30/lessons/12951


solution = lambda s: "".join([s[0].upper()]+[s[i].upper() if s[i-1] == " " else s[i].lower() for i in range(1,len(s))])
print(solution("3people unFollowed me"))
