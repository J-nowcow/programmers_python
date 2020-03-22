#https://programmers.co.kr/learn/courses/30/lessons/60060
"""
words의 길이 10만 이하
단어 길이의 합 100만 이하 -> 이거 어떻게 써먹을까
각 단어의 길이 만 이하

? 가 접두사 접미사 둘중 하나로만 줬으니까 좀 간단하게 풀 수 있을 듯
가장 간단한 방법은 그냥 정렬 두개 해서 비교하기...?

탐색을 이진 탐색으로 구현해줘야 O(nlogn) 으로 구현이 가능할 듯
+) 트라이 써도 O(nlogn)으로 구현할 수 있고 이게 정해라고 함

"""
def find(list, word):
    # 이진 탐색으로, word가 list에 포함되는 단어들을 찾아서
    # 포함되는 마지막 단어 인덱스 - 포함되는 첫 단어 인덱스 + 1 해주기
    # 일단 그전에 n으로 짜면 터지는지 체크 -> 터짐
    
    if len(list) < 10: # 리스트 값이 작으면 노가다가 더 빠름
        count = 0
        for i in list:
            if i.startswith(word):
                count += 1
        return count
    
    start = 0; end = len(list) - 1 # 일단 처음과 끝
    
    # case 1. 처음 끝 둘다 맞으면 그냥 바로 리턴
    if list[start].startswith(word) and list[end].startswith(word):
        return len(list)

    
    # case 2. 끝 부분 찾아주기
    if not list[-1].startswith(word):
        while start <= end:
            mid = (start+end)//2
            if list[mid] > word: # 더 크면 end를 당겨와야 함
                if list[mid].startswith(word): # 하지만 답이라면 start를 밀어야함
                    start = mid + 1
                else:
                    end = mid - 1
            else: # 더 작으면 start를 밀어줘야 함
                start = mid + 1
        b = start - 1
        start = 0; end = b
    else:
        b = end
    # case 3. 시작 부분 찾아주기
    if not list[0].startswith(word):
        while start <= end:
            mid = (start + end) // 2
            if list[mid] > word:
                end = mid - 1
            else:
                if list[mid].startswith(word):
                    end = mid - 1
                else:
                    start = mid + 1
        a = end + 1
    else:
        a = start
    return b - a + 1
    

def solution(words, queries):
    answer = []
    rwords = sorted([ i[::-1] for i in words ], key = lambda x:(len(x),x)) # 뒷자리부터 정렬해준 친구
    words.sort(key = lambda x:(len(x),x))
    # 정렬된 리스트에서, 같은 길이만 탐색하는게 시간 줄일 수 있음
    tmp = len(words[0])
    
    len_list = [tmp] # 길이 값 저장해주는 리스트
    len_point = [0] # 위의 len_list의 인덱스 위치

    k = len(words)
    for i in range(k):
        if len(words[i]) > tmp:
            len_list.append(len(words[i]))
            len_point.append(i)
            tmp = len(words[i])
            
    # print(len_list, len_point)
    len_list.append(10001) # max 값
    len_point.append(k) # max index

    m = {} # 중복인거 고려하기 위한 딕셔너리
    for q in queries: # 각 쿼리에 대해 탐색하기
        try:
            # words[a:b]를 하면 q와 같은 길이의 words만 자를 수 있음
            t = len_list.index(len(q))
            a, b = len_point[t], len_point[t+1]

            if len(q.strip("?")) == 0: # 전부 ?이면 바로 넣기
                answer.append(b-a)
            elif q in m: # 중복이면 바로 넣
                answer.append(m[q])
            else:
                if q[0] != "?": # 접미사인 경우
                    answer.append(find(words[a:b], q.strip("?")))
                    
                else: # 접두사인 경우 뒤집어서 탐색해주기
                    answer.append(find(rwords[a:b], q.strip("?")[::-1]))
                m[q] = answer[-1]
        except: # 그 길이 값이 없으면 answer에 0 추가
            answer.append(0) 
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))            
