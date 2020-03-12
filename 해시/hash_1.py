def solution(participant, completion):
    participant.sort(); completion.sort()
    for i in range(len(participant)):
        if i != len(completion) and participant[i] == completion[i]: pass
        else: return participant[i]

participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]
print(solution(participant, completion))
