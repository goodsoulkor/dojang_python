# unit 36. 사람 클래스로 학생 클래스 만들기 - 상속
class Person:
    def greeting(self):
        print("Hello")


class Student(Person):
    def study(self):
        print("Do study")


james = Student()
james.greeting()
james.study()
print()

# 상속 관계 확인하기 - issubclass
class Person:
    pass


class Student(Person):
    pass


print(issubclass(Student, Person))
print()

# 상속 관계와 포함 관계 알아보기

# 상속 관계
"""
상속은 명확하게 같은 종류이며 동등한 관계일 때 사용한다.
즉, 학생은 사람이다 라고 했을 때 말이 되면 동등한 관계이다.
is-a 관계 -> Student is a Person
"""

# 포함관계
# 사람 목록을 관리하는 클래스
class Person:
    def greeting(self):
        print("Hello")


class Person_List:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):
        self.person_list.append(person)


# 사람 목록은 사람을 가지고 있다. - has-a
# PersonList has a Person

# 동등한 관계일 때는 상속하고 그 이외에는 속성에 인스턴스를 넣는 포함 방식으로 사용

# 기반 클래스의 속성 사용하기
class Person:
    def __init__(self):
        print("Person __init__")
        self.hello = "hello"


class Student(Person):
    def __init__(self):
        print("Student __init__")
        self.school = "Python coding dojang"


james = Student()
print(james.school)
# print(james.hello)  # 에러 발생
print()

# super()로 기반 클래스 초기화 하기
class Person:
    def __init__(self):
        print("Person __init__")
        self.hello = "hello"


class Student(Person):
    def __init__(self):
        print("Student __init__")
        super().__init__()  # 기반 클래스 __init__ 호출
        self.school = "Python coding dojang"


james = Student()
print(james.school)
print(james.hello)
print()

# 기반 클래스를 초기화하지 않아도 되는 경우
class Person:
    def __init__(self):
        print("Person __init__")
        self.hello = "hello"


class Student(Person):
    pass


james = Student()
print(james.hello)
print()

# 명확하게 표현
class Student(Person):
    def __init__(self):
        print("Student __init__")
        super(Student, self).__init__()
        self.school = "python coding dojang"


# 메서드 오버라이딩
class Person:
    def greeting(self):
        print("hello")


class Student(Person):
    def greeting(self):
        print("Hi")


james = Student()
james.greeting()
print()


class Person:
    def greeting(self):
        print("hello")


class Student(Person):
    def greeting(self):
        super().greeting()  # 슈퍼 클래스의 메서드를 호출하여 중복을 줄임
        print("Hi")


james = Student()
james.greeting()
print()
