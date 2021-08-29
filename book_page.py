def pageCount(n, p):
    # Write your code here
    book = [[i+j for i in range(2)] for j in range(0,n+1,2)]
    if(p > n // 2):
        position = len(book) - 1
    else:
        position = 0
    print(book)
    if(p % 2 != 0):
        page_turn = book.index([p-1, p])
        answer = abs(position - page_turn)
    else:
        page_turn = book.index([p, p+1])
        answer = abs(position - page_turn)

    return answer

print(pageCount(6, 4))
