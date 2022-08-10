# unit 29. 함수 사용하기

# hello world! 출력 함수
def hello():
    print("hello, world!")


# 호출
# hello()

# 함수 작성과 호출 순서
# 항상 함수를 먼저 만들고 실행해야 한다.

# 덧셈 함수
def add(a, b):
    print(a + b)


# add(10, 20)

# docstring
def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환합니다."""
    return a + b


print(add.__doc__)

# 함수 결과 반환하기 return
def add(a, b):
    return a + b


x = add(10, 20)
print(x)

# return으로 중간에 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print(a, "입니다.", sep="")


not_ten(5)
not_ten(10)
print()

# 값을 여러개 반환하기
def sub_add(a, b):
    return a + b, a - b


x, y = sub_add(10, 20)
print(x, y)

z = sub_add(10, 20)
print(z)
print()

# 함수의 호출 과정
def mul(a, b):
    c = a * b
    return c


def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)


x = 10
y = 20
add(x, y)
