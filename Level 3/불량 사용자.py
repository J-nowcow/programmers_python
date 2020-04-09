#카카오 코테 실전 3번
# 3시 17분 해결
"""
테스트 데이터만 보고 트라이 쓰는 문젠줄 알고 식겁했는데 아니네 편안
user_id 크기 8 이하니까 그냥 완전 탐색 문제인듯
재귀로 짜주면 되는듯
따지자면 dfs인가...?
    
"""


def f(user_id, banned_id, check, ban_p, answer, check_list):

    # ban_p: banned_id 몇번째 꺼 밴할 차례인지 확인해주기
    # check_list: 벌써 밴 한적 있는 리스트인지 확인해서 제거해주기
    
    if ban_p == len(banned_id): # 끝까지 도달했으면 = 모든 아이디를 밴했으면
        if check not in check_list: # 중복 아니면
            answer += 1
            tmp = [i for i in check]
            check_list.append(tmp)
            # 굳이 tmp 만들어주는 이유는 이렇게 안하면 check가 바뀌면서 check_list도 계속 영향을 받음
            
        return answer
    
    for i in range(len(user_id)):
        # 비교해줄 친구: user_id[i]와 banned_id[ban_p]
        if check[i] == 1: continue # 이미 밴된 칸이면 패스
        
        elif len(user_id[i]) != len(banned_id[ban_p]): continue # 길이 다르면 다른거니까 패스
        
        else:
            ban = True
            for c in range(len(user_id[i])):
                if banned_id[ban_p][c] != "*" and user_id[i][c] != banned_id[ban_p][c]: # 서로 다르고 * 아니면
                    ban = False
                    break
                
            if ban == True: # 밴 할 수 있는 아이디면
                check[i] = 1
                ban_p += 1 # 1 추가해주고
                answer = f(user_id, banned_id, check, ban_p, answer, check_list) # 다음 위치 재귀로 확인해주기
                check[i] = 0; ban_p-=1 # 확인한 다음엔 0으로 다시 바꿔주기
    return answer

def solution(user_id, banned_id):
    check = [0]*len(user_id) # 그 칸 탐색했는지 체크해주는 리스트
    check_list =[]
    answer = f(user_id, banned_id, check, 0, 0, check_list)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))
