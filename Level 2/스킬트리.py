# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        idx = 0; check = True
        for j in i:
            if j in skill:
                if skill.index(j) == idx: idx += 1
                else: break
        else: answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))
