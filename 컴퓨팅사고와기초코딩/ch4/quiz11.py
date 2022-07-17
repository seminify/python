id = 'ilovepython'
password = '123456'
s = input('아이디를 입력하시오: ')
if s == id:
    s = input('패스워드를 입력하시오: ')
    if s == password:
        print('환영합니다.')
    else:
        print('비밀번호가 다릅니다.')
else:
    print('아이디를 찾을 수 없습니다.')
