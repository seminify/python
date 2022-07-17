import turtle
import random

screen = turtle.Screen()
image1 = 'front.gif'
image2 = 'back.gif'
screen.addshape(image1)
screen.addshape(image2)
t1 = turtle.Turtle()
s = 'y'
while s == 'y':
    coin = random.randint(0, 1)
    if coin == 0:
        t1.shape(image1)
        t1.stamp()
        print('앞면입니다.')
    else:
        t1.shape(image2)
        t1.stamp()
        print('뒷면입니다.')
    s = input('계속 (y/n): ')
print('게임이 종료되었습니다.')
