# unit 33. 클로저 사용하기

# 변수의 사용범위
x = 10  # 전역 변수


def foo():
    print(x)  # 전역 변수 출력


foo()
print(x)  # 전역 변수 출력
print()


def foo():
    x = 10  # foo의 지역 변수
    print(x)  # foo의 지역 변수 출력


foo()
print()
# print(x)  foo의 지역 변수는 출력할 수 없다.


# 함수 안에서 전역 변수 변경하기
x = 10


def foo():
    x = 20  # x는 foo의 지역변수
    print(x)  # foo의 지역 변수 출력


foo()
print(x)  # 전역 변수 출력
print()

x = 10


def foo():
    global x  # 전역 변수 x 사용
    x = 20  # x는 전역 변수
    print(x)  # 전역 변수 출력


foo()
print(x)  # 전역 변수 출력
print()

# 전역 변수가 없을 때 global 사용 시 해당 변수는 전역 변수가 된다.

# 함수 안에서 함수 만들기
"""
def 함수1():
    코드
    def 함수2():
        코드
"""


def print_hello():
    hello = "Hello, world!"

    def print_message():
        print(hello)

    print_message()


print_hello()
print()

# 지역 변수 범위
# 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있다.

# 지역 변수 변경하기
def A():
    x = 10

    def B():
        x = 20

    B()
    print(x)


A()
# 함수에서 변수를 만들면 항상 현재 함수의 지역 변수가 된다.
print()

# 현재 함수의 바깥쪽 지역 변수를 변경하려면 nonlocal을 사용한다.
def A():
    x = 10

    def B():
        nonlocal x
        x = 20

    B()
    print(x)


A()
print()

# nonlocal이 변수를 찾는 순서
# nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 찾는다.
def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)

        C()

    B()


A()
print()

# global로 전역 변수 사용하기
# 함수가 몇 단계든 상관없이 global을 사용하면 무조건 전역 변수를 사용한다.
x = 1


def A():
    x = 10

    def B():
        x = 20

        def C():
            global x
            x = x + 30
            print(x)

        C()

    B()


A()
print()

# 클로저 사용하기
def cal():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b

    return mul_add


c = cal()
print(c(1), c(2), c(3), c(4), c(5))
# 함수를 둘러싼 환경(지역변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)라고 한다.
# 지역변수와 코드를 묶어서 사용하고 싶을 때 사용한다.
# 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용

# TODO 여기부터 진행
