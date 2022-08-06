# 21. 터틀 그래픽스로 그림그리기

# 21.1 사각형 그리기
import turtle as t

# t.shape("turtle")
# for i in range(4):
#     t.forward(100)
#     t.rt(90)

# 21.2.1 오각형 그리기
# t.shape("turtle")
# for i in range(5):
#     t.forward(100)
#     t.rt(360 / 5)

# 21.2.2 다각형 그리기
# n = int(input())
# t.shape("turtle")
# for i in range(n):
#     t.forward(100)
#     t.rt(360 / n)

# 21.2.3 다각형에 색칠하기
# n = 6
# t.shape("turtle")
# t.color("red")
# t.begin_fill()
# for i in range(n):
#     t.forward(100)
#     t.rt(360 / n)
# t.end_fill()

# 21.3 원 그리기
# t.shape("turtle")
# t.circle(120)

# 21.3.1 반복해서 원 그리기
# n = 60
# t.shape("turtle")
# t.speed("fastest")
# for i in range(n):
#     t.circle(200)
#     t.right(360 / n)

# t.speed("fastest")
"""
0.5 ~ 10
거북이 속도
fastest - 10
fast - 9
normal - 6
slow - 3
slowest - 1
"""

# 21.3.2 선으로 복잡한 무늬 그리기
# t.shape("turtle")
# t.speed(10)
# for i in range(300):
#     t.forward(i)
#     t.right(91)

# shape
t.shape("classic")
t.speed(1)
t.forward(100)
"""
arrow / turtle / circle / square / triangle / classic
"""

# t.mainloop()
