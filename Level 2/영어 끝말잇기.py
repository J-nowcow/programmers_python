#https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n,words):
    for i in range(1,len(words)):
        # 이미 나왔던 단어거나, 마지막 글자와 첫 글자가 다르다면
        if (words[i] in words[:i]) or (words[i-1][-1] != words[i][0]):
            return [i%n + 1, i//n +1]
    # 아무도 탈락하지 않았다면
    return [0,0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n,words))
