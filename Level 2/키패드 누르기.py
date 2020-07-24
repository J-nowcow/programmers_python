# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    pos = {0:(3,1)}
    for i in range(9):
        pos[i+1] = (i//3,i%3)
    left = (3,0); right = (3,2)
    
    answer = ''
    for i in numbers:
        tmp = pos[i]
        if i in (1,4,7):
            answer += "L"; left = tmp
        elif i in (3,6,9):
            answer += "R"; right = tmp
        else:
            ld = abs(tmp[0]-left[0]) + abs(tmp[1]-left[1])
            rd = abs(tmp[0]-right[0]) + abs(tmp[1]-right[1])
            
            if ld < rd or (ld == rd and hand == "left"):
                answer += "L"
                left = tmp
            else:
                answer += "R"
                right = tmp
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
