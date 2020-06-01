#https://programmers.co.kr/learn/courses/30/lessons/12977
"""
리스트에서 3개 뽑는 조합 만들기
3개 숫자의 합 최댓값 3000 -> 에라토스테네스 체 만들어서 찾기
"""
def solution(nums):
    prime = set(range(2,3000))
    for i in range(2, 3000//2+1):
        if i in prime:
            prime -= set(range(2*i,3000,i)) # 소수의 배수들 제거
    
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] in prime:
                    answer += 1
    return answer

nums = [1,2,3,4]
print(solution(nums))
