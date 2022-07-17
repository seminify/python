americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500
american = int(input('아메리카노 판매 개수: '))
cafelatte = int(input('카페라떼 판매 개수: '))
capucino = int(input('카푸치노 판매 개수: '))
sales = american * americano_price
sales += (cafelatte * cafelatte_price)
sales += (capucino * capucino_price)
print('총 매출은', sales, '입니다.')
if sales < 100000:
    print('적자')
else:
    print('흑자')
