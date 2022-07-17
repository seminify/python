phone_book = {'홍길동': '010-1234-5679',
              '강감찬': '010-1111-2222',
              '이순신': '010-3333-4444'}
del phone_book['홍길동']
print(phone_book)
print(phone_book.pop('이순신'))
print(phone_book)
