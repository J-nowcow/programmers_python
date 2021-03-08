#https://programmers.co.kr/learn/courses/30/lessons/72412

# 5비트 숫자로 정보 표현 : 0 ~ 31
# n % 4 == 0 : cpp, 1: java, 2 : python
# n >> 2 % 2 == 0 : backend, 1 : frontend
# n >> 3 % 2 == 0 : junior, 1 : senior
# n >> 4 % 2 == 0 : chicken, 1 : pizza

# 각각의 비트에 해당하는 값 정렬한 다음 이진탐색으로 찾아주기

def solution(info, query):
    dic = dict([(i,[]) for i in range(32)])
    for i in info:
        tmp = 0
        i  = i.split()
        tmp += ["cpp","java","python"].index(i[0])
        tmp += ["backend", "frontend"].index(i[1]) << 2
        tmp += ["junior", "senior"].index(i[2]) << 3
        tmp += ["chicken", "pizza"].index(i[3]) << 4
        dic[tmp].append(int(i[4]))

    for i in dic:
        dic[i].sort()

    answer = []
    
    for q in query:
        q = q.split()
        if q[0].strip() == "-":
            bit = [0,1,2]
        else:
            bit = [["cpp","java","python"].index(q[0])]

        tmp = []
        for i in bit: tmp.append((1 << 2) + i)
        if q[2].strip() == "-": bit += tmp
        elif q[2].strip() == "frontend": bit = tmp

        
        tmp = []
        for i in bit: tmp.append((1 << 3) + i)
        if q[4].strip() == "-": bit += tmp
        elif q[4].strip() == "senior": bit = tmp

        tmp = []
        for i in bit: tmp.append((1 << 4) + i)
        if q[6].strip() == "-": bit += tmp
        elif q[6].strip() == "pizza": bit = tmp

        count = 0
        score = int(q[7])
        for i in bit:
            tmp = dic[i]
            if not len(tmp): continue
            start = 0
            end = len(tmp) - 1
            while start <= end:
                mid = (start + end)//2
                if score <= tmp[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            count += (len(tmp) - start)
        answer.append(count)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
