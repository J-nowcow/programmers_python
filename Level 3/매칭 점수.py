# https://programmers.co.kr/learn/courses/30/lessons/42893
"""
기본 점수: word가 등장한 횟수
외부 링크수: 다른 웹페이지로 링크가 걸린 개수
head 안에 들어있는 content= 부분이 주소
body 안에 들어있는 주소들이 외부 링크
"""
import re
def solution(word, pages):
    base = []; link = []; others = [] # 기본 점수, 각각의 주소, 외부 링크
    for i in pages:
        base.append(re.split("[^a-z]+",i.lower()).count(word.lower()))
        link.append(re.findall('<meta property.+>', i)[0].split('"')[3])
        #print(link)
        others.append(re.findall('<a href="(https://.+?)">', i))
        print(others)
        
    # 각각의 링크점수 계산
    s = [0]*len(base)
    for i in range(len(base)):
        if len(others[i]) > 0: s[i] = (base[i] / len(others[i]))
    #print(s)
    
    for i in range(len(others)):
        for j in others[i]:
            if j in link:
                # 다른 링크의 외부링크로 연결되어 있으면 base에 점수 추가
                base[link.index(j)] += s[i]
    #print(base)
    return base.index(max(base))

word = "blind"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word,pages))
