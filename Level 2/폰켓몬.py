# https://programmers.co.kr/learn/courses/30/lessons/1845

solution = lambda nums: min(len(set(nums)), len(nums)//2)
print(solution([3,3,3,2,2,4]))
