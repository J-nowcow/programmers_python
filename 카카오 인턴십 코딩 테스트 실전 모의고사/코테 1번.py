#카카오 코테 실전 1번
#2시 12분 해결
"""
하나씩 빈 스택에 채워주면서 같은거 두개 나오면 pop 두번 해주기
board가 가로로 주어져 있는데 이거 세로로 바꿔주면 훨씬 쉬워질듯
더 빠르게 짤 수도 있지만 move 1000 이하고 사이즈 30 이하니까 그냥 연산 3만번 때려도 됨
"""

def solution(board, moves):
    answer = 0
    board = [[board[i][j] for i in range(len(board))] for j in range(len(board))] # 행열 위치 바꿔주기
    
    s = [] # 인형 담아줄 스택
    for i in moves:
        i -= 1 # 위치를 1번부터 줘서 인덱스 계산하기 위해 1 빼주기
        for j in range(len(board)):
            if board[i][j] != 0: # 처음으로 인형 있는 칸
                if len(s) == 0: s.append(board[i][j]) # 비어있으면 추가해주기
                else:
                    if s[-1] == board[i][j]: # 같은 인형을 넣으면
                        s.pop(); answer += 2 # 답 추가
                    else:
                        s.append(board[i][j]) # 아니면 스택 추가
                board[i][j] = 0 #비워주기
                break
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
