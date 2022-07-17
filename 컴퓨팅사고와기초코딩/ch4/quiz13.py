import random

print('동전 던지기 게임을 시작합니다.')
while True:
    coin = random.randrange(2)
    if coin == 0:
        print('앞면입니다.')
    else:
        print('뒷면입니다.')
    s = input('계속 (y/n): ')
    if s == 'n':
        break
print('게임이 종료되었습니다.')
