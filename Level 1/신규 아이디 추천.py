#https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = "".join(re.findall("[\w\-_.]+", new_id))
    new_id = ".".join(re.findall("[^.]+",new_id))
    if not len(new_id): new_id = "a"
    new_id = new_id[:15].strip(".")
    if len(new_id) <= 2: new_id += (3-len(new_id)) * new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
