#https://programmers.co.kr/learn/courses/30/lessons/17686
"""
되게 정규표현식 쓰고 싶게 생긴 문제
그냥 head number tail 노가다로 찾아줘도 될 것 같음
찾은 다음에 key에 하나씩 넣어주면 될 듯
다른 풀이 보니까 split에도 \d+ 들어갈 수 있나봄 처음알았
re.split 으로 나눌 수 있
"""
import re

def solution(files):
    list = []
    for c in files:
        # match : 처음부터 확인, \D: 숫자가 아닌 것과 매치, +: 숫자 나올때까지 반복       
        a = re.match("[\D]+",c)

        # match의 group 쓰면 뽑아진 문자 출력해줌
        c = c[len(a.group()):] # 스플라이싱 해서 지우기
        
        b = re.match("[\d]+",c) # \d: 숫자와 매치
        c = c[len(b.group()):] # 한번 더
        
        list.append([a.group(), b.group(), c]) # 스플라이싱 해서 리스트에 넣어주기

    # 대소문자 구분 없이 1차 정렬, 숫자로 2차 정렬
    list.sort(key = lambda x: (x[0].upper(), int(x[1])))
    
    # 스플라이싱 한거 다시 합쳐주기
    answer = ["".join(i) for i in list]
    
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
