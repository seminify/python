import random

time = random.randint(1, 24)
print('좋은 아침입니다. 지금 시각은 ' + str(time) + '시 입니다.')
sunny = random.choice([True, False])
people = random.randint(0, 20)
print('people: ', people)
if ((time >= 6 and time <= 9) or (time >= 14 and time <= 16) and sunny and (people < 10)):
    print('종달새가 노래를 한다.')
else:
    print('종달새가 노래를 하지 않는다.')
