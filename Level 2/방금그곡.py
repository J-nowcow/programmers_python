#https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = None

    # 반음계 처리하기 편하도록 다른 문자열로 바꿔놓는다.
    a = "HIJKL"; b = "C#D#F#G#A#"
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        for j in range(5):
            info[3] = info[3].replace(b[j*2:j*2+2], a[j:j+1])
            musicinfos[i] = ",".join(info)

    for i in range(5):
        m = m.replace(b[i*2:i*2+2], a[i:i+1])
        
    for i in musicinfos:
        i = i.split(",")
        # time: 재생 시간
        time = 60 * (int(i[1][0:2]) - int(i[0][0:2])) + int(i[1][3:5]) - int(i[0][3:5])
        string = i[3] * (time//len(i[3])) + i[3][:time%len(i[3])]

        # 찾는 문자열이 string에 포함된다면 조건 고려해서 바꿔준다.
        if m in string:
            if answer == None:
                answer = [i[2], time, i[0]]
            else:
                # 재생 시간이 더 길다면 바꾸기
                if time > answer[1]:
                    answer = [i[2], time, i[0]]
                # 재생 시간이 같고 먼저 입력됐다면 바꾸기
                elif time == answer[1] and i[0] < answer[2]:
                    answer = [i[2], time, i[0]]
                
    return "(None)" if not answer else answer[0]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,musicinfos))
