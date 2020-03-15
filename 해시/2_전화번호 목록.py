#https://programmers.co.kr/learn/courses/30/lessons/42577
"""
한 전화번호가 다른 전화번호의 접두사가 되는 경우가 있는지 찾는 문제
phone_book의 길이가 1000000이므로 nlogn 이하로 짜야함
정렬하면 알아서 번호 순서대로 들어가지므로, 자기 뒷 번호가 자기보다 길고 시작이 같으면 리턴
"""

def solution(phone_book):
    phone_book.sort() #번호순으로 정렬
    check = phone_book[0]
    for v in phone_book[1:]:
        if v == check: return False
        elif len(v) > len(check): # 더 길고 같으면 리턴
            if check == v[:len(check)]: return False
        check = v # 다르면 체크할 숫자 바꿔주기
    return True


print(solution(	["12", "123", "1235", "567", "88"]))
