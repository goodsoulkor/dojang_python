# unit 37. 두 점 사이의 거리 구하기

# 클래스로 점 구현하기
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(x=30, y=20)  # point1
p2 = Point2D(x=60, y=50)  # point2

print("p1: {} {}".format(p1.x, p1.y))
print("p2: {} {}".format(p2.x, p2.y))
print()

# 피타고라스의 정리로 두 점 구하기
# a 제곱 + b 제곱 = c 제곱
a = p2.x - p1.x  # 선 a의 길이
b = p2.y - p1.y  # 선 b의 길이

# c의 길이를 계산하려면 제곱근을 구해야 함
# math 모듈의 sqrt 함수 사용
import math

c = math.sqrt((a * a) + (b * b))  # (a * a) + (b * b)의 제곱근을 구함
print(c)

# 여기서 거듭 제곱을 구하는 math.pow(값, 지수)를 사용해도 됨
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(c)

# ** 연산자 사용
c = math.sqrt((a**2) + (b**2))
print(c)
print()

# 절대값 함수
# 내장 함수 abs 또는 math 모듈의 fabs 함수를 사용하면 양수 또는 음수를 절대값으로 만들 수 있다.
d = 10
d1 = -10
print(abs(d), abs(d1))
print(math.fabs(d), math.fabs(d1))
print()

# nametuple 사용하기
# nametuple은 자료형 이름과 요소의 이름을 지정하면 클래스를 만들어 준다.
# nametuple을 사용하여 점을 표현한 뒤 두 점의 거리를 구하기
import collections

Point2D2 = collections.namedtuple("Point2D2", ["x", "y"])  # nametuple로 점 표현

p1 = Point2D2(x=30, y=20)
p2 = Point2D2(x=60, y=50)

a = p2.x - p1.x
b = p2.y - p1.y

c = math.sqrt((a**2) + (b**2))
print(c)
