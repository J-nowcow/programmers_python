def solution(phone_book):
    phone_book.sort()
    check = phone_book[0]
    for v in phone_book[1:]:
        if v == check: return False
        elif len(v) > len(check):
            if check == v[:len(check)]: return False
        check = v
    return True


print(solution(	["12", "123", "1235", "567", "88"]))
