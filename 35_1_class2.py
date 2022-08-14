# unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기

# 클래스 속성과 인스턴스 속성
# __init__ 메서드에서 만들었던 속성은 인스턴스 속성이다.

# 클래스 속성
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag("book")

maria = Person()
maria.put_bag("key")

print(james.bag)
print(maria.bag)

print(james.__dict__)
print(Person.__dict__)
print()

# 인스턴스 속성 사용하기
class Person2:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james2 = Person2()
james2.put_bag("book")

maria2 = Person2()
maria2.put_bag("key")

print(james2.bag)
print(maria2.bag)
print()

# 클래스 속성: 모든 인스턴스가 공유, 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
# 인스턴스 속성: 인스턴스 별로 독립되어 있음, 각 인스턴스가 값을 따로 저장해야 할 때 사용

# 비공개 클래스 속성 사용하기
class Knight:
    __item_limit = 10  # 비공개 클래스 속성

    def print_item_limit(self):  # 클래스 안에서만 접근할 수 있음
        print(Knight.__item_limit)


x = Knight()
x.print_item_limit()
# print(Knight.__item_limit)  # 오류


# 독스트링
class Person:
    """사람 클래스"""

    def greeting(self):
        """인사 메서드"""
        print("Hello")


print(Person.__doc__)
print(Person.greeting.__doc__)

maria = Person()
print(maria.greeting.__doc__)
print()

# 정적 메서드 사용하기
# @staticmethod를 붙인다. 이때 정적 메서드는 매개변수에 self를 붙이지 않는다.
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)
Calc.mul(10, 20)
print()

# 인스턴스 속성, 인스턴스 메서드가 필요없을 때 사용한다.
# 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수를 만들 때 사용한다.

# 파이썬 자료형의 인스턴스 메서드와 정적 메서드
a = {1, 2, 3, 4}
a.update({5})  # 인스턴스 메서드
print(a)
print(set.union(a, {6}))  # 정적(클래스) 메서드
print()
# 이처럼 인스턴스의 내용을 변경해야 할 때는 update와 같이 인스턴스 메서드를 사용하고
# 인스턴스 내용과 상관없이 결과만 구하면 될 때는 set.union과 같이 정적 메서드로 작성하면 됨

# 클래스 메서드 사용하기
# @classmethod 를 붙인다. 이때 클래스 메서드의 첫 번째 매개변수에 cls를 지정해야 한다.
class Person:
    count = 0  # 클래스 속성

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print("{0}명 생성되었습니다.".format(cls.count))  # cls로 class 속성에 접근


james = Person()
maria = Person()

Person.print_count()
# 클래스 메서드는 메서드 안에서 클래스의 속성, 클래스 메서드에 접근해야 할 때 사용한다.
# 특히 cls를 사용하면 메서드 안에서 현재 클래스의 인스턴스를 만들 수도 있다.
# 즉, cls는 클래스이므로 cls()는 Person()과 같다.
"""
@classmethod
def create(cls):
    p = cls()  # 인스턴스 생성
    return p
"""
