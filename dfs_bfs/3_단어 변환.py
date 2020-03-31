#https://programmers.co.kr/learn/courses/30/lessons/43163
"""
단어가 50개밖에 없으니까 그냥 O(length * words^2)로 짜면 될 것 같음
n 1씩 추가시키면서, begin에 n번째로 찾아진 단어들 넣고 
각 begin에 대해 words 돌면서 다음에 찾아지는 원소들 뽑아내기
단어 비교하는게 O(length)고 begin에 들어가는 원소가 총 n개니까
탐색은 최대 n^2 번 돌아감 -> O(mn^2)

"""

def solution(begin, target, words):
    if target not in words: return 0 # 없는 경우 미리 예외처리

    begin = [begin] # 밑에 계산 하기 위해 리스트로 변환해주기

    for answer in range(1,51): # 최대 50번 안에 못찾으면 없는거임
        tmp = [] # n번 돌았을 때 찾아지는 단어 임시로 저장하는 리스트
        for b in begin:
            for w in words:
                #print(b,w)
                if sum(int(b[i] != w[i]) for i in range(len(b))) == 1: # 같으면 0, 다르면 1 -> 합이 1이면 조건 만족
                    words.remove(w)
                    tmp .append(w)
                    if w == target: return answer # 타겟 찾으면 리턴
        begin = tmp
    return 0 # 끝까지 못찾았으면 0 리턴

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
