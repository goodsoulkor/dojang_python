# 36. 다중 상속 사용하기
class Person:
    def greeting(self):
        print("Hello")


class University:
    def manage_credit(self):
        print("학점 관리")


class Undergraduate(Person, University):
    def study(self):
        print("공부하기")


james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()
print()

# 다이아몬드 상속
class A:
    def greeting(self):
        print("안녕하세요 A 입니다.")


class B(A):
    def greeting(self):
        print("안녕하세요 B 입니다.")


class C(A):
    def greeting(self):
        print("안녕하세요 C 입니다.")


class D(B, C):
    pass


x = D()
x.greeting()
print()

# 메서드 탐색 순서
print(D.mro())
print(D.__mro__)
# class D(B, C): 로 다중 상속 시 B, C 순서로 메서드를 찾는다.

# 추상 클래스 사용하기
# 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용한다.
from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass


class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")


james = Student()
james.study()
james.go_to_school()
# 추상 클래스에서 정의한 메서드를 정의해줘야 오류가 나지 않는다.
# 추상 클래스는 인스턴스로 만들 수 없다.
# james = StudentBase() X
