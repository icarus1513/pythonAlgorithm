def solution(phone_book):
    answer = True
    check = False
    phone_book_len = len(phone_book)
    for i in range(phone_book_len) :
        for j in range(i+1,phone_book_len) :
            if phone_book[j].startswith(phone_book[i]) :
                answer = False
                return answer
            elif phone_book[i].startswith(phone_book[j]):
                answer = False
                return answer
    return answer