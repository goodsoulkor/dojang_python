# unit 34. 클래스 사용하기

# 프로그래밍으로 객체를 만들 때 사용하는 것이 클래스 이다.

# 클래스와 메서드 만들기
class Person:
    def greeting(self):
        print("Hello")


james = Person()

# 메서드 호출하기
# james.greeting()

# 인스턴스와 객체의 차이점
a = list(range(10))
b = list(range(20))
# a, b는 객체
# a, b는 list 클래스의 인스턴스

# 메서드 안에서 메서드 호출하기
class Person:
    def greeting(self):
        print("Hello")

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안에서 메서드 호출


# james = Person()
# james.hello()

# 특정 클래스의 인스턴스인지 확인 - isinstance
class Person:
    pass


james = Person()
print(isinstance(james, Person))
print()

# isinstance는 주로 객체의 자료형을 판단할 때 사용한다.
# 팩토리얼 함수에서 숫자(객체)가 정수일 때만 계산하도록 한다.
def factorial(n):
    if not isinstance(n, int) or n < 0:  # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 속성 사용하기
# 속성(attribute)를 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당한다.
class Person:
    def __init__(self):
        self.hello = "hello"

    def greeting(self):
        print(self.hello)


james = Person()
james.greeting()
print()

# 인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = "hello"
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("{0} I'm {1}".format(self.hello, self.name))


maria = Person("maria", 20, "Seoul")
maria.greeting()

print("name:", maria.name)
print("age:", maria.age)
print("address:", maria.address)
print()

# 클래스의 위치인수, 키워드 인수
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]


maria = Person("maria", 20, "Seoul")


class Person:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.address = kwargs["address"]


maria1 = Person(name="maria", age=20, address="Seoul")
maria2 = Person(**{"name": "maria", "age": 20, "address": "Pusan"})

# 인스턴스를 생성한 뒤 속성 추가하기, 특정 속성만 허용하기
class Person:
    pass


maria = Person()
maria.name = "maria"
print(maria.name)
print()
# 이렇게 추가한 속성은 해당 인스턴스에만 생성된다.

# __init__이 아닌 다른 메서드에도 속성을 추가할 수 있다.
class Person:
    def greeting(self):
        self.hello = "hello"


maria = Person()
# print(maria.hello)  # 오류발생 아직 hello 속성이 없다.
maria.greeting()
print(maria.hello)
print()
# 이렇게 메서드를 호출해야 hello 속성이 추가된다.

# 특정 속성만 허용하고 다른 속성은 제한하고 싶을 때
# __slots__에 허용할 속성 이름을 리스트로 넣어준다.
# __slots__ = ["속성이름1", "속성이름2"]
class Person:
    __slots__ = ["name", "age"]  # name, age 속성만 허용(다른 속성은 생성 제한)


maria = Person()
maria.name = "maria"
maria.age = 20
# maria.address = "Seoul"  # 허용되지 않은 속성을 추가할 때 오류 발생

# 비공개 속성
# 클래스 안에서만 접근할 수 있고 바깥에서는 접근할 수 없다.
# __attribute 와 같이 밑줄 두 개로 시작한다.
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 비공개 속성


maria = Person("maria", 20, "Seoul", 10000)
# print(maria.__wallet)  # 클래스 바깥에서 비공개 속성에 접근하면 에러


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안에서만 접근할 수 있음
        print("remain money {0}".format(self.__wallet))


maria = Person("maria", 20, "Seoul", 10000)
maria.pay(3000)
print()

# 비공개 메서드 사용하기
class Person:
    def __greeting(self):
        print("hello")

    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출가능


james = Person()
# james.__greeting()  # 에러: 비공개 메서드를 클래스 바깥에서 호출할 수 없음
