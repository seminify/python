phone_book = {'홍길동': '010-1234-5679'}
phone_book['강감찬'] = '010-1111-2222'
phone_book['이순신'] = '010-3333-4444'
for key in sorted(phone_book.keys()):
    print(key, phone_book[key])
