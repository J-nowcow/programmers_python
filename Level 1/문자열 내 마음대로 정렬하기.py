#https://programmers.co.kr/learn/courses/30/lessons/12915
solution = lambda strings, n: sorted(strings, key = lambda x: (x[n],x))

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))
