# unit 32. 람다 표현식 사용하기
# def plus_ten(x):
#     return x + 10


# print(plus_ten(1))

# print(lambda x: x + 10)

# plus_ten = lambda x: x + 10
# print(plus_ten(1))

# 람다 표현식 자체를 호출하기
# print((lambda x: x + 10)(1))

# 람다 표현식 안에서는 변수를 만들 수 없다.
# lambda x: y = 10; x + y  오류
# 바깥에 있는 변수는 사용할 수 있다.
# y = 10
# print((lambda x: x + y)(1))

# 람다 표현식을 인수로 사용하기
# def plus_ten(x):
#     return x + 10


# print(list(map(plus_ten, [1, 2, 3])))

# print(list(map(lambda x: x + 10, [1, 2, 3])))

# 람다 표현식으로 매개변수가 없는 함수 만들기
# lambda : 1
# x = 10
# lambda : x

# 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# print(b)
# 람다에서 if 사용 시 반드시 else 도 사용해야 한다.

# elif 사용할 수 없다.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# print(b)

# map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
c = list(map(lambda x, y: x * y, a, b))
# print(c)

# filter 사용하기
# 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져온다.
# filter(함수, 반복가능한객체)
def f(x):
    return x > 5 and x < 10


a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
b = list(filter(f, a))
# print(b)

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
b = list(filter(lambda x: x > 5 and x < 10, a))
# print(b)

# reduce 사용하기
# 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과아 누적해서 반환하는 함수
"""
from functools import reduce
reduce(함수, 반복가능한객체)
"""
from functools import reduce

# 리스트에 저장된 요소를 순서대로 더한 뒤 누적된 결과 반환
def f(x, y):
    return x + y


a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, a)
print(b)

a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) - 1):
    x = x + a[i + 1]

print(x)
