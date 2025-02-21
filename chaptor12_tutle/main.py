# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할겁니다
from random import choice
from turtle import Turtle, Screen
import random

t = Turtle()        # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()   # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# t.penup()
# t.forward(20)
# t.pendown()
# t.forward(20)
# t.penup()
# t.forward(20)
# t.pendown()
# t.forward(20)
# t.penup()
# t.forward(20)
# t.pendown()
# t.forward(20)
# t.penup()
# t.forward(20)
# t.pendown()
# t.forward(20)
# t.penup()
# t.forward(20)
# t.pendown()
# t.forward(20)
#
# for _ in range(10):    # 그냥 반복을 10번 하는 거고 변수를 사용하지 않았기 때문에 _를 썼습니다(i나 n이 아니라)
#     t.penup()          # 점선
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# for _ in range(10):     # 사각형
#     t.forward(100)
#     t.left(90)

# for _ in range(4):    # 사각형
#     t.forward(100)
#     t.left(90)
#
# for _ in range(3):    # 삼각형
#     t.forward(100)
#     t.left(120)

# for _ in range(3):    # 삼각형
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(120)

# for _ in range(4):      # 사각형
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(90)
#
# for _ in range(6):      # 육각형
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(60)

# for _ in range(5):      # 오각형
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(72)

# for _ in range(5):      # 오각형
#     for _ in range(10):
#         t.penup()
#         t.forward(5)
#         t.pendown()
#         t.forward(5)
#     t.left(72)

def dotted_line():  # 점선
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()
#
# for _ in range(3):  # 삼각형
#     dotted_line()
#     t.left(120)
#
# # 이상의 함수를 사용하여 사각형을 그린다고 가정했을 때
#
# for _ in range(4):  # 사각형
#     dotted_line()
#     t.left(90)
#
# for _ in range(5):  # 오각형
#     dotted_line()
#     t.left(72)
#
# for _ in range(6):  # 육각형
#     dotted_line()
#     t.left(60)

# def draw_figures(num):
#     for _ in range(num):
#         dotted_line()
#         t.left(360 / num)
#         if  num + 1:
#             num <= 10

# 해당 부분까지 다 하신 부분들은
# 오각형, 육각형 ... 삼각형까지 그려볼 수 있도록 하고
# 이후 코드를 축약할 방법에 대해서 고민하도록 하겠습니다.

# 1. draw_figures(num)을 정의하시오.
# 2. num이 3 미만이라면 "도형을 그릴 수 없습니다"가 출력되고 매서드를 종료하시오.
# 3. 3이상이라면 해당 매서드가 실행될 수 있도록 하시고,
# 4. 반복문을 통해 draw_figures를 호출해 삼각형부터 십각형까지 그리는데,
# 5. 도형마다 색깔이 다를 수 있도록 작성하시오.

# def draw_figures(num):
#     if num < 3:
#         print("도형을 그릴 수 없습니다.")
#         return      # 함수에서 return 다음 아무것도 입력하지 않으면 함수 종료
#     # elif num >= 3:
#     #     for _ in range(num):
#     #         t.left(360 / num)
#     for _ in range(num):
#         t.forward(100)
#         t.left(360 / num)
#         t.color(random.choice(colors))

def draw_dotted_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360 / num)

# 랜덤 객체를 생성
random = random.Random()

colors = [
    "forest green",
    "mint cream",
    "steel blue",
    "medium blue",
    "firebrick",
    "slate blue",
    "indigo",
    "yellow"
]

t.speed(10)
# 내부에 거북이 색깔들을 요소로하는 리스트를 완성
# 랜덤 모듈을 사용해서요(행맨에서 했습니다)

# for i in range(3, 11, 1):
#     t.color(random.choice(colors))
#     draw_dotted_figures(i)

# draw_figures(3)
# draw_figures(4)
# draw_figures(1)

# for i in range(11):
#     draw_figures(i)
'''
    .heading() 매서드:
        거북이가 바라보는 방향을 나타내는 속성으로 도(degree) 단위로 나타남.
        
        해당 매서드는 콘솔탕에 float 형태로 출력됩니다.
        0도 : 동
        90도 : 북
        180도 : 서
        270도 : 남
        
    .setheading() 매서드 :
        특정 각도로 거북이를 회전시키는 매서드
    
    .circle() 매서드 :
        거북이가 원 그리는 매서드
'''
# t.forward(100)
# print(t.heading())
# t.forward(90)
# print(t.heading() * 100)

# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(10)
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading() + 10)
# t.circle(100)

# for _ in range(360 // 10):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading() + 10)

# 이상의 네 줄의 코드를 응용하여 draw_spriogaraph(size_of_gap)로 함수화 하시오.

def draw_spriogaraph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading() + size_of_gap)

t.speed(0)
draw_spriogaraph(2)

















screen.exitonclick()





















