#카카오 코테 실전 5번
# 4시 45분 해결
"""
징검다리가 있고, 한번에 점프할 수 있는 최대 칸 수가 k라고 주어졌음
간단하게 생각해보면 (k+1)개 씩 잘라서 각각 탐색해보면 구할 수 있을 거임
그런데 아마 이러면 효율성이 터질거임
리스트 사이즈를 20만으로 줬으니까 nlogn 안으로 구현해야 한다는 소린데...
흐으음

연속한 k개가 터지는지 확인해야 하니까
가장 첫번 째 값부터 체크해 나가면서
자기보다 큰지 작은지만 확인?
그러면서 자기보다 작은 가장 큰 수 저장해뒀다가
k번 이상 갔을 때에 자기보다 큰 게 나와주면 그 사이 다 끝났을 때 펑
아님 자기보다 살짝 작은게 나와줘도 펑

1) 가장 작은 값부터 정렬한 임시 리스트를 하나 만들어주기
2) 임시 리스트에서 이진 탐색하면서 값 하나씩 설정해주기
3) 지금 설정한 값만큼 뺐을 때 통과가 되는지 체크해주기

-> 정렬 O(nlogn)
탐색 O(logn)
각 탐색에 대해 통과 여부 체크 O(n)
--> O(nlogn) + O(logn * n) 으로 돌아갈 것 같음
그런데 얘도 타임리밋 걸림 문제가 뭐지
탐색이 O(n)이 아니였음 -> 고쳐주니까 해결
"""

def solution(stones, k):
    if k == len(stones): #예외 처리: k가 전부 다 커버되는 경우 그냥 최댓값 출력
        return max(stones) 

    sort_s = sorted(stones) # 돌을 숫자 크기순서로 정렬해준 친구
    #print(sort_s, stones)
    #print(sort_s)
    #print(stones)
    n = len(stones)
    begin = 0; end = n - 1
    while begin <= end: # 이진 탐색 해주기
        mid = (begin+end)//2
        #print(begin, end, mid, sort_s[mid])
        """
        이 부분 로직을 좀 수정해줘야 빠르게 돌아갈듯
        for다음 max 쓰면 너무 커지나봄
        
        for i in range(n - k + 1): # 첫 번 째 돌부터 뒤에서 k번째 돌까지
            if max(stones[i:i+k]) < sort_s[mid]:
                print(1)
                # i부터 i+k-1 번째 돌까지 전부 mid번 째 돌 사이즈보다 작으면
                # 이만큼이 전부 빈거니까 건널 수 없음
                end = mid - 1
                break
        else: # 그런 경우가 없으면 = 이 돌 사이즈까지는 문제 없으면
            print(2)
            begin = mid + 1
        print(begin, end, mid)
        """
        i = 0
        check = True
        while i < n - k + 1:
            for j in range(i,i+k):
                if stones[j] > sort_s[mid]: # 더 큰 값 찾았으면
                    i = j+1 # i~j까지는 다시 탐색할 필요 없으니까 바로 점핑
                    break
            else: # 하나도 못찾았으면
                check = False
                break

        if check: # 가능한 경우 -> begin을 뒤로
            begin = mid + 1
        else: # 불가능한 경우 -> end를 앞으로
            end = mid - 1
            
    # 5 5 6 -> 5 5 4 되고 끝나는 경우 마지막 탐색이 불가능했던 거니까 5의 값
    # 5 5 6 -> 6 6 6 -> 6 6 5 되고 끝나는 경우 5는 가능, 6은 불가능 -> 5의 값
    # 6 6 6 -> 7 6 6 되는 경우 가능했던 거니까 6의 값
    
    # sort_s[end] 로 넣어주면 된다고 생각했음
    # 그런데 sort_s[begin]으로 넣으니까 맞았음 이유가 뭘까
    # 좀따 생각해보기로
    
    #print(begin, end, mid)
    #print(sort_s[begin], sort_s[end], sort_s[mid])
    return sort_s[begin]

import random
stones = [random.randint(1,100) for _ in range(30)]
k = 4
print(solution(stones, k))
