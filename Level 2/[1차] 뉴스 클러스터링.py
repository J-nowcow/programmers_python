#https://programmers.co.kr/learn/courses/30/lessons/17677
"""
두 문자의 자카드 유사도 구하기
정렬한 다음에 앞에부터 하나씩 비교해주면 O(nlogn + 2n)으로 가능

두개 같으면 합집합 교집합 둘다 1 추가, 인덱스도 둘다 추가
아니면 합집합만 1추가, 인덱스 더 작은쪽만 1 추가
"""

def solution(str1, str2):
    #전처리: 두글자씩 끊어서 문자 아닌것 제거 후 정렬
    a = sorted([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    b = sorted([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])

    i = 0; j = 0
    inter = 0; union = 0 # 교집합, 합집합의 크기
    while i < len(a) or j < len(b):
        # 한쪽 집합 다쓰면 합집합에 다른쪽 집합 남은만큼 더해주기
        if i == len(a): union += len(b)-j; break
        elif j == len(b): union += len(a)-i; break
        
        # 같을 때
        if a[i] == b[j]: inter += 1; i += 1; j +=1
        # 다를 때
        elif a[i] > b[j]: j += 1
        else: i += 1
        union += 1

    return 65536 if union == 0 else 65536*inter//union

str1 = "aa1+aa2"
str2 = "12"
print(solution(str1, str2))
