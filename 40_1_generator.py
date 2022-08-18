# unit 40. 제너레이터와 yield

# 제너레이터는 이터레이터를 생성해주는 함수이다.
# 함수 안에 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)를 지정한다.
# yield 값
def number_generator():
    yield 0
    yield 1
    yield 2


# for i in number_generator():
#     print(i)

# 제너레이터 객체가 이터레이터인지 확인
# dir 함수로 확인
g = number_generator()
# print(dir(g))
# print(g.__next__())

# 이터레이터는 __next__ 메서드에서 직접 return으로 값을 반환했지만 제너레이터는 yield에 지정한 값이 반환값으로 나온다.
# 또한 이터레이터는 raise로 StopIteration 예외를 직접 발생시켰지만 제너레이터는 함수의 끝까지 도달하면 자동으로 발생된다.

# for와 제너레이터
print(g.__iter__())
print()
# yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보한다.

# yield의 동작 과정
a = next(g)
print(a)
b = next(g)
print(b)
c = next(g)
print(c)
print()

# 제너레이터 함수를 끝내지 않은 상태에서 yield로 함수 바깥에 값을 전달
# return은 반환 즉시 함수 종료

# 제너레이터 만들기
# range(횟수) 처럼 동작
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


# for i in number_generator(3):
#     print(i)

# yield에서 함수 호출하기
# 리스트에 들어있는 문자열을 대문자로 변환하여 함수 바깥으로 전달
def upper_generator(x):
    for i in x:
        yield i.upper()  # 함수의 반환값을 바깥으로 전달


fruits = ["apple", "pear", "grape", "pineapple", "orange"]

for i in upper_generator(fruits):
    print(i)
print()

# yield from 으로 값을 여러번 바깥으로 전달
def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i


for i in number_generator():
    print(i)
print()
# 이런 경우 yield from을 사용한다.
# python 3.3 이상부터 사용 가능
# yield from 반복 가능한 객체
# yield from 이터레이터
# yield from 제너레이터
def number_generator():
    x = [1, 2, 3]
    yield from x  # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달


for i in number_generator():
    print(i)
print()

# yield from 에 제너레이터 객체 지정하기
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def three_generator():
    yield from number_generator(3)  # 숫자를 세 번 바깥으로 전달


for i in three_generator():
    print(i)
print()

# 제너레이터 표현식
# 리스트 표현식을 괄호로 묶으면 제너레이터 표현식이 된다.
# 리스트 표현식은 처음부터 리스트 요소를 만들어 내지만 제너레이터 표현식은 필요할 때 요소를 만들어내므로 메로리를 절약할 수 있다.
# (식 for 변수 in 반복가능한객체)

a = [i for i in range(50) if i % 2 == 0]
print(a)
b = (i for i in range(50) if i % 2 == 0)
print(b)
