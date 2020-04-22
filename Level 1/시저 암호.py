#https://programmers.co.kr/learn/courses/30/lessons/12926
#숏코딩이 너무 재밌다..
solution = lambda s,n:"".join([[" ",chr((ord(i)-65+n)%26+65),chr((ord(i)-97+n)%26+97)][int(i!=" ")+int(96<ord(i))] for i in s])


s = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1,26):
    print(solution(s,i))
